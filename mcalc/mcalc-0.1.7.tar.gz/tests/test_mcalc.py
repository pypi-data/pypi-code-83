import pytest
from hypothesis import given, assume, strategies as st

from mcalc.calc import Calculator


@given(
    st.floats(min_value=-10000, max_value=10000),
    st.floats(min_value=-10000, max_value=10000),
)
def test_add(x, y):
    calc = Calculator(x)
    assert calc.add(y) == sum([x, y])


@given(
    st.floats(min_value=-10000, max_value=10000),
    st.floats(min_value=-10000, max_value=10000),
)
def test_subtract(x, y):
    calc = Calculator(x)
    assert calc.subtract(y) == x - y


@given(
    st.floats(min_value=-10000, max_value=10000),
    st.floats(min_value=-10000, max_value=10000),
)
def test_multiply(x, y):
    calc = Calculator(x)
    assert calc.multiply(y) == x * y


@given(
    st.floats(min_value=-10000, max_value=10000),
    st.floats(min_value=-10000, max_value=10000),
)
def test_divide(x, y):
    assume(abs(y)) > 0.001
    calc = Calculator(x)
    assert calc.divide(y) == x / y


@given(
    st.floats(min_value=-10000, max_value=10000),
    st.floats(min_value=-10000, max_value=10000),
)
def test_n_root(x, y):
    assume(abs(x)) > 0.001
    assume(abs(y)) > 0.01
    calc = Calculator(x)
    if x < 0:
        with pytest.raises(NotImplementedError):
            calc.n_root(y) == x ** (1 / y)
    else:
        assert calc.n_root(y) == x ** (1 / y)


@given(
    st.floats(min_value=-1000000, max_value=1000000),
)
def test_init(x):
    assert Calculator(x).get_memory() == x


@given(
    st.floats(min_value=-1000000, max_value=1000000),
)
def test_reset(x):
    assert Calculator(x).reset() == 0.0
    assert Calculator().reset(x) == x
