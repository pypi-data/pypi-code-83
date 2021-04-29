"""Finesse environment information."""

import sys

try:
    from IPython.core.ultratb import AutoFormattedTB
except ImportError:
    AutoFormattedTB = None

from .datastore import invalidate, init_singleton

# Platform detection.
IS_WINDOWS = sys.platform.startswith("win")


def traceback_handler_instance():
    return init_singleton(_TracebackHandler)


def reset_traceback_handler():
    invalidate(_TracebackHandler)


def is_interactive():
    """Check if Finesse is being run from an interactive environment.

    Returns
    -------
    bool
        `True` if a Jupyter notebook, Qt console or IPython shell is in use, `False`
        otherwise.
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return True  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


def show_tracebacks(show_tb=None):
    """Get or set whether to show tracebacks in Jupyter/IPython in full form or just as
    a single error message.

    Parameters
    ----------
    show_tb : bool, optional
        Set whether to show tracebacks; defaults to None, which doesn't change the
        current setting.

    Returns
    -------
    bool
        The current setting value (if `show_tb` was not set) or the previous setting
        value (if `show_tb` was set).
    """
    tb = traceback_handler_instance()
    previous = tb.show_tb
    if show_tb is not None:
        tb.show_tb = show_tb
    return previous


def tb():
    """Show the last traceback in full."""
    tb = traceback_handler_instance()
    tb.show_last()


def has_pygraphviz():
    """Determine if pygraphviz and graphviz are available on the current path.

    Returns
    -------
    bool
        `True` if pygraphviz and graphviz are available, `False` otherwise.

    Notes
    -----

    This returns `False` if either pygraphviz or graphviz is not installed or correctly
    configured. If pygraphviz is installed but graphviz is not installed or could not be
    found, an import error complaining about something like "libagraph.so.1" is emitted
    (see the `pygraphviz FAQ
    <https://pygraphviz.github.io/documentation/stable/reference/faq.html>`_).
    """
    try:
        import pygraphviz  # noqa: F401
    except ImportError:
        return False
    return True


class _TracebackHandler:
    """Handler for user errors during parse and build.

    This detects the environment within which the user is running Finesse - either a
    normal Python terminal or script or within IPython or JupyterLab. Depending on the
    environment, either complete tracebacks are shown or else only the error message.

    The behaviour of this handler can be configured globally using
    :func:`.show_tracebacks`.

    Do not instantiate this class directly; use :func:`traceback_handler_instance`.
    """

    def __init__(self):
        self.show_tb = True
        self.etype = None
        self.evalue = None
        self.tb = None
        self.stb = None
        self.text = None
        self.a = None

        if AutoFormattedTB is not None:
            self.a = AutoFormattedTB(
                mode="Context", color_scheme="Neutral", tb_offset=1
            )

    def store_tb(self):
        import traceback

        self.etype, self.evalue, self.tb = sys.exc_info()

        if AutoFormattedTB is not None:
            self.stb = self.a.structured_traceback(
                self.etype, self.evalue, self.tb, tb_offset=1
            )
            self.text = self.a.stb2text(self.stb)
        else:
            self.text = traceback.format_exc()

    def get_stb(self):
        if self.show_tb:
            return self.stb
        else:
            return self.stb[-1:]

    def get_text(self):
        return self.text

    def show_last(self):
        print(self.text)
