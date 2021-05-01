from __future__ import annotations

import abc
import typing

from lime_uow import exceptions

__all__ = (
    "Resource",
    "check_for_ambiguous_implementations",
)

T = typing.TypeVar("T", covariant=True)


class Resource(abc.ABC, typing.Generic[T]):
    def close(self) -> None:
        ...

    @staticmethod
    @abc.abstractmethod
    def key() -> str:
        raise NotImplementedError

    def open(self, **kwargs: typing.Dict[str, typing.Any]) -> T:
        return typing.cast(T, self)

    def rollback(self) -> None:
        ...

    def save(self) -> None:
        ...

    def __eq__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            return self.key == typing.cast(Resource[typing.Any], other).key
        else:
            return NotImplemented

    def __ne__(self, other: object) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self) -> int:
        return hash(self.key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.key}"


def check_for_ambiguous_implementations(
    rs: typing.Iterable[Resource[typing.Any]], /
) -> None:
    names = [r.key() for r in rs]
    duplicate_keys = {name: ct for name in names if (ct := names.count(name)) > 1}
    if duplicate_keys:
        raise exceptions.MultipleRegisteredImplementations(duplicate_keys)
