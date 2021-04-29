"""Finesse Sphinx extension.

This provides the `kat:command`, `kat:element` and `kat:analysis` directives and indices
for use in the documentation to document and cross-reference KatScript instructions.

Loosely based on https://www.sphinx-doc.org/en/master/development/tutorials/recipe.html
and https://github.com/click-contrib/sphinx-click/blob/master/sphinx_click/ext.py.

Author: Sean Leavey
"""

import abc
from functools import partial
from collections import defaultdict
from inspect import getabsfile
from docutils import nodes
from docutils.statemachine import string2lines, ViewList
from sphinx import addnodes
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_refnode, nested_parse_with_titles
from numpydoc.docscrape_sphinx import get_doc_object
from finesse.script.spec import KatSpec
from finesse.script.generator import KatSyntaxUnparser

__version__ = "0.7.0"

_SPEC = KatSpec()
_SYNTAXGEN = KatSyntaxUnparser()

_lines = partial(string2lines, tab_width=4, convert_whitespace=True)


def kat_syntax(adapter):
    """Build kat syntax string for `adapter`."""
    return _SYNTAXGEN.syntax(adapter.short_name)


class InstructionDirective(SphinxDirective, metaclass=abc.ABCMeta):
    """A custom Sphinx directive that describes a KatScript instruction."""

    description = "Instruction"
    has_content = True
    required_arguments = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        directive = self.arguments[0]
        try:
            self.adapter = _SPEC.directives[directive]
        except KeyError:
            raise ValueError(
                f"directive {directive} doesn't exist in KatScript language spec"
            )

    @property
    def doc_obj(self):
        """The numpydoc object."""
        return get_doc_object(self.adapter.docobj_type)

    def _description_slug(self):
        """Description type, usable as HTML attribute."""
        return nodes.fully_normalize_name(self.description)

    def _alias_slug(self, alias):
        return nodes.make_id(f"kat-{self._description_slug()}-{alias}")

    def _format_summary(self):
        yield from _lines(" ".join(self.doc_obj["Summary"]))
        yield ""

    def _format_syntax(self):
        yield f":Syntax: ``{kat_syntax(self.adapter)}``"
        yield ""

    def _format_param_text(self, name, params):
        yield f":{name}:"
        yield ""

        for pnames, pdoc in params:
            pnames = [f"``{pname.strip()}``" for pname in pnames.split(",")]
            # Indent the line so we get an inner definition list.
            line = f"  {', '.join(pnames)}"

            if pdoc:
                line += f": {pdoc}"

            yield line
            yield ""

        yield ""

    def run(self):
        """Main entry function, called by docutils upon encountering the directive.

        This generates the signature line (directive aliases), description, parameter
        lists and any other content specified in the restructuredText document.
        """
        try:
            source = getabsfile(self.adapter.call_signature_type)
        except TypeError:
            # This may be a Cythonised target. Use the string name instead.
            source = self.adapter.call_signature_type.__name__

        kat = self.env.get_domain("kat")

        if ":" not in self.name:
            raise ValueError(
                f"incorrect name format '{self.name}'; must be of the form 'kat:thing'"
            )

        self.domain, self.objtype = self.name.split(":", 1)

        # Index entry.
        indexnode = addnodes.index(entries=[])

        node = addnodes.desc()
        node.document = self.state.document
        node["domain"] = self.domain
        node["objtype"] = self.objtype
        node["noindex"] = noindex = "noindex" in self.options
        node["classes"].append(self.domain)
        node["classes"].append(node["objtype"])

        # Add each alias to the signature.
        signode = addnodes.desc_signature("", "", is_multiline=True)
        self.set_source_info(signode)
        node.append(signode)

        for i, alias in enumerate(self.adapter.aliases):
            is_primary = alias == self.adapter.full_name

            # All signatures have anchors due to the signode["ids"] line below, but
            # add_permalink shows a "#" next to the signature that users can copy.
            sigline = addnodes.desc_signature_line("", add_permalink=is_primary)
            sigline += addnodes.desc_name(text=alias)
            signode += sigline

            # Map index entry.
            if not noindex:
                anchor = self._alias_slug(alias)

                # Register an anchor for this alias.
                signode["ids"].append(anchor)

                kat.add_instruction(anchor, self, alias)

                if "noindexentry" not in self.options:
                    indextext = f"{alias} (KatScript {self.description})"
                    indexnode["entries"].append(("single", indextext, anchor, "", None))

        # The parameters.
        required_params = []
        optional_params = []

        for param_name, param_type, param_doc in self.doc_obj["Parameters"]:
            # Join together lines of pdoc.
            if param_doc:
                param_doc = " ".join(param_doc)
            else:
                param_doc = None

            param = param_name, param_doc

            if "optional" in param_type:
                optional_params.append(param)
            else:
                required_params.append(param)

        contentnode = addnodes.desc_content()
        self.set_source_info(contentnode)
        node.append(contentnode)

        content = ViewList()

        # The summary.
        for line in self._format_summary():
            content.append(line, source)
        content.append("", source)

        # The syntax.
        for line in self._format_syntax():
            content.append(line, source)
        content.append("", source)

        # Add parameters.
        if required_params:
            for line in self._format_param_text("Required", required_params):
                content.append(line, source)
        if optional_params:
            for line in self._format_param_text("Optional", optional_params):
                content.append(line, source)

        # Any extra content specified in the rST file.
        for line in self.content:
            content.append(line, source)
        content.append("", source)

        nested_parse_with_titles(self.state, content, contentnode)

        return [indexnode, node]


class CommandDirective(InstructionDirective):
    """A custom directive that describes a kat script command."""

    description = "Command"


class ElementDirective(InstructionDirective):
    """A custom directive that describes a kat script element."""

    description = "Element"


class AnalysisDirective(InstructionDirective):
    """A custom directive that describes a kat script analysis."""

    description = "Analysis"


class KatIndex(Index, metaclass=abc.ABCMeta):
    """A custom index that creates an instruction matrix."""

    index_type = None

    def generate(self, docnames=None):
        content = defaultdict(list)

        # Sort the list of instructions in alphabetical order.
        instructions = self.domain.get_objects()
        instructions = sorted(instructions, key=lambda instruction: instruction[0])

        # Generate the expected output, shown below, from the above using the first
        # letter of the recipe as a key to group thing.
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for name, dispname, typ, docname, anchor, _ in instructions:
            if typ != self.index_type:
                continue

            display_name = self.format_display_name(dispname)
            description = typ

            # The key is the index (in this case, the first character).
            content[display_name[0].lower()].append(
                (display_name, 0, docname, anchor, docname, "", description)
            )

        # Convert the dict to the sorted list of tuples expected.
        content = sorted(content.items())

        return content, True

    def format_display_name(self, name):
        return name


class CommandIndex(KatIndex):
    """A custom index that creates a command matrix."""

    name = "commandindex"
    localname = "Command Index"
    shortname = "Command"
    index_type = "Command"


class ElementIndex(KatIndex):
    """A custom index that creates an element matrix."""

    name = "elementindex"
    localname = "Element Index"
    shortname = "Element"
    index_type = "Element"


class AnalysisIndex(KatIndex):
    """A custom index that creates an analysis matrix."""

    name = "analysisindex"
    localname = "Analysis Index"
    shortname = "Analysis"
    index_type = "Analysis"


class KatDomain(Domain):
    name = "kat"
    label = "Kat Domain"
    roles = {
        "command": XRefRole(),
        "element": XRefRole(),
        "analysis": XRefRole(),
    }
    directives = {
        "command": CommandDirective,
        "element": ElementDirective,
        "analysis": AnalysisDirective,
    }
    indices = {
        CommandIndex,
        ElementIndex,
        AnalysisIndex,
    }
    initial_data = {
        "instructions": [],  # Object list.
    }

    def get_full_qualified_name(self, node):
        return "{}.{}".format("instruction", node.arguments[0])

    def get_objects(self):
        yield from self.data["instructions"]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        # Match the specified reference to an alias of the available kat script
        # directives.
        if typ == "command":
            match = [
                (docname, anchor)
                for name, sig, otyp, docname, anchor, prio in self.get_objects()
                if (otyp == "Command" and target in _SPEC.commands[sig].aliases)
            ]
        elif typ == "element":
            match = [
                (docname, anchor)
                for name, sig, otyp, docname, anchor, prio in self.get_objects()
                if (otyp == "Element" and target in _SPEC.elements[sig].aliases)
            ]
        elif typ == "analysis":
            match = [
                (docname, anchor)
                for name, sig, otyp, docname, anchor, prio in self.get_objects()
                if (otyp == "Analysis" and target in _SPEC.analyses[sig].aliases)
            ]
        else:
            match = []

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ, contnode, targ)
        else:
            print(f"Did not find kat script instruction for xref '{target}'")
            return None

    def add_instruction(self, anchor, instruction, signature):
        """Add a new instruction to the domain."""
        name = "{}.{}".format("instruction", signature)

        # name, dispname, type, docname, anchor, priority
        self.data["instructions"].append(
            (name, signature, instruction.description, self.env.docname, anchor, 0)
        )


def setup(app):
    app.add_domain(KatDomain)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
