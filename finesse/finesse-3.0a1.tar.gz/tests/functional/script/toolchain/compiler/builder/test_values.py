"""Kat compiler toolchain value tests.

Note: it is preferable to test compiled kat script values in the `katparser` testing module since
this tests the end-user language constructs directly. In some cases it's however not easy to test a
particular aspect with the available kat script elements, commands, etc. and instead custom
constructs are required; in such cases the tests should go here.
"""

import pytest
import numpy as np
from finesse.symbols import OPERATORS, FUNCTIONS, Constant
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler, fake_element_cls, fake_element_noparam_cls):
    compiler.spec.register_element(
        "fake_element", {"setter": fake_element_cls, "getter": fake_element_cls}
    )
    compiler.spec.register_element(
        "fake_noparam",
        {"setter": fake_element_noparam_cls, "getter": fake_element_noparam_cls},
    )
    # Have to use real Finesse operator here because the builder matches against Finesse operations.
    compiler.spec.binary_operators["*"] = OPERATORS["__mul__"]
    compiler.spec.unary_operators["-"] = FUNCTIONS["neg"]
    return compiler


@pytest.mark.parametrize(
    "expression,expected",
    (
        ("2*[1, 2]", 2 * np.array([1, 2])),
        ("3.141*[1, 2, 3, 4, 5]", 3.141 * np.array([1, 2, 3, 4, 5])),
        ("-10*[[1], [2], [3]]", -10 * np.array([[1], [2], [3]])),
    ),
)
def test_eager_numerical_array(compiler, expression, expected):
    # NOTE: this uses a fake element with no model parameters because model parameters don't support
    # ndarray values.
    model = compiler.compile(f"fake_noparam myel1 {expression}")
    np.testing.assert_array_equal(model.myel1.a, expected)


def test_lazy_numerical_array(compiler):
    """Test reference inside array.

    These are lazily evaluated because they contain symbols.
    """
    model = compiler.compile(
        dedent_multiline(
            """
            fake_element myel1 a=1
            fake_noparam myel2 -2*[1, &myel1.a]
            """
        )
    )
    np.testing.assert_array_equal(
        model.myel2.a.eval(),
        np.array([-2, OPERATORS["__mul__"](Constant(-2), model.myel1.a.ref)]),
    )
