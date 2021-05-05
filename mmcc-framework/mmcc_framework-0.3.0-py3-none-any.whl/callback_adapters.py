from abc import ABC, abstractmethod
from typing import Any, Callable, Dict

from mmcc_framework.activity import Activity
from mmcc_framework.exceptions import MissingCallbackException
from mmcc_framework.response import Response

Callback = Callable[[
    Dict[str, Any],  # data
    Dict[str, Any],  # kb
    Dict[str, Any],  # context
    Activity
], Response]
"""A function that takes data, kb, context, current activity and returns a Response."""


class CallbackAdapter(ABC):
    """A class that provides a method to access the callbacks."""

    @abstractmethod
    def get(self, identifier: str) -> Callback:
        """Returns the callback corresponding to the identifier.

        :raises MissingCallbackException: if no callback corresponds to the identifier
        """
        raise NotImplementedError()

    @abstractmethod
    def check(self, identifier: str) -> bool:
        """Returns true if the identifier is valid."""
        raise NotImplementedError()


class DictCallback(CallbackAdapter):
    """Takes the callbacks from the provided dictionary `callbacks`."""

    def __init__(self, callbacks: Dict[str, Callback]) -> None:
        self.callbacks = callbacks

    def get(self, identifier: str) -> Callback:
        try:
            return self.callbacks[identifier]
        except KeyError as err:
            raise MissingCallbackException(cause=identifier) from err

    def check(self, identifier: str) -> bool:
        return identifier in self.callbacks


class FunctionCallback(CallbackAdapter):
    """Adapts the old method (function that returns the callback) for handling callbacks."""

    def __init__(self, callbacks: Callable[[str], Callback]) -> None:
        self.callbacks = callbacks

    def get(self, identifier: str) -> Callback:
        try:
            return self.callbacks(identifier)
        except KeyError as err:
            raise MissingCallbackException(cause=identifier) from err

    def check(self, identifier: str) -> bool:
        try:
            return callable(self.get(identifier))
        except MissingCallbackException:
            return False
