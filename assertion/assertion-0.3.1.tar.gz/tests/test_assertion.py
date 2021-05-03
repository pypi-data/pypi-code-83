import logging
from functools import partial

from hypothesis import given, settings  # type: ignore
from hypothesis.strategies import integers, sampled_from, text  # type: ignore
from pytest import mark, raises  # type: ignore

from assertion import Assertion
from tests.conftest import (
    MutableBoolean,
    anything,
    builtin_exceptions,
    func_and_parameters,
    get_awaitable_with_fuse,
    get_func_with_fuse,
)

assertion = Assertion(timeout=10.0, msg_length_max=10_000)
no_wait = Assertion(msg_length_max=10_000)
short_wait = Assertion(timeout=2.0)


@given(
    exception=sampled_from(builtin_exceptions),
    max_msg_length=integers(min_value=10),
    fail_desc_length=integers(min_value=1, max_value=100),
)
def test_constructor(exception, max_msg_length, fail_desc_length):
    with raises(exception) as exc:
        bssert = Assertion(
            msg_length_max=max_msg_length, exception=exception, timeout=0
        )
        bssert.false("#" * fail_desc_length)
    assert len(str(exc.value)) == min(
        [fail_desc_length + len("'' != False"), max_msg_length]
    )


@given(
    a=anything,
    comp=sampled_from(
        [
            (no_wait.true, lambda a: bool(a)),
            (no_wait.false, lambda a: not bool(a)),
        ]
    ),
)
def test_one_parameter_asserts(a, comp):
    assert_func, test_func = comp

    if test_func(a):
        assert_func(a)
    else:
        with raises(AssertionError) as exc:
            assert_func(a)
        assert repr(a) in str(exc.value)


@given(
    a=anything,
    b=anything,
    comp=sampled_from(
        [
            (no_wait.equal, lambda a, b: a == b),
            (no_wait.not_equal, lambda a, b: a != b),
            (no_wait.less, lambda a, b: a < b),
            (no_wait.less_or_equal, lambda a, b: a <= b),
            (no_wait.greater, lambda a, b: a > b),
            (no_wait.greater_or_equal, lambda a, b: a >= b),
            (no_wait.in_, lambda a, b: a in b),
            (no_wait.not_in, lambda a, b: a not in b),
            (no_wait.is_, lambda a, b: a is b),
            (no_wait.is_not, lambda a, b: a is not b),
        ]
    ),
)
@settings(max_examples=2000)
def test_two_parameter_asserts(a, b, comp):
    assert_func, test_func = comp

    try:
        test_func(a, b)
    except TypeError:
        with raises(TypeError):
            assert_func(a, b)
    else:
        if test_func(a, b):
            assert_func(a, b)
        else:
            with raises(AssertionError) as exc:
                assert_func(a, b)
            assert repr(a) in str(exc.value)
            assert repr(b) in str(exc.value)


@given(msg=text())
def test_msg_kw(msg):
    with raises(AssertionError) as exc:
        no_wait.true(False, msg=msg)
    if msg:
        assert str(exc.value).startswith(msg + ": ")


@given(fap=func_and_parameters())
def test_funcs(fap):
    func, args = fap

    if func(*args):
        assertion.true(partial(func, *args))
        with raises(AssertionError):
            no_wait.false(partial(func, *args))
    else:
        assertion.false(partial(func, *args))
        with raises(AssertionError):
            no_wait.true(partial(func, *args))


@mark.asyncio
async def test_async_wait():
    with raises(AssertionError):
        await short_wait.true(get_awaitable_with_fuse(2.1))

    await short_wait.true(get_awaitable_with_fuse(1.9))


def test_sync_wait():
    with raises(AssertionError):
        short_wait.true(get_func_with_fuse(2.1))

    short_wait.true(get_func_with_fuse(1.9))


@mark.asyncio
async def test_redundant_await():
    for _ in range(3):
        await assertion.true(True)


@mark.asyncio
async def test_async_tester():
    async def func_async(v=42):
        return v

    await assertion.equal(func_async(42), lambda: 42)
    await assertion.equal(func_async, lambda: 42)


def test_sync_mutable_boolean():
    assertion.true(MutableBoolean(5))


@mark.asyncio
async def test_async_mutable_boolean():
    await assertion.true(MutableBoolean(5))


def test_sync_warning(caplog):
    caplog.set_level(logging.WARNING)

    # w/o warning
    with caplog.at_level(logging.WARNING):
        short_wait.true(get_func_with_fuse(0.5))
    assert caplog.text == ""

    # w/ warning
    with caplog.at_level(logging.WARNING):
        short_wait.true(get_func_with_fuse(1.5))
    assert "before success" in caplog.text


@mark.asyncio
async def test_async_warning(caplog):
    caplog.set_level(logging.WARNING)

    # w/o warning
    with caplog.at_level(logging.WARNING):
        await short_wait.true(get_awaitable_with_fuse(0.5))
    assert caplog.text == ""

    # w/ warning
    with caplog.at_level(logging.WARNING):
        await short_wait.true(get_awaitable_with_fuse(1.5))
    assert "before success" in caplog.text
