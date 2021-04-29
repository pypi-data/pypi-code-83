"""Kat script to Finesse object adapters.

Adapters provide various useful information to the kat script compiler about Finesse
objects, and vice versa for the kat script generator.
"""

import abc
import inspect
import logging

LOGGER = logging.getLogger(__name__)


def _remove_signature_parameters(signature, remove_first=True, remove_extra=None):
    """Remove any parameter whose name appears in `remove` from `signature`.

    There is also the option to remove the first parameter, which is usually "self" (in
    the case of methods) or some parameter that receives the container (e.g. a
    :class:`.Model` in the case of commands).
    """
    if not remove_extra:
        remove_extra = []
    parameters = []
    for i, (name, parameter) in enumerate(signature.parameters.items()):
        if i == 0 and remove_first:
            continue
        if name in remove_extra:
            continue
        parameters.append(parameter)
    return signature.replace(parameters=parameters)


class BaseAdapter(metaclass=abc.ABCMeta):
    """Adapter defining a kat script instruction and how it maps to/from a type.

    This encapsulates the required information to take a kat script instruction and
    generate a corresponding Python object (e.g. a :class:`.Laser` from a `laser l1 ...`
    instruction) and to dump that Python object back to kat script.

    This is an abstract class that should be subclassed.

    Parameters
    ----------
    aliases : str or sequence
        The instruction alias(es). The first is considered the full name and is dumped
        in full archival mode. The last is considered the short form name and used in
        default dump mode. Any other specified aliases are only supported for parsing.

    setter : type
        The Python setter type for this instruction. This is used to build Python
        objects for elements, analyses, etc., and to set values in the model for
        commands.

    getter : type or callable, optional
        The Python getter type for this instruction. This is used to retrieve the
        object's current parameter values to generate its kat script representation. If
        `getter` is not specified, it is assumed that this instruction should not be
        regenerated in kat script. This may be the same as `setter` or alternatively a
        class that inherts :class:`.GetterProxy`. In the latter case the object should
        implement a `__call__` method that accepts the containing object and returns
        either a single (args, kwargs) tuple or a sequence thereof, depending on
        `singular`.

    singular : bool
        Whether the instruction can only be specified once per script. In such a case,
        if `getter` is a `GetterProxy`, it should only define a single `(args, kwargs)`
        tuple instead of a sequence thereof.

    build_last : bool, optional
        Whether to build the Python object last, regardless of dependencies. This is
        useful for elements with implicit dependencies (see e.g. the cavity adapter). Be
        careful using this flag because statements for other adapters that depend on
        statements for adapters with this flag will be built first. Defaults to False.

    Raises
    ------
    ValueError
        If `aliases` sequence has less than 1 entry.
    """

    def __init__(
        self, aliases, setter, getter=None, singular=False, build_last=False,
    ):
        if isinstance(aliases, str):
            aliases = [aliases]

        if len(aliases) < 1:
            raise ValueError("At least one alias must be specified in 'aliases'")

        self.aliases = aliases
        self.setter = setter
        self.getter = getter
        self.singular = singular
        self.build_last = build_last

    @property
    def full_name(self):
        return self.aliases[0]

    @property
    def short_name(self):
        return self.aliases[-1]

    @abc.abstractmethod
    def apply(self, model, *args, **kwargs):
        raise NotImplementedError

    def get(self, container):
        """Get ordered mapping of argument names to values from `container`.

        Parameters
        ----------
        container : object
            The container to retrieve argument names and values for.

        Returns
        -------
        :class:`list`
            Positional argument values.

        :class:`dict`
            Mapping of keyword argument names to values.

        Raises
        ------
        RuntimeError
            If this adapter's :meth:`.dump_signature` contains parameters that are not
            present in `container`.
        """
        if not self.getter:
            LOGGER.debug(f"{self!r} has no kat script representation")
            return

        if isinstance(self.getter, GetterProxy):
            params = self.getter(container)

            if params is None:
                LOGGER.debug(
                    f"skipping serialisation of empty {self!r} parameters (returned "
                    f"from a GetterProxy)"
                )
                return

            return params
        else:
            kwargs = {}
            for arg, param in self.dump_signature().parameters.items():
                name = param.name
                try:
                    # Try to get the attribute value.
                    value = getattr(container, name)
                except AttributeError as e:
                    raise RuntimeError(
                        f"The dump signature (getter) for '{self!r}' defines parameter "
                        f"'{name}' that is not a property or attribute of "
                        f"'{container!r}'. Either define "
                        f"'{container.__class__.__name__}.{name}' as a property or "
                        f"attribute or set {self.full_name}'s `getter` to a "
                        f"`GetterProxy` object (see BaseAdapter docstring)."
                    ) from e

                kwargs[name] = value

        # FIXME: in the future, this should support being able to return parameters in
        # different modes, like positional or keyword-only.
        return [], kwargs

    @property
    def docobj_type(self):
        """Type to use to get the Python object's docstring.

        :getter: Returns the type to be used to retrieve the Python object's docstring.

        Notes
        -----
        This assumes that classes contain the documentation for the `__init__` method,
        in line with the Numpydoc convention.
        """
        signature_type = self.setter

        if isinstance(signature_type, property):
            # Use the setter's signature.
            signature_type = signature_type.fset

        return signature_type

    def doc_signature(self, exclude_name=False):
        """The signature of the documentation object.

        This is an ordered mapping of the Python object's supported parameters to
        :py:class:`inspect.Parameter` objects.

        Parameters
        ----------
        exclude_name : bool, optional
            Exclude the `name` parameter. This is useful for code that already handles
            the name separately. Defaults to `False`.

        Returns
        -------
        :py:class:`inspect.Signature`
            The documentation object's pseudo-signature.
        """
        return _remove_signature_parameters(
            inspect.signature(self.docobj_type),
            remove_first=True,
            remove_extra=["name"] if exclude_name else [],
        )

    @property
    def call_signature_type(self):
        """Type to use to get the Python object's call signature.

        :getter: Returns the type to be used to retrieve the Python object's call
                 signature.
        """
        signature_type = self.setter

        if inspect.isclass(signature_type):
            # Use the init method.
            signature_type = signature_type.__init__
        elif isinstance(signature_type, property):
            # Use the setter's signature.
            signature_type = signature_type.fset

        return signature_type

    def call_signature(self, exclude_name=False):
        """The call signature of the corresponding Python object constructor.

        This is an ordered mapping of the Python object's supported parameters to
        :py:class:`inspect.Parameter` objects.

        Parameters
        ----------
        exclude_name : bool, optional
            Exclude the `name` parameter. This is useful for code that already handles
            the name separately. Defaults to `False`.

        Returns
        -------
        :py:class:`inspect.Signature`
            The call object's pseudo-signature.
        """
        return _remove_signature_parameters(
            inspect.signature(self.call_signature_type),
            remove_first=True,
            remove_extra=["name"] if exclude_name else [],
        )

    @property
    def dump_signature_type(self):
        signature_type = self.getter

        if isinstance(signature_type, GetterProxy):
            # You're doing it wrong.
            raise TypeError(
                "Adapter has a getter proxy set, so no dump signature type exists. "
                "Change the code calling this method to first check the getter type."
            )

        if inspect.isclass(signature_type):
            # Use the init method.
            signature_type = signature_type.__init__
        elif isinstance(signature_type, property):
            # Use the getter's signature.
            signature_type = signature_type.fget

        return signature_type

    def dump_signature(self, exclude_name=False):
        """The Python object constructor call signature as available to the generator.

        This is used when generating kat script for the corresponding Python object and
        may exclude or include parameters found or not found in the real Python object
        constructor, e.g. to allow a kat script command to use different arguments to
        that of the Python API.

        Parameters
        ----------
        exclude_name : bool, optional
            Exclude the `name` parameter. This is useful for code that already handles
            the name separately. Defaults to `False`.

        Returns
        -------
        :py:class:`inspect.Signature`
            The dump object's pseudo-signature.
        """
        return _remove_signature_parameters(
            inspect.signature(self.dump_signature_type),
            remove_first=True,
            remove_extra=["name"] if exclude_name else [],
        )

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.full_name} @ {hex(id(self))}>"


class ModelObject(BaseAdapter, metaclass=abc.ABCMeta):
    """Mixin for adapters that control Python objects directly (e.g. elements) as
    opposed to attributes (e.g. commands)."""

    def compile(self, args, kwargs):
        return self.setter(*args, **kwargs)


class ElementAdapter(ModelObject, BaseAdapter):
    """Adapter for elements."""

    def apply(self, model, item):
        model.add(item)

    def get(self, item):
        # Split the name argument onto its own.
        args, kwargs = super().get(item)
        element_name = kwargs.pop("name")
        return element_name, args, kwargs


class CommandAdapter(BaseAdapter):
    """Adapter for commands.

    Commands set properties of a :class:`.Model`.

    Command getters should return a *sequence* of args and kwargs representing
    potentially multiple commands to dump.
    """

    def apply(self, model, allargs):
        # The compiler passes this method an (args, kwargs) tuple when building
        # commands.
        args, kwargs = allargs
        return self.setter(model, *args, **kwargs)


class AnalysisAdapter(ModelObject, BaseAdapter):
    """Adapter for analyses."""

    def apply(self, model, item):
        model.analysis = item


class GetterProxy(metaclass=abc.ABCMeta):
    """An object that when called returns the parameters and values that should be
    dumped to represent an object in kat script.

    Inheriting classes should define `__call__`, returning an ordered mapping of
    parameters to values.
    """

    @abc.abstractmethod
    def __call__(self, item):
        raise NotImplementedError
