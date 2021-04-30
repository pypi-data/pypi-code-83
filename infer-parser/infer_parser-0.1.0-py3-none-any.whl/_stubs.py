"""Stub unsupported types for PYthon 3.7 and 3.8."""

import types
import typing as t


def get_origin(hint: t.Any) -> t.Any:
    """Return type hint origin."""
    try:
        return hint.__origin__
    except AttributeError:
        return None


def get_args(hint: t.Any) -> t.Tuple[t.Any, ...]:
    """Return type hint args."""
    try:
        assert isinstance(hint.__args__, tuple)
        return hint.__args__
    except AttributeError:
        return ()


class Stub:
    "Stub for unsupported types."
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Does nothing."""

    def __getitem__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Does nothing."""
        return self


def stub(module: t.Any, name: str, value: t.Any = Stub()) -> None:
    """Stub name."""
    if not hasattr(module, name):
        setattr(module, name, value)


def create_all() -> None:
    """Create stubs."""
    stub(t, "Annotated")
    stub(t, "Final")
    stub(t, "Literal")
    stub(t, "get_args", get_args)
    stub(t, "get_origin", get_origin)
    stub(types, "GenericAlias", type("GenericAliasStub", (), {}))


__all__ = ["create_all"]
