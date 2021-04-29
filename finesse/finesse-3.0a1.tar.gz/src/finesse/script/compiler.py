"""Kat model compiler.

This takes parsed productions, figures out the dependencies and builds the model in the
correct order.

Sean Leavey <sean.leavey@ligo.org>
"""

import logging
from collections import defaultdict, ChainMap
from io import StringIO
import re
from functools import singledispatchmethod
from networkx import (
    selfloop_edges,
    lexicographical_topological_sort,
    simple_cycles,
    descendants,
    NetworkXUnfeasible,
)
import numpy as np
from .. import Model
from ..symbols import Resolving
from ..utilities import option_list, ngettext
from ..exceptions import (
    FinesseException,
    ModelAttributeError,
    ModelParameterDefaultValueError,
    ModelParameterSelfReferenceError,
)
from . import syntax
from .graph import KatGraph, KatNodeType, KatEdgeType
from .containers import (
    KatToken,
    KatReferenceToken,
    KatScript,
    KatElement,
    KatFunction,
    KatKwarg,
    KatGroupedExpression,
    KatExpression,
    KatArray,
    KatNumericalArray,
)
from .parser import KatParser
from .exceptions import KatScriptError, KatSyntaxError, KatMissingAfterDirective
from .util import duplicates, merge_attributes

LOGGER = logging.getLogger(__name__)


def production(node, graph):
    from .generator import KatUnfiller

    unfiller = KatUnfiller()
    return unfiller.production(node, graph)


def argument_signature_parameter(argument_node, adapter, graph):
    data = graph.nodes[argument_node]
    parameters = adapter.call_signature(exclude_name=True).parameters

    if key_token := data.get("key_token"):
        # It's a keyword argument: just look up the key.
        return parameters[key_token.value]

    # It's a positional argument: look up the correct index.
    return list(parameters.values())[graph.argument_node_order(argument_node)]


class KatCompiler:
    """Kat model compiler."""

    def __init__(self, spec=None):
        if spec is None:
            from .spec import KatSpec

            spec = KatSpec()

        self.spec = spec
        self.graph = None
        self.build_graph = None
        self._parser = None
        self._parameter_dependencies = None

    @property
    def script(self):
        return self._parser.script

    def compile(self, string, **kwargs):
        """Compile the contents of `string`.

        Parameters
        ----------
        string : :class:`str`
            The string to compile kat script from.

        Other Parameters
        ----------------
        kwargs
            Keyword arguments supported by :meth:`.compile_file`.

        Returns
        -------
        :class:`.Model`
            The model compiled from reading `string`.
        """
        return self.compile_file(StringIO(string), **kwargs)

    def compile_file(self, fobj, model=None, resolve=True, build=True):
        """Compile the contents of the specified file.

        Parameters
        ----------
        fobj : :class:`io.FileIO`
            The file object to compile kat script from. This should be opened in text
            mode.

        model : :class:`.Model`, optional
            An existing model to compile the contents of `fobj` into. If not specified,
            a new, empty model is created.

        resolve : :class:`bool`, optional
            Resolve the parsed script. If False, the parsed contents is added to graph
            but no sanity checks are performed and nothing is returned. Defaults to
            True.

        build : :class:`bool`, optional
            Build the parsed script. If False, no Finesse objects will be added to the
            model and nothing will be returned. Defaults to True.

        Returns
        -------
        :class:`.Model` or None
            If `resolve` and `build` are True, the model compiled from reading `fobj`;
            None otherwise.

        Raises
        ------
        :class:`.KatSyntaxError`
            If a syntax error is present in the contents of `fobj`.
        """
        # Reset state.
        self._parser = KatParser()
        self.graph = KatGraph()
        self.build_graph = None
        self._parameter_dependencies = []

        try:
            script = self._parser.parse_file(fobj)
        except KatSyntaxError as e:
            # There was a syntax error. Try to improve the error message using the spec.
            self._reraise_parser_error_in_spec_context(e)

        self._fill(script, self.graph.ROOT_NODE_NAME)

        # At this stage there shouldn't be any dependencies between branches.
        assert self.graph.is_tree()

        if resolve:
            self._resolve()

            if build:
                return self._build(self.graph.ROOT_NODE_NAME, model)

    @property
    def _directive_functions(self):
        return ChainMap(self.spec.commands, self.spec.analyses)

    @property
    def _expression_functions(self):
        return ChainMap(self.spec.expression_functions, self.spec.unary_operators)

    @property
    def _available_functions(self):
        return ChainMap(self._directive_functions, self._expression_functions)

    def _fill(self, value, path, **attributes):
        assert path not in self.graph
        attributes = merge_attributes(
            attributes, self._item_node_attributes(value, path)
        )
        self.graph.add_node(path, **attributes)

        if hasattr(value, "arguments"):
            # Assemble arguments.
            for order, argument in enumerate(value.arguments):
                argument_path = self.graph.item_node_name(order, path)
                self._fill(argument, argument_path)
                self.graph.add_edge(
                    argument_path, path, type=KatEdgeType.ARGUMENT, order=order
                )

        return attributes

    @singledispatchmethod
    def _item_node_attributes(self, item, path):
        """Get the attributes for `item` to be added to the corresponding node."""
        raise NotImplementedError(
            f"don't know how to handle an item with type '{item.__class__.__name__}'"
        )

    @_item_node_attributes.register(KatScript)
    def _(self, script, path):
        return {"type": KatNodeType.ROOT, "extra_tokens": script.extra}

    @_item_node_attributes.register(KatToken)
    def _(self, token, path):
        attributes = {"token": token}
        if token.type == "NAME":
            # This could be a keyword, constant or parameter reference.
            name = token.value

            if name in self.spec.keywords:
                token_type = KatNodeType.KEYWORD
            elif name in self.spec.constants:
                token_type = KatNodeType.CONSTANT
            else:
                # Assume this is a parameter like `l1.P`.
                self._parameter_dependencies.append(path)
                token_type = KatNodeType.PARAMETER
        else:
            # This is some other token like a number or string.
            token_type = KatNodeType.VALUE

        attributes["type"] = token_type

        return attributes

    @_item_node_attributes.register(KatReferenceToken)
    def _(self, token, path):
        attributes = {"token": token, "type": KatNodeType.PARAMETER_REFERENCE}
        self._parameter_dependencies.append(path)
        return attributes

    @_item_node_attributes.register(KatKwarg)
    def _(self, kwarg, path):
        return self._fill(
            kwarg.value, path, key_token=kwarg.key, extra_tokens=kwarg.extra
        )

    @_item_node_attributes.register(KatElement)
    def _(self, element, path):
        directive_token = element.directive
        element_type = directive_token.value
        if element_type not in self.spec.elements:
            if element_type in self.spec.commands or element_type in self.spec.analyses:
                # Syntax error was on an command or analysis definition.
                raise KatWrongSyntaxError(directive_token, self.script, self.spec)
            else:
                raise KatUnrecognisedElementError(element, self.script)
        return {
            "token": element.directive,
            "name_token": element.name,
            "type": KatNodeType.ELEMENT,
            "extra_tokens": element.extra,
        }

    @_item_node_attributes.register(KatFunction)
    def _(self, function, path):
        directive_token = function.directive
        if directive_token.value not in self._available_functions:
            raise KatUnrecognisedFunctionError(function, self.script)
        return {
            "token": directive_token,
            "type": KatNodeType.FUNCTION,
            "extra_tokens": function.extra,
        }

    @_item_node_attributes.register(KatGroupedExpression)
    def _(self, group, path):
        return {
            "type": KatNodeType.GROUPED_EXPRESSION,
            "extra_tokens": group.extra,
        }

    @_item_node_attributes.register(KatExpression)
    def _(self, expression, path):
        operator_token = expression.operator
        if operator_token.value not in self.spec.binary_operators:
            raise KatUnrecognisedTypeError(
                f"unknown expression operator '{operator_token.raw_value}'",
                self.script,
                expression.operator,
            )
        return {"type": KatNodeType.EXPRESSION, "token": operator_token}

    @_item_node_attributes.register(KatArray)
    def _(self, array, path):
        return {"type": KatNodeType.ARRAY, "extra_tokens": array.extra}

    @_item_node_attributes.register(KatNumericalArray)
    def _(self, array, path):
        return {"type": KatNodeType.NUMERICAL_ARRAY, "extra_tokens": array.extra}

    def _resolve(self):
        """Resolve references and perform sanity checks on the graph.

        Dependencies due to parameters (e.g. `m1.p1.o`) and parameter references (e.g.
        `&l1.P`) are created by drawing edges to the relevant nodes, transforming the
        parse tree into a graph.

        This additionally checks that:

        - element names are valid and unique,
        - keyword arguments aren't defined in duplicate, and
        - no cycles exist due to dependencies (i.e. if a reference depends on the
          referencing component or its ancestors in any way).

        The `order` attributes of the root edges are overwritten using a topological
        sort to ensure the resulting graph is built in a way that most types of
        dependency can be resolved.
        """
        # Various types of node that we need to validate.
        elements = defaultdict(list)
        singular_directives = defaultdict(list)
        analyses = []

        for node, data in self.graph.root_directive_nodes(data=True):
            node_type = data["type"]
            token = data["token"]
            directive = token.value

            if node_type in KatNodeType.DIRECTIVE_NODES:
                if node_type in KatNodeType.ELEMENT:
                    name_token = data["name_token"]
                    name = name_token.value

                    if name in self.spec.constants:
                        # Disallow.
                        raise KatScriptError(
                            f"constant '{name}' cannot be used as an element name",
                            self.script,
                            [[name_token]],
                        )
                    elif name in self.spec.keywords:
                        LOGGER.warning(
                            f"element name '{name}' (line {name_token.lineno}) is also "
                            f"the name of a keyword, which may lead to confusion"
                        )

                    adapter = self._element_adapter(directive)
                    elements[name].append(node)
                elif node_type in KatNodeType.FUNCTION:
                    adapter = self._function_adapter(directive)
                    if directive in self.spec.analyses:
                        analyses.append(token)

                if adapter.singular:
                    singular_directives[directive].append(node)

                # Check for duplicate keyword arguments.
                dupekvs = duplicates(
                    [
                        self.graph.nodes[node]["key_token"]
                        for node in self.graph.dependent_argument_nodes(node)
                        if "key_token" in self.graph.nodes[node]
                    ],
                    key=lambda token: token.raw_value,
                )
                if dupekvs:
                    keys, dupetokens = zip(*dupekvs)
                    keylist = option_list([f"'{key}'" for key in keys], final_sep="and")
                    msg = ngettext(
                        len(keys),
                        f"duplicate arguments with key {keylist}",
                        f"duplicate arguments with keys {keylist}",
                        sub=False,
                    )
                    error_tokens = [
                        [token] for tokens in dupetokens for token in tokens
                    ]
                    raise KatScriptError(msg, self.script, error_tokens)

        for directive, nodes in singular_directives.items():
            if len(nodes) > 1:
                raise KatScriptError(
                    f"there can only be one '{directive}' directive",
                    self.script,
                    [[self.graph.nodes[node]["token"]] for node in nodes],
                )

        for name, nodes in elements.items():
            if len(nodes) > 1:
                raise KatScriptError(
                    f"multiple elements with name '{name}'",
                    self.script,
                    [[self.graph.nodes[node]["name_token"]] for node in nodes],
                )

        # Check that there isn't more than one root analysis.
        if len(analyses) > 1:
            raise KatScriptError(
                "duplicate analysis trees (combine with 'series' or 'parallel')",
                self.script,
                [[token] for token in analyses],
            )

        # Create dependencies for parameters and parameter references.
        for source_param_path in self._parameter_dependencies:
            source_token = self.graph.nodes[source_param_path]["token"]

            # Targets may not exist in the current script; they may already be in the
            # model prior to parsing.
            try:
                target_directive_path = self.graph.param_target_element_path(
                    source_token.value
                )
            except ValueError:
                LOGGER.debug(
                    f"parameter '{source_token.raw_value}' targetted by "
                    f"'{source_param_path}' does not exist in the script - ignoring"
                )
                continue

            # Add the dependency.
            self.graph.add_edge(
                target_directive_path, source_param_path, type=KatEdgeType.DEPENDENCY,
            )

        # Create graph with just the root directives (use a copy because it may be
        # modified during compilation).
        self.build_graph = self.graph.root_directive_graph()

        def node_build_order(source_graph):
            """Compute node topological order, or throw a cycle error."""
            # Remove self-references, since these will be dealt with by the compiler.
            graph = source_graph.copy()
            for edge in selfloop_edges(source_graph):
                graph.remove_edge(*edge)

            try:
                # Compute topological order, resolving ambiguities in favour of lower
                # line numbers.
                # Convert to list so we know immediately if there are cycles.
                return list(
                    lexicographical_topological_sort(
                        graph, key=lambda node: graph.nodes[node]["token"].lineno
                    )
                )
            except NetworkXUnfeasible:
                # The graph contains at least one cyclic dependency. Work out the
                # cause(s) by finding cycles using the full graph.
                cyclic_param_nodes = set()
                for cycle_nodes in simple_cycles(self.graph):
                    for cycle_node in cycle_nodes:
                        data = self.graph.nodes[cycle_node]
                        if data["type"] not in KatNodeType.DEPENDENT_NODES:
                            # Ignore anything in the cycle that isn't a reference node
                            # (e.g. directives).
                            continue

                        cyclic_param_nodes.add(cycle_node)

                # Grab and sort the cyclic tokens in line order.
                cyclic_parameter_tokens = sorted(
                    [self.graph.nodes[node]["token"] for node in cyclic_param_nodes],
                    key=lambda tok: tok.lineno,
                )

                raise KatCycleError(self.script, cyclic_parameter_tokens)

        # Split the nodes into groups depending on whether they descend from a node with
        # the "build_last" flag.
        first_build_nodes = set(self.build_graph.nodes)
        second_build_nodes = set()
        for node in self.build_graph.nodes():
            adapter = self._directive_adapter(self.graph.nodes[node]["token"].value)
            if not adapter.build_last or node in second_build_nodes:
                # Keep the directive in the first set.
                continue

            # All nodes that descend from (depend on) specified node.
            children = descendants(self.build_graph, node)

            # Move node and descendants from first to second build step.
            first_build_nodes.remove(node)
            first_build_nodes.difference_update(children)
            second_build_nodes.add(node)
            second_build_nodes.update(children)

        first_build_subgraph = self.build_graph.subgraph(first_build_nodes)
        second_build_subgraph = self.build_graph.subgraph(second_build_nodes)
        final_build_order = node_build_order(first_build_subgraph) + node_build_order(
            second_build_subgraph
        )

        # Reorder the root edges topologically.
        for source, target in self.graph.root_argument_edges():
            index = final_build_order.index(source)
            LOGGER.debug(f"{source} has build order {index}")
            self.graph.edges[(source, target)]["order"] = index

    def _build(self, node, model):
        data = self.graph.nodes[node]
        nodetype = data["type"]

        if nodetype in KatNodeType.COMPILER_TERMINAL_NODES:
            # Just use the value.
            value = data["token"].value
        elif nodetype == KatNodeType.CONSTANT:
            # Look up the symbol corresponding to the constant.
            value = self.spec.constants[data["token"].value]
        elif nodetype == KatNodeType.PARAMETER:
            # Copy existing model parameter by value.
            target = data["token"].value
            value = model.reduce_get_attr(target)
            LOGGER.debug(f"parameter {node} targets {target} by value")
        elif nodetype == KatNodeType.PARAMETER_REFERENCE:
            source_directive_path = self.graph.branch_base(node)

            if self.graph.has_edge(source_directive_path, node):
                # This is a reference to another parameter in the same element. Throw an
                # exception that can get caught by the argument compiler. Doing it this
                # way ensures expressions with nested self-references (like `1-&m1.T` in
                # `m m1 1-&m1.T 0`) get set as resolving.
                LOGGER.debug(f"{node} is a self-reference")
                raise KatParameterSelfReferenceException()

            # Copy existing model parameter by reference.
            target = data["token"].value
            try:
                value = model.reduce_get_attr(target).ref
            except FinesseException as e:
                # There was an error getting a reference to the target.
                raise KatParameterCompilationError(
                    e, self.script, node, self.graph
                ) from e
            LOGGER.debug(f"parameter {node} targets {target} by reference")
        elif nodetype == KatNodeType.EXPRESSION:
            operator = self.spec.binary_operators[data["token"].value]
            arguments = self._built_arguments(node, model)
            # Arguments are already in order.
            assert len(arguments) == 2
            lhs, rhs = arguments
            value = operator(lhs, rhs)

            # Eagerly evaluate the expression if its arguments don't depend on anything
            # else.
            if self.graph.is_independent(node):
                value = value.eval()
                LOGGER.debug(
                    f"eagerly evaluated dependencyless expression '{node}' to a "
                    f"{type(value)}"
                )
        elif nodetype == KatNodeType.GROUPED_EXPRESSION:
            arguments = self._built_arguments(node, model)
            assert len(arguments) == 1
            value = arguments[0]
        elif nodetype == KatNodeType.ARRAY:
            value = self._built_arguments(node, model)
        elif nodetype == KatNodeType.NUMERICAL_ARRAY:
            value = np.array(self._built_arguments(node, model))
        elif nodetype == KatNodeType.ELEMENT:
            args, kwargs = self._built_directive_params(node, model)
            adapter = self._element_adapter(data["token"].value)

            # Add name to arguments.
            name = data["name_token"].value
            args = [name, *args]

            try:
                value = adapter.compile(args, kwargs)
            except Exception as e:
                raise KatDirectiveCompilationError(
                    e, self.script, node, adapter, self.graph, self.spec
                ) from e
        elif nodetype == KatNodeType.FUNCTION:
            function_name = data["token"].value

            if function_name in self._expression_functions:
                operator = self._expression_functions[function_name]
                args, kwargs = self._built_directive_params(node, model)

                try:
                    value = operator(*args, **kwargs)
                except TypeError as e:
                    # Replace 'lambda' in the function init error with the function
                    # name.
                    args = list(e.args)
                    args[0] = re.sub(
                        r"(\<lambda\>(\d+)?|\w+)\(\)", f"'{function_name}'", args[0],
                    )
                    raise TypeError(*args)

                # Eagerly evaluate the function if its arguments don't depend on
                # anything else.
                if self.graph.is_independent(node):
                    value = value.eval()
                    LOGGER.debug(
                        f"eagerly evaluated dependencyless function '{node}' to a "
                        f"{type(value)}"
                    )
            else:
                # A directive function.
                adapter = self._function_adapter(data["token"].value)
                args, kwargs = self._built_directive_params(node, model)

                if hasattr(adapter, "compile"):
                    try:
                        value = adapter.compile(args, kwargs)
                    except Exception as e:
                        raise KatDirectiveCompilationError(
                            e, self.script, node, adapter, self.graph, self.spec
                        ) from e
                else:
                    LOGGER.debug(f"function {node} has arguments {args}, {kwargs}")
                    value = args, kwargs
        elif nodetype == KatNodeType.ROOT:
            if model is None:
                LOGGER.debug("creating new model")
                model = Model()
            else:
                LOGGER.debug(f"building into existing model {model!r}")

            for argument_node in self._sorted_arguments(node):
                item = self._build(argument_node, model)
                directive = self.graph.nodes[argument_node]["token"].value
                adapter = self._directive_adapter(directive)

                LOGGER.debug(f"applying {item!r} to {model!r}")
                try:
                    adapter.apply(model, item)
                except Exception as e:
                    raise KatDirectiveCompilationError(
                        e, self.script, argument_node, adapter, self.graph, self.spec
                    ) from e

                # Get all nodes connected to this argument node by a DEPENDENCY edge,
                # where the node is a subbranch of the argument node.
                self_references = self.graph.filter_dependent_nodes(
                    argument_node,
                    key=lambda refnode, _: self.graph.branch_base(refnode)
                    == argument_node,
                )

                if self_references:
                    # Convert to a list because we'll iterate multiple times.
                    self_references = list(self_references)

                    # Delete graph dependencies so that references resolve when we build
                    # again.
                    for target in self_references:
                        LOGGER.debug(f"breaking dependency {argument_node} -> {target}")
                        self.graph.remove_edge(argument_node, target)

                    for self_ref_path in self_references:
                        self_ref_param_path = self.graph.branch_base(
                            self_ref_path, argument_node
                        )

                        # Figure out the signature parameter's name and use it to grab
                        # the corresponding element's parameter. We have to do it this
                        # way because element parameters are unordered, and we might be
                        # dealing with positional arguments.
                        sigparam = argument_signature_parameter(
                            self_ref_param_path, adapter, self.graph
                        )
                        param = next(
                            param
                            for param in item.parameters
                            if param.name == sigparam.name
                        )

                        LOGGER.debug(f"resolving self-referencing {param.full_name}")
                        try:
                            value = self._build(self_ref_param_path, model)
                        except Exception as e:
                            raise KatParameterCompilationError(
                                e, self.script, self_ref_param_path, self.graph
                            ) from e

                        # Get rid of keys.
                        if isinstance(value, dict):
                            assert len(value) == 1
                            _, value = value.popitem()

                        LOGGER.debug(f"setting {param.full_name} to {type(value)}")

                        try:
                            param.value = value
                        except Exception as e:
                            raise KatParameterCompilationError(
                                e, self.script, self_ref_param_path, self.graph
                            ) from e

                    LOGGER.debug(f"finished resolving self-refs for {item!r}")

            value = model
        else:
            raise RuntimeError(f"don't know how to compile parameter '{nodetype}'")

        # Detect kwargs.
        if "key_token" in data:
            value = {data["key_token"].value: value}

        LOGGER.debug(f"compiled {nodetype} {node} to {type(value)}")
        return value

    def _sorted_arguments(self, node):
        return sorted(
            self.graph.dependent_argument_nodes(node),
            key=self.graph.argument_node_order,
        )

    def _built_arguments(self, node, model):
        """Get built dependent arguments of the current node."""
        return [
            self._build(argument_node, model)
            for argument_node in self._sorted_arguments(node)
        ]

    def _built_directive_params(self, node, model):
        """Get built dependent arguments of the current node in Python signature form.

        Self-referencing parameters are caught here too, and set to :class:`.Resolving`;
        these are fully resolved at the end of compilation.
        """
        args = []
        kwargs = {}
        for argument_node in self._sorted_arguments(node):
            try:
                item = self._build(argument_node, model)
            except KatParameterSelfReferenceException:
                item = Resolving()

                # Detect kwargs.
                if key_token := self.graph.nodes[argument_node].get("key_token"):
                    item = {key_token.value: item}

            if isinstance(item, dict):
                kwargs.update(item)
            else:
                args.append(item)
        return args, kwargs

    def _element_adapter(self, element):
        if element := self.spec.elements.get(element):
            return element

        raise ValueError(f"could not find element corresponding to '{element}'")

    def _function_adapter(self, function):
        if command := self.spec.commands.get(function):
            return command
        if analysis := self.spec.analyses.get(function):
            return analysis

        raise ValueError(f"could not find function corresponding to '{function}'")

    def _directive_adapter(self, directive):
        try:
            return self._element_adapter(directive)
        except ValueError:
            try:
                return self._function_adapter(directive)
            except ValueError:
                raise ValueError(
                    f"could not find directive corresponding to '{directive}'"
                )

    def _reraise_parser_error_in_spec_context(self, error):
        """Try to improve parser errors using the :class:`.KatSpec`.

        The parser is unaware of the available elements and functions etc. in the kat
        language spec, because this is only used during compilation. In some cases the
        error messages can be improved with knowledge of the spec, so this method
        identifies such cases.
        """
        if isinstance(error, KatMissingAfterDirective):
            # Use the spec to figure out whether the user might have missed a
            # parenthesis or a name.
            if error.directive.value in self.spec.directives:
                raise KatWrongSyntaxError(error.directive, self.script, self.spec)
            else:
                # Unrecognised directive type. Since that's the earlier error, throw
                # that.
                raise KatScriptError(
                    f"unknown element or function '{error.directive.raw_value}'",
                    self.script,
                    [[error.directive]],
                )

        # Nothing matched, so just reraise.
        raise error


class KatUnrecognisedTypeError(KatScriptError):
    """Error representing an unrecognised type."""

    def __init__(self, message, script, item):
        super().__init__(message, script, [[item]])


class KatUnrecognisedElementError(KatUnrecognisedTypeError):
    """Error representing an unrecognised element."""

    def __init__(self, element, script):
        directive = element.directive
        self.element_type = directive.raw_value
        super().__init__(f"unknown element '{self.element_type}'", script, directive)


class KatUnrecognisedFunctionError(KatUnrecognisedTypeError):
    """Error representing an unrecognised function."""

    def __init__(self, function, script):
        directive = function.directive
        self.function_type = directive.raw_value
        super().__init__(f"unknown function '{self.function_type}'", script, directive)


class KatWrongSyntaxError(KatSyntaxError):
    """Error representing an element, command or analysis that uses the wrong syntax."""

    def __init__(self, directive, script, spec):
        form = syntax(directive.raw_value, spec=spec, optional_as_positional=True)

        super().__init__(
            f"'{directive.raw_value}' should be written in the form '{form}'",
            script,
            directive,
        )


class KatBuildError(KatScriptError):
    """Error during the parser build step."""


class KatCycleError(KatBuildError):
    """Cyclic parameters."""

    def __init__(self, script, cyclic_nodes):
        # Convert list of error tokens to error item lists.
        items = [[item] for item in cyclic_nodes]
        super().__init__("cyclic parameters", script, items)


class KatDirectiveCompilationError(KatBuildError):
    def __init__(self, msg, script, statement_node, adapter, graph, spec):
        data = graph.nodes[statement_node]
        show_item = data["token"]
        error_items = [show_item]
        directive = show_item.value

        if msg:
            # Convert exceptions.
            msg = str(msg)

            # Replace the called Finesse Python API function name, if present, with the
            # directive name.
            msg = re.sub(r"(\<lambda\>|\w+)\(\)", f"'{directive}'", msg,)

            # Handle specific error messages.
            if matches := re.search(r"unexpected keyword argument '(\w+)'", msg):

                def keyfunc(_, data):
                    try:
                        return data["key_token"].value == matches.group(1)
                    except KeyError:
                        return False

                kwarg_node = next(graph.filter_argument_nodes(statement_node, keyfunc))
                # Mark the matching kwarg.
                item = production(kwarg_node, graph)
                # Mark the key.
                error_items = [item.key]

                # Add suggested syntax.
                expected = syntax(directive, spec=spec)
                msg = f"{msg} (expected syntax: {expected})"

        super().__init__(msg, script, [error_items])


class KatParameterCompilationError(KatBuildError):
    def __init__(self, error, script, param_node, graph):
        data = graph.nodes[param_node]
        value_token = data["token"]
        show_items = [value_token]

        # Add the key if it exists.
        try:
            show_items.append(data["key_token"])
        except KeyError:
            pass

        msg = str(error).strip()

        if isinstance(error, ModelAttributeError):
            # Mark only the value.
            show_items = [value_token]
        elif isinstance(error, ModelParameterDefaultValueError):
            # A referenced component doesn't have a default model parameter.
            target = data["token"].value
            msg = f"{msg} (hint: try '&{target}.[some parameter]')"
            # Mark only the value.
            show_items = [value_token]
        elif isinstance(error, ModelParameterSelfReferenceError):
            # Grab the production.
            item = production(param_node, graph)
            # Mark the key and the value.
            show_items = item.sorted_tokens

        super().__init__(msg, script, [show_items])


class KatParameterSelfReferenceException(Exception):
    """Indication that a parameter contains a self-reference that must be resolved
    later."""
