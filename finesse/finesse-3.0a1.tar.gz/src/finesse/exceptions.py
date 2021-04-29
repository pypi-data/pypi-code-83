"""Custom exception types raised by different Finesse functions and class methods."""

from .environment import traceback_handler_instance


class FinesseException(Exception):
    """The exception type which gets raised upon a Finesse failure.

    This identifies whether the current session is interactive or not, and consequently
    sets the level of verbosity. This can be overridden by calling
    :func:`~finesse.environment.show_tracebacks` with ``True``.
    """

    def __init__(self, message, **kwargs):
        if not traceback_handler_instance().show_tb:
            head = "\t(use finesse.tb() to see the full traceback)\n"
        else:
            head = "\n"
        message = head + str(message)
        super().__init__(message, **kwargs)

    def _render_traceback_(self):
        """use custom traceback in IPython/Jupyter."""
        tb = traceback_handler_instance()
        tb.store_tb()

        return tb.get_stb()


class ComponentNotConnected(FinesseException):
    pass


class ParameterLocked(FinesseException):
    pass


class NodeException(FinesseException):
    """Exception associated with :class:`.Node` related run-time errors.

    Objects of type `NodeException` store the error message as well as an optional reference to the
    node(s) which caused the exception to be raised.

    Parameters
    ----------
    message : str
        The error message.

    node : :class:`.Node`, optional
        A reference to the offending node(s), defaults to `None`. This can be a single node or a
        sequence of nodes.
    """

    def __init__(self, message, node=None):
        super().__init__(message)
        self.__node = node

    @property
    def node(self):
        """The node(s) responsible for raising this exception instance.

        :getter: Returns the node(s) (either a single :class:`.Node` object
                 or a sequence of these objects) responsible for the exception
                 (read-only).
        """
        return self.__node


class BeamTraceException(FinesseException):
    pass


class TotalReflectionError(FinesseException):
    """Exception indicating total reflection of a beam at a component when performing
    beam tracing.

    Parameters
    ----------
    message : str
        The error message.

    from_node, to_node : :class:`.Node`
        References to the offending source and target nodes, respectively.
    """

    def __init__(self, message, from_node=None, to_node=None):
        super().__init__(message)
        self.__from_node = from_node
        self.__to_node = to_node

    @property
    def coupling(self):
        """The tuple of (from, to) nodes responsible for the total reflection error.

        :getter: Returns the nodes responsible for the exception (read-only).
        """
        return (self.__from_node, self.__to_node)


class ModelAttributeError(FinesseException):
    """Error indicating a model path was not found.

    Model paths can be e.g. `l1.P` or `s1.p1.o`.

    This exists mainly so it can be caught by the parser.
    """

    def __init__(self, pieces):
        self.path = ".".join(pieces)

        if self.path.endswith("."):
            msg = f"'{self.path}' should not end with a '.'"
        else:
            msg = f"model has no attribute '{self.path}'"

        super().__init__(msg)


class ModelParameterDefaultValueError(FinesseException):
    """Error indicating a model element has no default model parameter.

    Some model parameters have defaults, such that they can be referenced in kat script
    using e.g. `&myvar` instead of `&myvar.value`. This error indicates a model element
    without such a default was referenced directly.
    """

    def __init__(self, element):
        super().__init__(
            f"{element.name} cannot be referenced because type '{element.__class__.__name__}' has "
            f"no default model parameter"
        )


class ModelParameterSelfReferenceError(FinesseException):
    """Error indicating a model parameter cannot be set to refer to itself."""

    def __init__(self, value, parameter):
        super().__init__(
            f"cannot set {parameter.full_name} to self-referencing value {value}"
        )
        self.value = value
        self.parameter = parameter
