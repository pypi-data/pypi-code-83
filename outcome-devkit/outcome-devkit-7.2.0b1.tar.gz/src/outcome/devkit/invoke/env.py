"""Helper to get/cache various variables to be used during invoke tasks.

Provides a mechansim to declare keys, and how to determine the value of those keys.
The values are only resolved once, and can refer to other values in a form of informal graph.

For example:

from outcome.devkit.invoke import env

# The most basic scenario is to declare a value
env.declare('my_key', 'my constant')


# Or you can declare a value based on a function. The name of the function will be the key.
@env.add
def my_key(e: env.Env) -> str:
    return 'my static value'


# Functions can refer to other env keys, creating a graph - be careful of loops!
@env.add
def my_graph_key(e: env.Env) -> str:
    return e.read(my_key)


# As a shortcut, you can just refer to an environment variable
env.from_os('MY_ENV_VAR')
env.from_os('my_alias', os_key='MY_ENV_VAR')


# Then, you can read the value wherever
def my_func():
    val = env.read(my_key)
"""

from __future__ import annotations

import os
from functools import partial
from typing import Any, Callable, Dict, Generic, List, Literal, Optional, Protocol, TypeVar, Union, cast, overload  # noqa: WPS235

from outcome.utils.config import Config

Value = Union[str, int, float, bool]
T = TypeVar('T', str, int, float, bool)
C = TypeVar('C', str, int, float, bool, covariant=True)

SourceFn = Callable[['Env'], Optional[T]]
Source = Union[SourceFn[T], Optional[T]]


class EnvItem(Generic[T]):
    """An EnvItem represents a specific key and value, and how to calculate that value.

    You shouldn't have to explicitly access EnvItem objects.
    """

    name: str
    run: bool
    value: Optional[T]
    source: Source[T]
    env: Env

    def __init__(self, name: str, source: Source[T], env: Env) -> None:
        self.name = name
        self.run = False
        self.value = None
        self.source = source
        self.env = env

    @overload
    def read(self) -> T:  # pragma: no cover
        ...

    @overload
    def read(self, required: Literal[True]) -> T:  # pragma: no cover
        ...

    @overload
    def read(self, required: bool) -> Optional[T]:  # pragma: no cover
        ...

    def read(self, required: bool = True) -> Optional[T]:
        if not self.run:
            if callable(self.source):
                # For some reason, the type narrowing doesn't work here
                self.value = cast(SourceFn[T], self.source)(self.env)
            else:
                self.value = self.source

            self.run = True

        if required and self.value is None:
            raise RuntimeError(f"Env item '{self.name}' is required!")

        return self.value


class Env:  # noqa: WPS214
    items: Dict[str, EnvItem[Any]]

    def __init__(self):
        self.reset()

    @overload
    def add(
        self,
        fn: None = None,
        *,
        key: Optional[str] = None,  # noqa: WPS234
    ) -> Callable[[SourceFn[T]], EnvItem[T]]:  # pragma: no cover
        ...

    @overload
    def add(self, fn: SourceFn[T], *, key: Optional[str] = None) -> EnvItem[T]:  # pragma: no cover
        ...

    def add(  # noqa: WPS234
        self,
        fn: Optional[SourceFn[T]] = None,
        key: Optional[str] = None,
    ) -> Union[EnvItem[T], Callable[[SourceFn[T]], EnvItem[T]]]:
        # This can be used as a straight decorator, or a parameterized decorator
        #
        # @env.add
        # def foo() -> str: ...  # noqa: E800
        #
        # @env.add(required=False)
        # def bar() -> Optional[str]: ...  # noqa: E800

        if callable(fn):
            key = key or fn.__name__
            return self._add(key, fn)

        def decorator(f: SourceFn[T]) -> EnvItem[T]:
            return self.add(f, key=key)

        return decorator

    @overload
    def read(self, key: EnvItem[T]) -> T:  # pragma: no cover
        ...

    @overload
    def read(self, key: EnvItem[T], require: Literal[True]) -> T:  # pragma: no cover
        ...

    @overload
    def read(self, key: EnvItem[T], require: bool = ...) -> Optional[T]:  # pragma: no cover
        ...

    def read(self, key: EnvItem[T], require: bool = True) -> Optional[T]:
        try:
            item = self.items[key.name]
            return item.read(require)
        except KeyError:  # pragma: no cover
            raise ValueError(f'Unknown env item! {key}')

    def from_os(self, key: str, os_key: Optional[str] = None, required: bool = True) -> EnvItem[str]:
        effective_os_key = os_key or key

        def read_from_os(env: Env) -> Optional[str]:
            return os.environ.get(effective_os_key, None)

        return self.add(read_from_os, key=key)

    def from_config(self, key: str, with_type: type, config: Optional[Config] = None) -> EnvItem[Value]:
        effective_config = config or Config()

        def read_from_config(env: Env) -> Optional[Any]:
            try:
                value = effective_config.get(key)
            except KeyError:
                return None
            # Lists aren't handled
            assert not isinstance(value, List)

            return with_type(value)

        return self.add(read_from_config, key=key)

    def declare(self, key: str, value: T) -> EnvItem[T]:
        return self._add(key, value)

    def reset(self):
        self.items = {}

    def _add(self, key: str, source: Source[T]) -> EnvItem[T]:
        if key in self.items:
            raise ValueError(f'Duplicate env item! {key}')

        self.items[key] = EnvItem(key, source, self)

        return self.items[key]


env = Env()


r = env.read
read = env.read
add = env.add
from_os = env.from_os
declare = env.declare
reset = env.reset


class FromConfigProtocol(Protocol[C]):  # pragma: no cover
    def __call__(self, key: str, config: Optional[Config] = None) -> EnvItem[C]:
        ...


str_from_config = cast(FromConfigProtocol[str], partial(env.from_config, with_type=str))
int_from_config = cast(FromConfigProtocol[int], partial(env.from_config, with_type=int))
float_from_config = cast(FromConfigProtocol[float], partial(env.from_config, with_type=float))
bool_from_config = cast(FromConfigProtocol[bool], partial(env.from_config, with_type=bool))
