"""Kat script generator."""

import logging
from io import StringIO
from functools import singledispatchmethod
from collections.abc import Iterable

import numpy as np

from ..model import Model
from ..element import ModelElement
from ..parameter import Parameter, ParameterRef
from ..symbols import OPERATORS, FUNCTIONS, Operation, Constant
from ..components import Port, Node
from ..analysis.actions import Action
from .containers import (
    KatToken,
    KatNumberToken,
    KatStringToken,
    KatWhitespaceToken,
    KatNoneToken,
    KatScript,
    KatElement,
    KatFunction,
    KatKwarg,
    KatExpression,
    KatGroupedExpression,
    KatArray,
)
from .tokens import LITERALS
from .spec import KatSpec
from .graph import KatNodeType, KatEdgeType, KatGraph
from .util import scriptsorted, merge_attributes


LOGGER = logging.getLogger(__name__)


class ElementContainer:
    """Container for top level model elements, used by the generator."""

    def __init__(self, element):
        super().__init__()
        self.element = element

    def __repr__(self):
        return f"ElementContainer({repr(self.element)})"


class CommandContainer:
    """Container for top level commands, used by the generator."""

    def __init__(self, adapter, *args, **kwargs):
        super().__init__()
        self.adapter = adapter
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f"CommandContainer({self.adapter.full_name})"


class KatUnbuilder:
    """Model to kat script."""

    # Model element types not dumped.
    IGNORED_ELEMENTS = [
        "Fsig",  # Models always contain an Fsig. The actual value is dumped as a command.
    ]

    # FIXME: move to KatSpec.
    UNARY_OPERATORS = {
        "pos": "+",
        "neg": "-",
    }

    # Reverse dicts for various types.
    LITERAL_MAP = dict((value, key) for key, value in LITERALS.items())

    def __init__(self, spec=None):
        if spec is None:
            spec = KatSpec()

        self.spec = spec
        self.graph = None
        self._lineno = None
        self._index = None

    def unbuild(self, item):
        fobj = StringIO()
        self.unbuild_file(fobj, item)
        fobj.seek(0)
        return fobj.read()

    def unbuild_file(self, fobj, item):
        self.graph = KatGraph()
        self._lineno = 1
        self._index = 1
        self._fill(item, self.graph.ROOT_NODE_NAME)

        unfiller = KatUnfiller()
        unfiller.unfill_file(fobj, self.graph.ROOT_NODE_NAME, self.graph)

    def _fill(self, value, path, **attributes):
        LOGGER.debug(f"filling {value!r} ({type(value)}) into graph at {path}")

        assert path not in self.graph

        attributes = merge_attributes(
            attributes, self._item_node_attributes(value, path)
        )
        self.graph.add_node(path, **attributes)

        return attributes

    @singledispatchmethod
    def _item_node_attributes(self, item, path):
        """Get the attributes for `item` to be added to the corresponding node."""
        raise NotImplementedError(
            f"don't know how to handle an item with type '{item.__class__.__name__}'"
        )

    @_item_node_attributes.register(Model)
    def _(self, model, path):
        extra_tokens = []
        order = 0

        # Components, detectors, etc.
        for element in model.elements.values():
            element_type = element.__class__.__name__
            if element_type in self.IGNORED_ELEMENTS:
                LOGGER.debug(f"skipping filling of ignored element type {element_type}")
                continue

            if order > 0:
                extra_tokens.append(self._newline_token())

            # Define a proxy so we can differentiate model element definitions from
            # references to model elements.
            proxy = ElementContainer(element)
            element_path = self.graph.item_node_name(order, path)
            if self._fill(proxy, element_path):
                self.graph.add_edge(
                    element_path, path, type=KatEdgeType.ARGUMENT, order=order
                )

            order += 1

        # Commands.
        for adapter in self.spec.commands.values():
            command_params = adapter.get(model)

            if command_params is None:
                # Nothing to dump.
                continue

            if adapter.singular:
                # The getter should return a single args, kwargs tuple.
                command_params = [command_params]

            # There are command(s) to dump for this adapter.
            for args, kwargs in command_params:
                if order > 0:
                    extra_tokens.append(self._newline_token())

                proxy = CommandContainer(adapter, *args, **kwargs)
                command_path = self.graph.item_node_name(order, path)
                if self._fill(proxy, command_path):
                    self.graph.add_edge(
                        command_path, path, type=KatEdgeType.ARGUMENT, order=order
                    )

                order += 1

        # Analysis.
        if model.analysis:
            if order > 0:
                extra_tokens.append(self._newline_token())

            analysis_path = self.graph.item_node_name(order, path)
            if self._fill(model.analysis, analysis_path):
                self.graph.add_edge(
                    analysis_path, path, type=KatEdgeType.ARGUMENT, order=order
                )

            order += 1

        return {"type": KatNodeType.ROOT, "extra_tokens": extra_tokens}

    @_item_node_attributes.register(ElementContainer)
    def _(self, proxy, path):
        """Model element definitions."""
        element = proxy.element
        adapter = self.spec.adapter_by_setter(type(element))
        params = adapter.get(element)
        if not params:
            return

        name, args, kwargs = params

        extra_tokens = []
        token = self._name_token(adapter.full_name)
        extra_tokens.append(self._space_token())
        name_token = self._name_token(name)
        extra_tokens.append(self._space_token())
        extra_tokens.extend(self._fill_element_args(args, kwargs, path))

        return {
            "token": token,
            "name_token": name_token,
            "type": KatNodeType.ELEMENT,
            "extra_tokens": extra_tokens,
        }

    @_item_node_attributes.register(CommandContainer)
    def _(self, proxy, path):
        """Command definitions."""
        return self._fill_function(proxy.adapter, proxy.args, proxy.kwargs, path)

    @_item_node_attributes.register(Action)
    def _(self, action, path):
        adapter = self.spec.adapter_by_setter(type(action))
        params = adapter.get(action)
        if not params:
            return
        return self._fill_function(adapter, *params, path)

    @_item_node_attributes.register(Parameter)
    def _(self, parameter, path):
        return self._fill(parameter.value, path)

    @_item_node_attributes.register(ParameterRef)
    def _(self, reference, path):
        value = self._name_token(f"&{reference.name}")
        return {"token": value, "type": KatNodeType.PARAMETER_REFERENCE}

    @_item_node_attributes.register(ModelElement)
    def _(self, value, path):
        """Reference to a model element.

        Model element definitions are matched as :class:`.ElementContainer`.
        """
        return {"token": self._name_token(value.name), "type": KatNodeType.VALUE}

    @_item_node_attributes.register(Port)
    @_item_node_attributes.register(Node)
    def _(self, value, path):
        return {"token": self._name_token(value.full_name), "type": KatNodeType.VALUE}

    @_item_node_attributes.register(int)
    @_item_node_attributes.register(np.integer)
    def _(self, value, path):
        value = int(value)
        if value < 0:
            return self._fill(FUNCTIONS["neg"](abs(value)), path)
        return {"token": self._number_token(value), "type": KatNodeType.VALUE}

    @_item_node_attributes.register(float)
    @_item_node_attributes.register(np.floating)
    def _(self, value, path):
        value = float(value)
        if value < 0:
            return self._fill(FUNCTIONS["neg"](abs(value)), path)
        return {"token": self._number_token(value), "type": KatNodeType.VALUE}

    @_item_node_attributes.register(complex)
    def _(self, value, path):
        real = value.real
        imag = value.imag

        if not real:
            cplx = complex(f"{abs(imag)}j")
            if imag < 0:
                return self._fill(FUNCTIONS["neg"](cplx), path)
            return {"token": self._number_token(cplx), "type": KatNodeType.VALUE}
        elif not imag:
            if real < 0:
                return self._fill(FUNCTIONS["neg"](abs(real)), path)
            return {"token": self._number_token(real), "type": KatNodeType.VALUE}
        else:
            if real < 0:
                real = FUNCTIONS["neg"](abs(real))
            binop = OPERATORS["__add__"] if imag >= 0 else OPERATORS["__sub__"]
            return self._fill(binop(real, self._number_token(f"{abs(imag)}j")), path)

    @_item_node_attributes.register(str)
    def _(self, value, path):
        if value in self.spec.keywords:
            value = self._name_token(value)
        else:
            value = self._string_token(value)
        return {"token": value, "type": KatNodeType.VALUE}

    @_item_node_attributes.register(bool)
    @_item_node_attributes.register(np.bool_)
    def _(self, value, path):
        return {
            "token": self._name_token("true" if value else "false"),
            "type": KatNodeType.VALUE,
        }

    @_item_node_attributes.register(type(None))
    def _(self, value, path):
        return {"token": self._none_token(), "type": KatNodeType.VALUE}

    @_item_node_attributes.register(Iterable)
    def _(self, array, path):
        extra_tokens = []
        extra_tokens.append(self._literal_token("["))
        extra_tokens.extend(self._fill_function_args(array, {}, path))
        extra_tokens.append(self._literal_token("]"))
        return {"type": KatNodeType.ARRAY, "extra_tokens": extra_tokens}

    @_item_node_attributes.register(Constant)
    def _(self, constant, path):
        return self._fill(constant.eval(), path)

    @_item_node_attributes.register(Operation)
    def _(self, operation, path):
        op = operation.name
        extra_tokens = []

        def make_arg(argument, order):
            argument_path = self.graph.item_node_name(order, path)
            self._fill(argument, argument_path)
            self.graph.add_edge(
                argument_path, path, type=KatEdgeType.ARGUMENT, order=order
            )

        if op in self.spec.binary_operators:
            assert len(operation.args) == 2
            extra_tokens.append(self._literal_token("("))
            make_arg(operation.args[0], 0)
            token = self._literal_token(operation.name)
            nodetype = KatNodeType.EXPRESSION
            make_arg(operation.args[1], 1)
            extra_tokens.append(self._literal_token(")"))
        elif unary_op := self.UNARY_OPERATORS.get(op):
            token = self._literal_token(unary_op)
            nodetype = KatNodeType.FUNCTION
            make_arg(operation.args[0], 0)
        elif op in self.spec.expression_functions:
            token = self._name_token(operation.name)
            nodetype = KatNodeType.FUNCTION
            extra_tokens.append(self._literal_token("("))
            for order, argument in enumerate(operation.args):
                if order > 0:
                    extra_tokens.append(self._literal_token(","))
                    extra_tokens.append(self._space_token())
                make_arg(argument, order)
            extra_tokens.append(self._literal_token(")"))
        else:
            raise NotImplementedError(f"don't know how to handle operation '{op}'")

        return {"token": token, "type": nodetype, "extra_tokens": extra_tokens}

    def _token(self, type, raw_value, tokcls=None):
        if tokcls is None:
            tokcls = KatToken

        start_index = self._index
        self._index += len(raw_value)
        stop_index = self._index

        return tokcls(self._lineno, start_index, stop_index, type, raw_value)

    def _name_token(self, value):
        return self._token("NAME", value)

    def _space_token(self, length=1):
        return self._token("WHITESPACE", " " * length, tokcls=KatWhitespaceToken)

    def _number_token(self, value):
        return self._token("NUMBER", str(value), tokcls=KatNumberToken)

    def _string_token(self, value):
        return self._token("STRING", repr(value), tokcls=KatStringToken)

    def _none_token(self):
        return self._token("NONE", "none", tokcls=KatNoneToken)

    def _literal_token(self, literal):
        return self._token(self.LITERAL_MAP[literal], literal)

    def _newline_token(self, count=1):
        self._lineno += count
        self._index = 1
        return self._token("NEWLINE", "\n" * count)

    def _fill_arg(self, value, order, path, **attributes):
        argument_path = self.graph.item_node_name(order, path)
        self._fill(value, argument_path, **attributes)
        self.graph.add_edge(argument_path, path, type=KatEdgeType.ARGUMENT, order=order)

    def _fill_args(self, args, kwargs, path, delimfunc):
        extra_tokens = []

        # Can't use enumerate because we loop twice.
        order = 0

        for value in args:
            if order > 0:
                extra_tokens.extend(delimfunc())
            self._fill_arg(value, order, path)
            order += 1

        for key, value in kwargs.items():
            if order > 0:
                extra_tokens.extend(delimfunc())
            key_token = self._name_token(key)
            equals_token = self._literal_token("=")
            self._fill_arg(
                value, order, path, key_token=key_token, extra_tokens=[equals_token]
            )
            order += 1

        return extra_tokens

    def _fill_element_args(self, args, kwargs, path):
        def delim():
            return [self._space_token()]

        return self._fill_args(args, kwargs, path, delim)

    def _fill_function_args(self, args, kwargs, path):
        def delim():
            return [self._literal_token(","), self._space_token()]

        return self._fill_args(args, kwargs, path, delim)

    def _fill_function(self, adapter, args, kwargs, path):
        extra_tokens = []
        token = self._name_token(adapter.full_name)
        extra_tokens.append(self._literal_token("("))
        extra_tokens.extend(self._fill_function_args(args, kwargs, path))
        extra_tokens.append(self._literal_token(")"))

        return {
            "token": token,
            "type": KatNodeType.FUNCTION,
            "extra_tokens": extra_tokens,
        }


class KatUnfiller:
    """KatGraph to kat script."""

    def unfill(self, node, graph):
        fobj = StringIO()
        self.unfill_file(fobj, node, graph)
        fobj.seek(0)
        return fobj.read()

    def unfill_file(self, fobj, node, graph):
        production = self.production(node, graph)
        unparser = KatUnparser()
        unparser.unparse_file(fobj, production)

    def production(self, node, graph):
        data = graph.nodes[node]
        nodetype = data["type"]

        # Create any dependent arguments.
        arguments = scriptsorted(
            [
                self.production(argument_node, graph)
                for argument_node in graph.dependent_argument_nodes(node)
            ]
        )
        # Grab any extra tokens.
        extra = scriptsorted(data.get("extra_tokens", []))

        # Detect kwargs.
        kwarg_extra = None
        if "key_token" in data:
            # Extract the equals token out of extra.
            equals = next(filter(lambda item: item.type == "EQUALS", extra))
            extra.remove(equals)
            kwarg_extra = [equals]

        if nodetype in KatNodeType.GENERATOR_TERMINAL_NODES:
            value = data["token"]
        elif nodetype == KatNodeType.ROOT:
            value = KatScript(arguments=arguments, extra=extra)
        elif nodetype == KatNodeType.ELEMENT:
            value = KatElement(
                directive=data["token"],
                arguments=arguments,
                extra=extra,
                name=data.get("name_token"),
            )
        elif nodetype == KatNodeType.FUNCTION:
            value = KatFunction(
                directive=data["token"], arguments=arguments, extra=extra
            )
        elif nodetype == KatNodeType.GROUPED_EXPRESSION:
            value = KatGroupedExpression(arguments=arguments, extra=extra)
        elif nodetype == KatNodeType.EXPRESSION:
            value = KatExpression(
                operator=data["token"], arguments=arguments, extra=extra
            )
        elif nodetype == KatNodeType.ARRAY:
            value = KatArray(arguments=arguments, extra=extra)
        else:
            raise RuntimeError(f"don't know how to generate '{nodetype}'")

        # Detect kwargs.
        if kwarg_extra:
            value = KatKwarg(key=data["key_token"], value=value, extra=kwarg_extra)

        return value


class KatUnparser:
    """TokenContainer to kat script."""

    def unparse(self, container):
        fobj = StringIO()
        self.unparse_file(fobj, container)
        fobj.seek(0)
        return fobj.read()

    def unparse_file(self, fobj, container):
        untokenizer = KatUntokenizer()
        untokenizer.untokenize_file(fobj, container.sorted_tokens)


class KatUntokenizer:
    """Token to kat script."""

    def untokenize(self, tokens):
        fobj = StringIO()
        self.untokenize_file(fobj, tokens)
        fobj.seek(0)
        return fobj.read()

    def untokenize_file(self, fobj, tokens):
        for token in tokens:
            fobj.write(token.raw_value)


class KatSyntaxUnparser:
    """Unparser for kat script meta-language."""

    def __init__(self, spec=None):
        self.unbuilder = KatUnbuilder(spec=spec)

    def syntax(self, directive, optional_as_positional=False):
        """Get syntax for `directive`.

        Parameters
        ----------
        directive : str
            The directive to generate syntax for.

        optional_as_positional : bool, optional
            Show optional parameters in positional form rather than keyword form.
            Defaults to False.

        Returns
        -------
        str
            The syntax for `directive`.

        Raises
        ------
        ValueError
            If `directive` is not recognised as a valid KatScript directive in `spec`.
        """
        from finesse.script.adapter import (
            ElementAdapter,
            CommandAdapter,
            AnalysisAdapter,
        )

        try:
            adapter = self.spec.directives[directive]
        except KeyError as e:
            raise ValueError(f"directive '{directive}' not recognised") from e

        args, has_var_positional, has_var_keyword = self._arguments(
            adapter, optional_as_positional
        )

        if isinstance(adapter, ElementAdapter):
            if has_var_positional:
                args.append("{arg1{ arg2{ ...}}}")
            if has_var_keyword:
                args.append("{kwarg1=value{ kwarg2=value{ ...}}}")

            return f"{directive} {' '.join(arg for arg in args)}"
        elif isinstance(adapter, (CommandAdapter, AnalysisAdapter)):
            if has_var_positional:
                args.append("{arg1{, arg2{, ...}}}")
            if has_var_keyword:
                args.append("{kwarg1=value{, kwarg2=value{, ...}}}")

            return f"{directive}({', '.join(arg for arg in args)})"
        else:
            raise ValueError(f"unrecognised adapter type '{type(adapter)}'")

    def _arguments(self, adapter, optional_as_positional):
        from inspect import Parameter as SigParameter

        args = []
        has_var_positional = False
        has_var_keyword = False

        for arg, parameter in adapter.call_signature().parameters.items():
            if parameter.kind == SigParameter.VAR_POSITIONAL:
                # This is the *args variable argument.
                has_var_positional = True
            elif parameter.kind == SigParameter.VAR_KEYWORD:
                # This is the **kwargs variable argument.
                has_var_keyword = True
            else:
                # Generate real kat script for the default value.
                pos_value = arg

                if parameter.default is parameter.empty:
                    # The parameter does not have a default.
                    key_value = arg
                else:
                    default = self.unbuilder.unbuild(parameter.default)
                    key_value = f"{arg}={default}"

                if parameter.kind == SigParameter.POSITIONAL_ONLY:
                    args.append(pos_value)
                elif parameter.kind == SigParameter.KEYWORD_ONLY:
                    args.append(key_value)
                else:
                    if optional_as_positional:
                        args.append(pos_value)
                    else:
                        args.append(key_value)

        return args, has_var_positional, has_var_keyword

    @property
    def spec(self):
        return self.unbuilder.spec
