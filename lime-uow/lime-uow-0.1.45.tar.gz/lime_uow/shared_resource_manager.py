from __future__ import annotations

import types
import typing

from lime_uow import exceptions, resource

__all__ = (
    "SharedResourceManager",
    "PlaceholderSharedResourceManager",
)

T = typing.TypeVar("T")
R = typing.TypeVar("R", bound=resource.Resource[typing.Any])


class SharedResourceManager:
    """
    SharedResources manages resources that live for the duration of the process.
    """

    def __init__(self, /, *shared_resource: resource.Resource[typing.Any]):
        resource.check_for_ambiguous_implementations(shared_resource)

        self.__shared_resources: typing.Dict[str, resource.Resource[typing.Any]] = {
            r.key(): r for r in shared_resource
        }
        self.__opened = False
        self.__closed = False

    def __enter__(self) -> SharedResourceManager:
        if self.__opened:
            raise exceptions.ResourcesAlreadyOpen()
        if self.__closed:
            raise exceptions.SharedResourceManagerClosed()
        self.__opened = True
        return self

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]],
        exc_val: typing.Optional[BaseException],
        exc_tb: typing.Optional[types.TracebackType],
    ) -> typing.Literal[False]:
        self.close()
        return False

    def close(self):
        if self.__closed:
            raise exceptions.SharedResourceManagerClosed()
        for resource_name in self.__shared_resources.keys():
            self.__shared_resources[resource_name].close()
        self.__closed = True
        self.__opened = False

    def exists(self, /, key: str) -> bool:
        return key in self.__shared_resources.keys()

    def get(
        self, resource_type: typing.Type[R], *, key: typing.Optional[str] = None
    ) -> R:
        if key is None:
            key = resource_type.key()

        if self.__closed:
            raise exceptions.SharedResourceManagerClosed()
        elif key in self.__shared_resources.keys():
            r = self.__shared_resources[key]
        else:
            raise exceptions.MissingResourceError(
                key=key, available_resources=self.__shared_resources.keys()
            )
        return typing.cast(R, r)

    def __eq__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            # noinspection PyTypeChecker
            return (
                self.__shared_resources.keys()
                == typing.cast(SharedResourceManager, other).__shared_resources.keys()
            )
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__shared_resources)

    def __repr__(self) -> str:
        resources_str = ", ".join(self.__shared_resources.keys())
        return f"{self.__class__.__name__}: {resources_str}"


class PlaceholderSharedResourceManager(SharedResourceManager):
    def __init__(self):
        super().__init__()
