from __future__ import annotations

import abc
import typing

from lime_uow import exceptions, resource, shared_resource_manager

__all__ = (
    "PlaceholderUnitOfWork",
    "UnitOfWork",
)

T = typing.TypeVar("T", bound="UnitOfWork")
R = typing.TypeVar("R", bound=resource.Resource[typing.Any])


class UnitOfWork(abc.ABC):
    def __init__(self):
        # fmt: off
        self.__resources: typing.Optional[typing.Dict[str, resource.Resource[typing.Any]]] = None
        self.__resources_validated = False
        self.__shared_resource_manager: typing.Optional[shared_resource_manager.SharedResourceManager] = None
        self.__context_manager_open = False
        # fmt: on

    def __enter__(self: T) -> T:
        if self.__context_manager_open:
            raise exceptions.NestedWithBlockException()

        if self.__shared_resource_manager is None:
            shared_resources = self.create_shared_resources()
            # fmt: off
            self.__shared_resource_manager = shared_resource_manager.SharedResourceManager(*shared_resources)
            # fmt: on
        fresh_resources = self.create_resources(self.__shared_resource_manager)
        resource.check_for_ambiguous_implementations(fresh_resources)
        self.__resources = {r.key(): r for r in fresh_resources}
        self.__resources_validated = True
        self.__context_manager_open = True
        return self

    def __exit__(self, *args) -> typing.Literal[False]:
        errors: typing.List[exceptions.RollbackError] = []
        try:
            self.rollback()
        except exceptions.RollbackErrors as e:
            errors += e.rollback_errors
        self.__resources = None
        if errors:
            raise exceptions.RollbackErrors(*errors)
        self.__context_manager_open = False
        return False

    def close(self) -> None:
        if self.__shared_resource_manager:
            self.__shared_resource_manager.close()

    def exists(self, /, key: str) -> bool:
        if self.__resources is None:
            raise exceptions.OutsideTransactionError(
                f"Attempted to access the key, {key}, within a UnitOfWork outside of a with block."
            )
        else:
            return key in self.__resources.keys()

    def get(
        self, resource_type: typing.Type[R], *, key: typing.Optional[str] = None
    ) -> R:
        if key is None:
            try:
                key = resource_type.key()
            except AttributeError as e:
                raise exceptions.LimeUoWException(
                    f"The {resource_type.__name__} class does not have the requisite .key() "
                    "attribute to comprise a valid resource."
                )
        if self.__resources is None or self.__shared_resource_manager is None:
            raise exceptions.OutsideTransactionError(
                f"Attempted to access {resource_type.__name__} within a UnitOfWork outside of a "
                f"with block."
            )
        else:
            if key in self.__resources.keys():
                rsrc = self.__resources[key]
            elif self.__shared_resource_manager.exists(key):
                rsrc = self.__shared_resource_manager.get(resource_type, key=key)
            else:
                raise exceptions.MissingResourceError(
                    key=key,
                    available_resources=self.__resources.keys(),
                )
            return typing.cast(R, rsrc)

    @abc.abstractmethod
    def create_resources(
        self, /, shared_resources: shared_resource_manager.SharedResourceManager
    ) -> typing.Iterable[resource.Resource[typing.Any]]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_shared_resources(
        self,
    ) -> typing.Iterable[resource.Resource[typing.Any]]:
        raise NotImplementedError

    def rollback(self):
        errors: typing.List[exceptions.RollbackError] = []
        if self.__resources is None:
            raise exceptions.OutsideTransactionError(
                "Attempted to rollback a UnitOfWork outside a with-block."
            )
        else:
            for r in self.__resources.values():
                try:
                    r.rollback()
                except Exception as e:
                    errors.append(
                        exceptions.RollbackError(
                            f"An error occurred while rolling back {self.__class__.__name__}: {e}",
                        )
                    )

        if errors:
            raise exceptions.RollbackErrors(*errors)

    def save(self):
        # noinspection PyBroadException
        try:
            if self.__resources is None:
                raise exceptions.OutsideTransactionError()
            else:
                for r in self.__resources.values():
                    r.save()
        except:
            self.rollback()
            raise


class PlaceholderUnitOfWork(UnitOfWork):
    def __init__(self):
        super().__init__()

    def create_resources(
        self, shared_resources: shared_resource_manager.SharedResourceManager
    ) -> typing.List[resource.Resource[typing.Any]]:
        return []

    def create_shared_resources(self) -> typing.List[resource.Resource[typing.Any]]:
        return []
