import typing

__all__ = (
    "InvalidResource",
    "LimeUoWException",
    "MissingResourceError",
    "MultipleRegisteredImplementations",
    "NestedWithBlockException",
    "OutsideTransactionError",
    "RollbackError",
)


class LimeUoWException(Exception):
    """Base class for exceptions arising from the lime-uow package"""

    def __init__(self, /, message: str):
        self.message = message
        super().__init__(message)


class MultipleRegisteredImplementations(LimeUoWException):
    def __init__(self, duplicates: typing.Mapping[str, int], /):
        self.duplicates = duplicates

        examples = ", ".join(
            f"{name} = {ct}" for name, ct in sorted(duplicates.items())
        )
        msg = f"Resource names must be unique, but found the following duplicates: {examples}."
        super().__init__(msg)


class InvalidResource(LimeUoWException):
    def __init__(self, /, message: str):
        super().__init__(message)


class MissingResourceError(LimeUoWException):
    def __init__(self, *, key: str, available_resources: typing.Iterable[str]):
        self.resource_name = key
        msg = (
            f"Could not locate a resource with the key {key!r}.  "
            f"Available resource keys include the following: {', '.join(available_resources)}."
        )
        super().__init__(msg)


class NoCommonAncestor(LimeUoWException):
    def __init__(self, /, message: str):
        super().__init__(message)


class OutsideTransactionError(LimeUoWException):
    def __init__(self, /, message: str):
        super().__init__(message)


class ReadOnlyConnection(LimeUoWException):
    def __init__(self, /, message: str):
        super().__init__(message)


class RollbackError(LimeUoWException):
    def __init__(self, /, message: str):
        super().__init__(message)


class RollbackErrors(LimeUoWException):
    def __init__(self, *rollback_errors: RollbackError):
        self.rollback_errors = rollback_errors
        err_msg = (
            f"The following errors occurred while performing a rollback: "
            f"{'; '.join(e.message for e in rollback_errors)}."
        )
        super().__init__(err_msg)


class ResourcesAlreadyOpen(LimeUoWException):
    def __init__(self):
        super().__init__("SharedResources are already open.")


class SharedResourceManagerClosed(LimeUoWException):
    def __init__(self):
        super().__init__("The SharedResourceManager has already been closed.")


class NestedWithBlockException(LimeUoWException):
    def __init__(self):
        super().__init__("Attempted to open a with-block inside another with-block.")


class ResourceHasNoKey(LimeUoWException):
    def __init__(self, *, resource_name: str):
        super().__init__(
            f"The resource, {resource_name}, does not implement the required .key() static method "
            f"for a resource."
        )
