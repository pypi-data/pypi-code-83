"""Miscellaneous utility functions for any part of Finesse."""

import copy
import logging
import functools
import re
from itertools import tee
from contextlib import contextmanager
from functools import partial

import numpy as np


def calltracker(func):
    """Decorator used for keeping track of whether the current state is inside the
    decorated function or not.

    Sets an attribute `has_been_called` on the function which gets switched on when the
    function is being executed and switched off after the function has returned. This
    allows you to query ``func.has_been_called`` for determining whether the code being
    executed has been called from within `func`.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        out = func(*args, **kwargs)
        wrapper.has_been_called = False

        return out

    wrapper.has_been_called = False
    return wrapper


def valid_name(name):
    """Validate the specified name."""
    return re.compile("^[a-zA-Z_][a-zA-Z0-9_]*$").match(name)


def check_name(name):
    """Checks the validity of a component or node name.

    A name is valid if it contains only alphanumeric characters and underscores, and is
    not empty.

    Parameters
    ----------
    name : str
        The name to check.

    Returns
    -------
    name : str
        The name passed to this function if valid.

    Raises
    ------
    ValueError
        If `name` contains non-alphanumeric / underscore characters.
    """
    if not valid_name(name):
        raise ValueError(
            "Name `{}` is not valid. Alphanumeric and underscores only".format(name)
        )
    return name


def pairwise(iterable):
    """Iterates through each pair in a iterable.

    Parameters
    ----------
    iterable : :py:class:`collections.abc.Iterable`
        An iterable object.

    Returns
    -------
    zip
        A zip object whose `.next()` method returns a tuple where the i-th
        element comes from the i-th iterable argument.
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def find(x, value):
    """Finds `value` in the list `x` and returns its index, returning `None` if `value`
    is not in the list."""
    try:
        return x.index(value)
    except ValueError:
        return None


def find_nearest(x, value, index=False):
    idx = np.argmin(np.abs(x - value))
    if index:
        return idx
    return x[idx]


def is_iterable(obj):
    """Reliable check for whether an object is iterable.

    Note that strings are treated as non-iterable objects
    when performing this check. This will only return true
    for iterable non-str objects.

    Returns
    -------
    flag : bool
        True if `obj` is iterable, False otherwise.
    """
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return not isinstance(obj, str)


@contextmanager
def changed_params(subs: dict):
    r"""Temporarily change model parameters within a context.

    This is a convenience function for providing a pattern of
    changing parameters temporarily, inside a context, without
    needing to make deep-copies of a :class:`.Model`. Usage of
    this function should be confined to ``with`` contexts.

    Parameters
    ----------
    subs : dict
        Dictionary of temporary parameter subsitutions. Expects a dict
        of :class:`.Parameter` to float value mappings.

    Examples
    --------
    In this example a simple Fabry-Perot cavity is created and
    this function is used to inspect how some cavity properties
    vary when temporarily changing parameters.

    .. jupyter-execute::

        import finesse
        import finesse.components as components

        from finesse.utilities import changed_params

        IFO = finesse.Model()
        IFO.chain(
            components.Laser("L0"),
            components.Mirror("ITM", Rc=-10),
            components.Space("CAV", L=1),
            components.Mirror("ETM", Rc=10),
        )
        IFO.add(components.Cavity("FP", IFO.ITM.p2))

        print(f"Initial FP.g = {IFO.FP.g}")
        print(f"Initial FP.gouy = {IFO.FP.gouy}\n")

        # Temporarily change ITM.Rcx to -15 m and ETM.Rcy to 9 m
        with changed_params({IFO.ITM.Rcx: -15, IFO.ETM.Rcy: 9}):
            print(f"Temporary FP.g = {IFO.FP.g}")
            print(f"Temporary FP.gouy = {IFO.FP.gouy}\n")

        # Check that params have been reset by looking at cavity again
        print(f"Final FP.g = {IFO.FP.g}")
        print(f"Final FP.gouy = {IFO.FP.gouy}")
    """
    # Get the current values of the parameters being changed
    initial_values = {p: copy.copy(p.value) for p in subs}
    # Set the parameters to their temp values
    for p, tval in subs.items():
        p.value = tval

    yield

    # Reset the values on exit
    for p in subs:
        p.value = initial_values[p]


@contextmanager
def opened_file(fobj, mode):
    """Get an open file regardless of whether a string or an already open file is
    passed.

    Parameters
    ----------
    fobj : str or file-like
        The path or file object to ensure is open. If `fobj` is an already open file object, its
        mode is checked to be correct but is otherwise returned as-is. If `fobj` is a string, it is
        opened with the specified `mode` and yielded, then closed once the wrapped context exits.
        Note that passed open file objects are *not* closed.

    mode : str
        The mode to ensure `fobj` is opened with.

    Yields
    ------
    :py:class:`io.FileIO`
        The open file with the specified `mode`.

    Raises
    ------
    ValueError
        If `fobj` is not a string nor open file, or if `fobj` is open but with a different `mode`.
    """
    close = False

    if isinstance(fobj, str):
        fobj = open(fobj, mode)
        close = True  # Close the file we just opened once we're done.
    else:
        try:
            # Ensure mode agrees.
            if fobj.mode != mode:
                raise ValueError(
                    f"Unexpected mode for '{fobj.name}' (expected '{mode}', got '{fobj.mode}')"
                )
        except AttributeError:
            raise ValueError(f"'{fobj}' is not an open file or path.")

    try:
        yield fobj
    finally:
        if close:
            fobj.close()


@contextmanager
def logs(level=None, exclude=None, fmt=None, datefmt=None, jupyter_tracebacks=None):
    """Change the default Finesse log stream handler behaviour in the encapsulated
    context.

    Parameters
    ----------
    level : str or int, optional
        The minimum log levels to print. The standard log levels "debug", "info",
        "warning", "error" and "critical" are supported, as are their corresponding
        level numbers (see :py:mod:`logging`).

    exclude : str or list of str, optional
        Log channel(s) to exclude. Simple wildcards are supported:

        - ``*`` matches 0 or more characters
        - ``?`` matches any single character
        - ``[abc]`` matches any characters in abc
        - ``[!abc]`` matches any characters not in abc

    fmt, datefmt : str, optional
        The stream format to use. The string specified for `fmt` should use "{" style
        parameters as supported by :class:`logging.Formatter`. The `datefmt` string
        should be a :func:`time.strftime` compatible format. Defaults to the existing
        builtin stream handler's default format.

    jupyter_tracebacks : bool, optional
        Whether to show full Jupyter tracebacks for :class:`parsing errors
        <.KatParserError>` raised within the encapsulated context. Defaults to `None`,
        which leaves the current value (which is by default determined by the
        environment in which Finesse is running) unchanged.

    Raises
    ------
    :class:`.ExistingLogHandlerError`
        If the current :mod:`finesse` root logger's first handler was not the one
        autoconfigured by Finesse upon first import. This function does not handle cases
        where the user has configured their own logging.

    Examples
    --------
    Print debug logs during parsing.

    >>> from finesse import Model
    >>> from finesse.utilities import logs
    >>> model = Model()
    >>> with logs(level="debug"):
    >>>     model.parse("laser l1 P=1")
    """
    from .. import show_tracebacks, PROGRAM
    from ..config import log_handler_instance

    logger = logging.getLogger(PROGRAM)
    handler = log_handler_instance()
    old_level = None
    old_excludes = None
    old_formatter = None
    old_tracebacks = None

    if level is not None:
        old_level = logger.level

        try:
            # Convert level name to uppercase.
            level = level.upper()
        except AttributeError:
            # Probably a number.
            pass

        logger.setLevel(level)

    if exclude is not None:
        if isinstance(exclude, str):
            exclude = [exclude]

        old_excludes = handler.reset_exclude_patterns()
        for pattern in exclude:
            handler.exclude(pattern)

    if fmt is not None or datefmt is not None:
        # We can't copy the format string out of the formatter, so we replace the object
        # instead and restore it later.
        old_formatter = handler.formatter

        if datefmt is None:
            # Use the default date format from the old handler.
            datefmt = old_formatter.datefmt

        handler.setFormatter(logging.Formatter(fmt, datefmt, style="{"))

    if jupyter_tracebacks is not None:
        old_tracebacks = show_tracebacks(jupyter_tracebacks)

    # Run the code in the context.
    yield

    if old_level is not None:
        logger.setLevel(old_level)

    if old_excludes is not None:
        handler.reset_exclude_patterns()
        for pattern in old_excludes:
            handler.exclude(pattern)

    if old_formatter is not None:
        handler.setFormatter(old_formatter)

    if old_tracebacks is not None:
        show_tracebacks(old_tracebacks)


def graph_layouts():
    """Available NetworkX and graphviz (if installed) graph plotting layouts."""
    return {**networkx_layouts(), **graphviz_layouts()}


def networkx_layouts():
    """Available NetworkX graph plotting layouts."""
    import inspect
    import networkx

    # Excluded layouts.
    excluded = (
        "rescale",
        # These layouts need the network to first be grouped into sets.
        "bipartite",
        "multipartite_layout",
    )

    layouts = {}
    suffix = "_layout"

    def find_layouts(members):
        for name, func in members:
            if name.startswith("_") or not name.endswith(suffix):
                # Not a public layout.
                continue

            # Strip the "_layout" part.
            name = name[: -len(suffix)]

            if name in excluded:
                continue

            layouts[name] = func

    find_layouts(inspect.getmembers(networkx.drawing.layout, inspect.isfunction))

    return layouts


def graphviz_layouts():
    """Available graphviz graph plotting layouts."""
    import networkx
    from ..environment import has_pygraphviz

    layouts = {}

    if has_pygraphviz():
        for layout in ["neato", "dot", "fdp", "sfdp", "circo"]:
            # Returns callable that can be called like `networkx.drawing.layout` members.
            layouts[layout] = partial(
                networkx.drawing.nx_agraph.pygraphviz_layout, prog=layout
            )

    return layouts


def doc_element_parameter_table(cls):
    """Prints table for a particular element class."""
    import finesse
    import tabulate
    from IPython.core.display import HTML
    from functools import partial
    from types import SimpleNamespace

    # object counter to keep track of odd and even rows
    i = SimpleNamespace()
    i.current = -1

    def my_html_row_with_attrs(celltag, cell_values, colwidths, colaligns, **kwargs):
        alignment = {
            "left": ' style="text-align: left;"',
            "right": ' style="text-align: right;"',
            "center": ' style="text-align: center;"',
            "decimal": ' style="text-align: right;"',
        }
        values_with_attrs = [
            "<{0}{1}>{2}</{0}>".format(celltag, alignment.get(a, ""), c)
            for c, a in zip(cell_values, colaligns)
        ]
        kwargs["i"].current += 1
        return (
            f"<tr style=\"vertical-align: middle;\" class=\"row-{'even' if kwargs['i'].current % 2 else 'odd'}\">"
            + "".join(values_with_attrs).rstrip()
            + "</tr>"
        )

    def process_changeable(pinfo):
        if pinfo.changeable_during_simulation:
            return "<div style='color:green;'>✓</div>"
        else:
            return "<div style='color:red;'>✗</div>"

    SphinxTable = tabulate.TableFormat(
        lineabove=tabulate.Line(
            '<table class="docutils align-default"><thead>', "", "", ""
        ),
        linebelowheader=tabulate.Line("</thead>", "", "", ""),
        linebetweenrows=None,
        linebelow=tabulate.Line("</table>", "", "", ""),
        headerrow=partial(my_html_row_with_attrs, "th", i=i),
        datarow=partial(my_html_row_with_attrs, "td", i=i),
        padding=0,
        with_header_hide=None,
    )
    tbl = [
        (p.name, p.description, p.units, p.dtype.__name__, process_changeable(p))
        for p in finesse.element.ModelElement._param_dict[cls][::-1]
    ]
    a = tabulate.tabulate(
        tbl,
        tablefmt=SphinxTable,
        colalign=("left", "left", "center", "center", "center"),
        headers=(
            "Name",
            "Description",
            "Units",
            "Data type",
            "Can change during simualation",
        ),
    )
    return HTML(a)
