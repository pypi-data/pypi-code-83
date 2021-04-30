# pylint: disable=unsubscriptable-object
"""Test infer_parser."""

import sys
import typing as t
import pytest
from infer_parser import make_parser


def has_version(major: int, minor: int) -> bool:
    """Check Python version."""
    return (sys.version_info.major, sys.version_info.minor) >= (major, minor)


def test_make_parser_for_bool() -> None:
    """Test make_parser(bool)."""
    parse = make_parser(bool)
    truthy = (
        ["1"],
        ["t"],
        ["true"],
        ["y"],
        ["yes"],
    )
    falsy = (
        ["0"],
        ["f"],
        ["false"],
        ["n"],
        ["no"],
    )
    invalid: t.Tuple[t.List[str], ...] = (
        [],
        [""],
        [" false "],
        [" t.r.u.e."],
        ["true", "false"],
    )

    assert all(map(parse, truthy))
    assert not any(map(parse, falsy))
    for tokens in invalid:
        with pytest.raises(ValueError):
            parse(tokens)


def test_make_parser_for_none() -> None:
    """Test make_parser(None)."""
    parse = make_parser(None)
    assert parse([""]) is None
    assert parse(["none"]) is None
    assert parse(["None"]) is None

    invalid: t.Tuple[t.List[str], ...] = (
        [],
        ["none", "None"],
        ["0"],
    )

    for tokens in invalid:
        with pytest.raises(ValueError):
            parse(tokens)


def test_make_parser_for_float() -> None:
    """Test make_parser(float)."""
    parse = make_parser(float)
    assert parse(["1.5"]) == 1.5
    assert parse(["9.0"]) == 9.0
    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse([""])
    with pytest.raises(ValueError):
        parse(["test"])
    with pytest.raises(ValueError):
        parse(["4", "5"])


def test_make_parser_for_int() -> None:
    """Test make_parser(int)."""
    parse = make_parser(int)
    assert parse(["-5"]) == -5
    assert parse(["9002"]) == 9002
    with pytest.raises(ValueError):
        parse(["0.0"])
    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse([""])
    with pytest.raises(ValueError):
        parse(["4", "5"])


def test_make_parser_for_str() -> None:
    """Test make_parser(str)."""
    parse = make_parser(str)
    assert parse([""]) == ""
    assert parse(["hello world"]) == "hello world"

    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse(["", ""])


def test_make_parser_for_class() -> None:
    """Test make_parser on custom classes."""
    class Err:  # pylint: disable=too-few-public-methods
        """Invalid parser."""

    parse = make_parser(Err)
    with pytest.raises(ValueError):
        parse(["hello"])

    class Ok:  # pylint: disable=too-few-public-methods
        """Valid parser."""
        def __init__(self, arg: str):
            self.arg = arg

    parse = make_parser(Ok)
    result = parse(["hello"])
    assert isinstance(result, Ok)
    assert result.arg == "hello"


def test_make_parser_for_optional() -> None:
    """Test make_parser(Optional[...])."""
    parse = make_parser(t.Optional[float])
    assert parse(["1.5"]) == 1.5
    assert parse([""]) is None
    assert parse(["None"]) is None
    assert parse(["5"]) == 5.0

    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse(["0xe"])


def test_make_parser_for_union() -> None:
    """Test make_parser(Union[...]).

    Order of type parameters matters.
    """
    parse = make_parser(t.Union[float, bool])
    assert parse(["false"]) is False
    assert parse(["False"]) is False
    assert parse(["0"]) == 0
    assert parse(["42"]) == 42

    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse([""])
    with pytest.raises(ValueError):
        parse(["e"])
    with pytest.raises(ValueError):
        parse(["true", "true"])

    zero = make_parser(t.Union[bool, float])("0")
    assert zero is False


@pytest.mark.skipif(not has_version(3, 8), reason="No t.Final")
def test_make_parser_for_final() -> None:
    """Test make_parser(Final[...])."""
    final = getattr(t, "Final")
    for type_ in [int, float, str]:
        assert make_parser(final[type_]) == make_parser(type_)


@pytest.mark.skipif(not has_version(3, 9), reason="No t.Annotated")
def test_make_parser_for_annotated() -> None:
    """Test make_parser on Annotated and Final types."""
    annotated = getattr(t, "Annotated")
    assert make_parser(annotated[bool, None]) == make_parser(bool)
    assert make_parser(annotated[str, ...]) == make_parser(str)


def test_make_parser_for_fixed_length_typing_tuple() -> None:
    """Test make_parser on fixed-length Tuple types."""
    parse = make_parser(t.Tuple[int, float])
    result = parse(["5", "5"])
    assert isinstance(result, tuple)
    assert isinstance(result[0], int)
    assert isinstance(result[1], float)
    assert result == (5, 5.0)

    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse([""])
    with pytest.raises(ValueError):
        parse(["5"])
    with pytest.raises(ValueError):
        parse(["5.0", "5"])

    assert parse(["0", "1.5"]) == (0, 1.5)

    parse = make_parser(t.Tuple[bool, bool, bool])
    assert parse(["true", "True", "1"]) == (True, True, True)

    parse = make_parser(t.Tuple[t.Tuple[int, ...]])
    assert parse(["0", "1", "2"]) == ((0, 1, 2),)


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_for_fixed_length_tuple() -> None:
    """Test make_parser on fixed-length tuple types."""
    parse = make_parser(tuple[int, float])  # type: ignore
    result = parse(["5", "5"])
    assert isinstance(result, tuple)
    assert isinstance(result[0], int)
    assert isinstance(result[1], float)
    assert result == (5, 5.0)

    with pytest.raises(ValueError):
        parse([])
    with pytest.raises(ValueError):
        parse([""])
    with pytest.raises(ValueError):
        parse(["5"])
    with pytest.raises(ValueError):
        parse(["5.0", "5"])

    assert parse(["0", "1.5"]) == (0, 1.5)

    parse = make_parser(tuple[bool, bool, bool])  # type: ignore
    assert parse(["true", "True", "1"]) == (True, True, True)

    parse = make_parser(tuple[tuple[int, ...]])  # type: ignore
    assert parse(["0", "1", "2"]) == ((0, 1, 2),)


def test_make_parser_for_variable_length_typing_tuple() -> None:
    """Test make_parser on variable-length Tuple types."""
    parse = make_parser(t.Tuple[float, ...])

    assert parse([]) == ()
    with pytest.raises(ValueError):
        parse([""])

    result = parse(["0.0", "1.1", "2.2", "3.3"])
    assert isinstance(result, tuple)
    assert all(isinstance(r, float) for r in result)
    assert result == (0.0, 1.1, 2.2, 3.3)

    parse = make_parser(t.Tuple[int, ...])
    assert parse(["1", "2", "3"]) == (1, 2, 3)
    with pytest.raises(ValueError):
        parse(["1", "2", "3", "four"])

    parse = make_parser(t.Tuple[t.Tuple[int, float], ...])
    assert parse(["1", "2", "3", "4"]) == ((1, 2.0), (3, 4.0))
    with pytest.raises(ValueError):
        parse(["1", "2", "3"])


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_for_variable_length_tuple() -> None:
    """Test make_parser on variable-length tuple types."""
    parse = make_parser(tuple[float, ...])  # type: ignore

    assert parse([]) == ()
    with pytest.raises(ValueError):
        parse([""])

    result = parse(["0.0", "1.1", "2.2", "3.3"])
    assert isinstance(result, tuple)
    assert all(isinstance(r, float) for r in result)
    assert result == (0.0, 1.1, 2.2, 3.3)

    parse = make_parser(tuple[int, ...])  # type: ignore
    assert parse(["1", "2", "3"]) == (1, 2, 3)
    with pytest.raises(ValueError):
        parse(["1", "2", "3", "four"])

    parse = make_parser(tuple[tuple[int, float], ...])  # type: ignore
    assert parse(["1", "2", "3", "4"]) == ((1, 2.0), (3, 4.0))
    with pytest.raises(ValueError):
        parse(["1", "2", "3"])

    with pytest.raises(TypeError):
        make_parser(tuple[...])  # type: ignore
    with pytest.raises(TypeError):
        make_parser(tuple[..., int])  # type: ignore
    with pytest.raises(TypeError):
        make_parser(tuple[int, float, ...])  # type: ignore


def test_make_parser_for_typing_list() -> None:
    """Test make_parser(List[...])."""
    with pytest.raises(TypeError):
        make_parser(t.List[t.List[int]])
    with pytest.raises(TypeError):
        make_parser(t.List[t.Tuple[int, ...]])

    parse = make_parser(t.List[int])
    assert parse([]) == []
    result = parse(["1", "2", "3"])
    assert all(isinstance(r, int) for r in result)
    assert result == [1, 2, 3]

    with pytest.raises(ValueError):
        parse([""])

    parse = make_parser(t.List[t.Tuple[str, int]])
    assert parse(["foo", "1", "bar", "2"]) == [("foo", 1), ("bar", 2)]
    assert parse([]) == []

    with pytest.raises(ValueError):
        parse(["foo"])
    with pytest.raises(ValueError):
        parse(["foo", "1", "bar"])
    with pytest.raises(ValueError):
        parse(["foo", "bar"])


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_for_list() -> None:
    """Test make_parser(list[...])."""
    with pytest.raises(TypeError):
        make_parser(list[list[int]])  # type: ignore
    with pytest.raises(TypeError):
        make_parser(list[tuple[int, ...]])  # type: ignore
    with pytest.raises(TypeError):
        make_parser(list[int, bool])  # type: ignore
    with pytest.raises(TypeError):
        make_parser(list[...])  # type: ignore

    parse = make_parser(list[int])  # type: ignore
    assert parse([]) == []
    result = parse(["1", "2", "3"])
    assert all(isinstance(r, int) for r in result)
    assert result == [1, 2, 3]

    with pytest.raises(ValueError):
        parse([""])

    parse = make_parser(list[tuple[str, int]])  # type: ignore
    assert parse(["foo", "1", "bar", "2"]) == [("foo", 1), ("bar", 2)]
    assert parse([]) == []

    with pytest.raises(ValueError):
        parse(["foo"])
    with pytest.raises(ValueError):
        parse(["foo", "1", "bar"])
    with pytest.raises(ValueError):
        parse(["foo", "bar"])


def test_make_parser_for_typing_dict() -> None:
    """Test make_parser(Dict[...])."""
    parse = make_parser(t.Dict[str, float])
    result = parse(["foo", "1.0", "bar", "2.0"])
    assert result == {"foo": 1.0, "bar": 2.0}

    parse = make_parser(t.Dict[int, int])
    assert parse([]) == {}
    assert parse(["1", "2", "3", "4"]) == {1: 2, 3: 4}
    with pytest.raises(ValueError):
        parse(["1", "2", "3"])
    with pytest.raises(ValueError):
        parse(["", ""])
    with pytest.raises(ValueError):
        parse(["1", "2", "3", "foo"])

    with pytest.raises(TypeError):
        make_parser(t.Dict[int, t.List[int]])


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_for_dict() -> None:
    """Test make_parser(dict[...])."""
    parse = make_parser(dict[str, float])  # type: ignore
    result = parse(["foo", "1.0", "bar", "2.0"])
    assert result == {"foo": 1.0, "bar": 2.0}

    parse = make_parser(dict[int, int])  # type: ignore
    assert parse([]) == {}
    assert parse(["1", "2", "3", "4"]) == {1: 2, 3: 4}
    with pytest.raises(ValueError):
        parse(["1", "2", "3"])
    with pytest.raises(ValueError):
        parse(["", ""])
    with pytest.raises(ValueError):
        parse(["1", "2", "3", "foo"])

    unsupported = [
        dict[bool],  # type: ignore
        dict[int, ...],  # type: ignore
        dict[int, list[int]],  # type: ignore
        dict[str, str, str],  # type: ignore
    ]
    for type_ in unsupported:
        with pytest.raises(TypeError):
            make_parser(type_)


def test_make_parser_for_unsupported_type() -> None:
    """make_parser should throw UnsupportedType on unsupported types."""
    unsupported = [
        ...,
        t.List[t.List[int]],
        t.Tuple[t.List[int], int],
        t.Any,
        t.Callable[..., t.Any],
        getattr(t, "Literal")[0, 1, 2],
    ]
    for type_ in unsupported:
        with pytest.raises(TypeError):
            make_parser(type_)


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_for_unsupported_type_with_generic_aliases() -> None:
    """make_parser should throw UnsupportedType on unsupported types."""
    unsupported = [
        list[list[int]],  # type: ignore
        tuple[list[int], int],  # type: ignore
    ]
    for type_ in unsupported:
        with pytest.raises(TypeError):
            make_parser(type_)


def test_make_parser_for_nested_type() -> None:
    """Test make_parser on nested types."""
    supported = [
        t.List[int],
        t.Dict[t.Tuple[str, int], t.Tuple[str, t.Tuple[int, float]]],
        t.Tuple[int, t.Dict[str, str]],
        t.Tuple[str, ...],
        t.Tuple[t.Tuple[t.Tuple[str, int]], t.List[int]],
    ]
    for type_ in supported:
        make_parser(type_)

    unsupported = [
        t.List[t.List[int]],
        t.List[getattr(t, "Literal")[0]],  # type: ignore
        t.Dict[t.Tuple[str, ...], t.Tuple[int]],
        t.Callable[..., int],
        getattr(t, "Literal")[True, False],
        t.Tuple[t.Dict[str, str], int],
        t.Tuple[t.Tuple[int, ...], ...],
    ]
    for type_ in unsupported:
        with pytest.raises(TypeError):
            make_parser(type_)


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_for_nested_type_with_generic_aliases() -> None:
    """Test make_parser on nested types with generic aliases."""
    supported = [
        list[int],  # type: ignore
        dict[tuple[str, int], tuple[str, tuple[int, float]]],  # type: ignore
        tuple[int, dict[str, str]],  # type: ignore
        tuple[str, ...],  # type: ignore
        tuple[tuple[tuple[str, int]], list[int]],  # type: ignore
    ]
    for type_ in supported:
        make_parser(type_)

    invalid = [
        list[int, float],  # type: ignore
        tuple[...],  # type: ignore
        tuple[str, str, ...],  # type: ignore
    ]
    unsupported = [
        list[list[int]],  # type: ignore
        list[getattr(t, "Literal")[0]],  # type: ignore
        dict[tuple[str, ...], tuple[int]],  # type: ignore
        tuple[dict[str, str], int],  # type: ignore
        tuple[tuple[int, ...], ...],  # type: ignore
    ]
    for type_ in invalid + unsupported:
        with pytest.raises(TypeError):
            make_parser(type_)


def test_make_parser_length() -> None:
    """Test make_parser result.length."""
    cases = {
        bool: 1,
        t.Dict[t.Tuple[int, str], str]: "*",
        int: 1,
        t.List[str]: "*",
        t.Tuple[str, str, str]: 3,
        t.Optional[t.Tuple[int, float]]: "*",
        t.Tuple[int, ...]: "*",
        t.Tuple[int, str, float]: 3,
        t.Tuple[int, t.Tuple[int, t.Tuple[int, int]]]: 4,
    }
    for type_, expected in cases.items():
        assert make_parser(type_).length == expected


@pytest.mark.skipif(not has_version(3, 8), reason="No t.Final")
def test_make_parser_length_of_final() -> None:
    """Test make_parser result.length of final."""
    final = getattr(t, "Final")
    assert make_parser(final[t.List[int]]).length == "*"
    assert make_parser(final[t.Dict[str, int]]).length == "*"
    assert make_parser(final[t.Tuple[t.Tuple[str, int]]]).length == 2


@pytest.mark.skipif(not has_version(3, 9), reason="No generic aliases")
def test_make_parser_length_of_generic_aliases() -> None:
    """Test make_parser result.length of generic aliases."""
    cases = {
        dict[tuple[int, str], str]: "*",  # type: ignore
        list[str]: "*",  # type: ignore
        getattr(t, "Annotated")[tuple[str, str, str], None]: 3,  # type: ignore
        getattr(t, "Final")[list[int]]: "*",  # type: ignore
        t.Optional[tuple[int, float]]: "*",  # type: ignore
        tuple[int, ...]: "*",  # type: ignore
        tuple[int, str, float]: 3,  # type: ignore
        tuple[int, tuple[int, tuple[int, int]]]: 4,  # type: ignore
    }
    for type_, expected in cases.items():
        assert make_parser(type_).length == expected
