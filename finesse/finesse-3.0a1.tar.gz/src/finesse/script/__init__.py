"""Parsing and unparsing of Finesse kat files and models."""

from ..utilities import opened_file


def parse(text, model=None, spec=None):
    """Parse kat script into a model.

    Parameters
    ----------
    text : str
        The kat script to parse.

    model : :class:`.Model`, optional
        The Finesse model to add the parsed objects to. Defaults to a new, empty model.

    spec : :class:`.spec.BaseSpec`, optional
        The language specification to use. Defaults to :class:`.spec.KatSpec`.

    Returns
    -------
    :class:`.Model`
        The parsed model.
    """
    from .compiler import KatCompiler

    compiler = KatCompiler(spec=spec)
    return compiler.compile(text, model=model)


def parse_file(path, model=None, spec=None):
    """Parse kat script from a file into a model.

    Parameters
    ----------
    path : str or :py:class:`io.FileIO`
        The path or file object to read kat script from. If an open file object is
        passed, it will be read from and left open. If a path is passed, it will be
        opened, read from, then closed.

    model : :class:`.Model`, optional
        The Finesse model to add the parsed objects to. Defaults to a new, empty model.

    spec : :class:`.spec.BaseSpec`, optional
        The language specification to use. Defaults to :class:`.spec.KatSpec`.

    Returns
    -------
    :class:`.Model`
        The parsed model.
    """
    from .compiler import KatCompiler

    compiler = KatCompiler(spec=spec)
    with opened_file(path, "r") as fobj:
        return compiler.compile_file(fobj, model=model)


def parse_legacy(text, model=None, ignored_blocks=None):
    """Parse kat script into a model.

    Parameters
    ----------
    text : str
        The kat script to parse.

    model : :class:`.Model`
        The Finesse model to add the parsed objects to.

    ignored_blocks : list, optional
        A list of names of ``FTBLOCK`` sections in the kat code to leave out of the
        model; defaults to empty list.

    Returns
    -------
    :class:`.Model`
        The parsed model.

    Raises
    ------
    NotImplementedError
        If `model` contains any non-default elements. Parsing into existing models is
        unsupported.
    """
    from .legacy import KatParser

    if model:
        # Newly-created models contain an fsig, so we need to account for that
        if len(model.elements) > 1:
            raise NotImplementedError(
                "Legacy parsing of extra commands with an existing model is "
                "unsupported. Please switch to the new syntax, or only call "
                "'parse_legacy' on a complete kat file."
            )
    parser = KatParser()
    return parser.parse(text, model=model, ignored_blocks=ignored_blocks)


def parse_legacy_file(path, model=None, ignored_blocks=None):
    """Parse kat script from a file into a model.

    Parameters
    ----------
    path : str or :py:class:`io.FileIO`
        The path or file object to read kat script from. If an open file object is
        passed, it will be read from and left open. If a path is passed, it will be
        opened, read from, then closed.

    model : :class:`.Model`
        The Finesse model to add the parsed objects to.

    ignored_blocks : list, optional
        A list of names of ``FTBLOCK`` sections in the kat code to leave out of the
        model; defaults to empty list.

    Returns
    -------
    :class:`.Model`
        The parsed model.

    Raises
    ------
    NotImplementedError
        If `model` contains any non-default elements. Parsing into existing models is
        unsupported.
    """
    from .legacy import KatParser

    if model:
        # Newly-created models contain an fsig, so we need to account for that
        if len(model.elements) > 1:
            raise NotImplementedError(
                "Legacy parsing of extra commands with an existing model is "
                "unsupported. Please switch to the new syntax, or only call "
                "'parse_legacy' on a complete kat file."
            )

    parser = KatParser()
    with opened_file(path, "r") as fobj:
        return parser.parse(fobj.read(), model=model, ignored_blocks=ignored_blocks)


def unparse(model):
    """Serialise a model to kat script.

    Parameters
    ----------
    model : :class:`.Model`
        The Finesse model to generate kat script for.

    Returns
    -------
    str
        The generated kat script.
    """
    from .generator import KatUnbuilder

    unbuilder = KatUnbuilder()
    return unbuilder.unbuild(model)


def unparse_file(path, model):
    """Serialise a model to kat script in a file.

    Parameters
    ----------
    path : str
        The kat file path to parse.

    model : :class:`.Model`
        The Finesse model to generate kat script for.

    Returns
    -------
    str
        The generated kat script.
    """
    from .generator import KatUnbuilder

    unbuilder = KatUnbuilder()
    with opened_file(path, "w") as fobj:
        return unbuilder.unbuild_file(fobj, model)


def syntax(directive, spec=None, **kwargs):
    """Get the syntax for `directive`.

    Parameters
    ----------
    directive : str
        The directive to retrieve syntax for.

    spec : :class:`.KatSpec`, optional
        The kat script specification to use. Defaults to :class:`.KatSpec`.

    Other Parameters
    ----------------
    kwargs : dict, optional
        Keyword arguments supported by :meth:`.KatSyntaxUnparser.syntax`.

    Returns
    -------
    str
        The syntax for `directive`.
    """
    from .generator import KatSyntaxUnparser

    unparser = KatSyntaxUnparser(spec=spec)
    return unparser.syntax(directive, **kwargs)


__all__ = (
    "KatParserError",
    "KatReferenceError",
    "parse",
    "parse_file",
    "parse_legacy",
    "parse_legacy_file",
    "unparse",
    "unparse_file",
    "syntax",
)
