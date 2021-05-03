from hypothesis import HealthCheck, given, settings
from hypothesis.strategies import integers, lists
from pytest import LogCaptureFixture, mark, raises

from assertion import Assertion
from assertion.deferred_info import DeferredInfo

a = Assertion(exception=ZeroDivisionError)


def test_defer_info():
    def_info = DeferredInfo(ZeroDivisionError, "fail_info", "message")

    for t in [str, repr]:
        assert "fail_info" in t(def_info)
        assert "message" in t(def_info)
        assert ZeroDivisionError.__name__ in t(def_info)


@given(n_fails=integers(1, 7))
def test_single_context_manager(n_fails):
    with raises(ZeroDivisionError) as exc:
        with a.deferring_context():
            for _ in range(n_fails):
                a.true(False)

    assert f"{n_fails} deferred exception" in str(exc.value)


@given(n_fails_a=integers(1, 7), n_fails_b=integers(0, 7))
def test_multiple_context_manager(n_fails_a, n_fails_b):
    with raises(ZeroDivisionError) as exc:
        with a.deferring_context():
            for i in range(n_fails_a):
                a.less_or_equal(i, -99, exception=ValueError)

            assert a.defer_level == 1

            with a.deferring_context():
                for i in range(n_fails_b):
                    a.equal(i, -99)

                assert a.defer_level == 2
            assert a.defer_level == 1

    assert type(exc.value) == ZeroDivisionError
    assert f"{n_fails_a+n_fails_b} deferred exception" in str(exc.value)


@given(n_fails=integers(0, 3))
def test_sync_decorator(n_fails):
    @a.deferring_decorator
    def potentially_failing():
        for _ in range(n_fails):
            a.false(True, msg="D'oh!")

        return 5

    if n_fails == 0:
        assert potentially_failing() == 5
    else:
        with raises(ZeroDivisionError) as exc:
            potentially_failing()

        assert f"{n_fails} deferred exception" in str(exc.value)
        assert "D'oh!" in str(exc.value)


@mark.asyncio
@given(n_fails=integers(0, 3))
async def test_async_decorator(n_fails):
    @a.deferring_decorator
    async def potentially_failing():
        for _ in range(n_fails):
            await a.false(True)

        return 5

    if n_fails == 0:
        assert await potentially_failing() == 5
    else:
        with raises(ZeroDivisionError) as exc:
            await potentially_failing()

        assert f"{n_fails} deferred exception" in str(exc.value)


@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@given(n_fails_per_level=lists(integers(0, 2), min_size=1, max_size=5))
def test_explicit_balanced(n_fails_per_level, caplog: LogCaptureFixture):
    caplog.clear()
    b = Assertion(exception=ZeroDivisionError)

    for n_fails in n_fails_per_level:
        b.start_deferring()

        for i in range(n_fails):
            b.greater_or_equal(-99, i)

    for i, n_fails in enumerate(n_fails_per_level):
        if i < len(n_fails_per_level) - 1 or sum(n_fails_per_level) == 0:
            b.stop_deferring()
        else:
            with raises(ZeroDivisionError) as exc:
                b.stop_deferring()
            assert f"{sum(n_fails_per_level)} deferred exception" in str(exc.value)

    del b
    assert caplog.text == ""


@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@given(
    n_fails_per_level=lists(integers(0, 2), min_size=1, max_size=5),
    n_missing_stops=integers(0, 5),
)
def test_explicit_missing_stops(
    n_fails_per_level, n_missing_stops, caplog: LogCaptureFixture
):
    caplog.clear()

    def potentially_unbalanced():
        b = Assertion(exception=ZeroDivisionError)

        for n_fails in n_fails_per_level:
            b.start_deferring()

            for i in range(n_fails):
                b.greater_or_equal(-99, i)

        for _ in range(len(n_fails_per_level) - n_missing_stops):
            b.stop_deferring()

        del b

    if sum(n_fails_per_level) == 0:
        potentially_unbalanced()
    else:
        if n_missing_stops == 0:
            with raises(ZeroDivisionError) as exc:
                potentially_unbalanced()
            assert f"{sum(n_fails_per_level)} deferred exception" in str(exc.value)
        else:
            potentially_unbalanced()
            assert f"{sum(n_fails_per_level)} deferred exception" in caplog.text

    if n_missing_stops > 0:
        assert "defer level not zero" in caplog.text
    else:
        assert caplog.text == ""


@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@given(
    n_fails_per_level=lists(integers(0, 2), min_size=1, max_size=5),
    n_additional_stops=integers(0, 2),
)
def test_explicit_additional_stops(
    n_fails_per_level, n_additional_stops, caplog: LogCaptureFixture
):
    caplog.clear()

    def potentially_unbalanced():
        b = Assertion(exception=ZeroDivisionError)

        for n_fails in n_fails_per_level:
            b.start_deferring()

            for i in range(n_fails):
                b.greater_or_equal(-99, i)

        for _ in range(len(n_fails_per_level) + n_additional_stops):
            b.stop_deferring()

        del b

    if sum(n_fails_per_level) == 0:
        potentially_unbalanced()

        if n_additional_stops > 0:
            assert "unmatched stop_deferring()" in caplog.text
        else:
            assert caplog.text == ""
    else:
        with raises(ZeroDivisionError) as exc:
            potentially_unbalanced()
        assert f"{sum(n_fails_per_level)} deferred exception" in str(exc.value)
