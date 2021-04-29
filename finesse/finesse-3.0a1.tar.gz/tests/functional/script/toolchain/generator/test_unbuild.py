import pytest
from finesse.symbols import OPERATORS, FUNCTIONS
from finesse.script.generator import ElementContainer
from ...util import dedent_multiline
from ..data import NONE, BOOLEANS, STRINGS, INTEGERS, FLOATS, IMAGINARIES, ARRAYS


@pytest.fixture
def unbuilder(
    unbuilder,
    fake_element_cls,
    fake_element_noparam_cls,
    fake_detector_cls,
    fake_analysis_cls,
):
    unbuilder.spec.register_element(
        ("fake_element",), {"setter": fake_element_cls, "getter": fake_element_cls}
    )
    unbuilder.spec.register_element(
        ("fake_noparam",),
        {"setter": fake_element_noparam_cls, "getter": fake_element_noparam_cls},
    )
    unbuilder.spec.register_element(
        ("fake_detector",), {"setter": fake_detector_cls, "getter": fake_detector_cls}
    )
    unbuilder.spec.register_analysis(
        ("fake_analysis",), {"setter": fake_analysis_cls, "getter": fake_analysis_cls}
    )
    unbuilder.spec.binary_operators["+"] = OPERATORS["__add__"]
    unbuilder.spec.binary_operators["-"] = OPERATORS["__sub__"]
    unbuilder.spec.unary_operators["+"] = FUNCTIONS["pos"]
    unbuilder.spec.unary_operators["-"] = FUNCTIONS["neg"]
    unbuilder.spec.expression_functions["sin"] = FUNCTIONS["sin"]
    unbuilder.spec.expression_functions["arctan2"] = FUNCTIONS["arctan2"]

    return unbuilder


@pytest.mark.parametrize(
    "_,expected,arg", NONE + BOOLEANS + STRINGS + INTEGERS + FLOATS + IMAGINARIES
)
def test_terminal_value(unbuilder, fake_element_noparam_cls, model, _, expected, arg):
    """Values like ints, floats, strings; those without additional dependencies."""
    script = unbuilder.unbuild(
        ElementContainer(fake_element_noparam_cls("myelement", arg))
    )
    assert script == f"fake_noparam myelement a={expected} b=none"


def test_reference(unbuilder, fake_element_cls, model):
    model.add(fake_element_cls("myel1"))
    model.add(fake_element_cls("myel2"))
    model.myel1.a = 1 - model.myel1.b.ref
    model.myel2.a = model.myel1.a.ref
    model.myel2.b = model.myel1.b.ref
    assert unbuilder.unbuild(model) == dedent_multiline(
        """
        fake_element myel1 a=(1-&myel1.b) b=none
        fake_element myel2 a=&myel1.a b=&myel1.b
        """
    )


@pytest.mark.parametrize(
    "function,expected",
    (
        (FUNCTIONS["neg"](1), "-1"),
        (FUNCTIONS["sin"](1), "sin(1)"),
        (FUNCTIONS["arctan2"](1, 2), "arctan2(1, 2)"),
    ),
)
def test_expression_function(unbuilder, fake_element_cls, model, function, expected):
    script = unbuilder.unbuild(ElementContainer(fake_element_cls("myel1", a=function)))
    assert script == f"fake_element myel1 a={expected} b=none"


@pytest.mark.parametrize("expected,array", ARRAYS)
def test_array(unbuilder, fake_element_noparam_cls, model, array, expected):
    script = unbuilder.unbuild(
        ElementContainer(fake_element_noparam_cls("myel1", a=array))
    )
    assert script == f"fake_noparam myel1 a={expected} b=none"


def test_port(unbuilder, fake_element_cls, fake_detector_cls, model):
    model.add(fake_element_cls("myel1"))
    model.add(fake_detector_cls("mydet1", target=model.myel1.p1))
    assert unbuilder.unbuild(model) == dedent_multiline(
        """
        fake_element myel1 a=none b=none
        fake_detector mydet1 target=myel1.p1
        """
    )


def test_node(unbuilder, fake_element_cls, fake_detector_cls, model):
    model.add(fake_element_cls("myel1"))
    model.add(fake_detector_cls("mydet1", target=model.myel1.p1.o))
    assert unbuilder.unbuild(model) == dedent_multiline(
        """
        fake_element myel1 a=none b=none
        fake_detector mydet1 target=myel1.p1.o
        """
    )


@pytest.mark.parametrize(
    "name,args,kwargs,expected",
    (
        ("myelement", [], {}, "fake_noparam myelement a=none b=none"),
        ("myelement", [None], {}, "fake_noparam myelement a=none b=none"),
        ("myelement", [None, None], {}, "fake_noparam myelement a=none b=none"),
        ("myelement", [None], {"b": None}, "fake_noparam myelement a=none b=none"),
        ("myelement", [], {"a": None}, "fake_noparam myelement a=none b=none"),
        ("myelement", [], {"b": None}, "fake_noparam myelement a=none b=none"),
        (
            "myelement",
            [],
            {"a": None, "b": None},
            "fake_noparam myelement a=none b=none",
        ),
        ("myelement", [1], {}, "fake_noparam myelement a=1 b=none"),
        ("myelement", [1, 2], {}, "fake_noparam myelement a=1 b=2"),
        ("myelement", [], {"a": 1}, "fake_noparam myelement a=1 b=none"),
        ("myelement", [], {"a": 1, "b": 2}, "fake_noparam myelement a=1 b=2"),
    ),
)
def test_element(
    unbuilder, fake_element_noparam_cls, model, name, args, kwargs, expected
):
    script = unbuilder.unbuild(
        ElementContainer(fake_element_noparam_cls(name, *args, **kwargs))
    )
    assert script == expected


@pytest.mark.parametrize(
    "args,kwargs,expected",
    (
        ([], {}, "fake_analysis(a=none, b=none)"),
        ([None], {}, "fake_analysis(a=none, b=none)"),
        ([None, None], {}, "fake_analysis(a=none, b=none)"),
        ([None], {"b": None}, "fake_analysis(a=none, b=none)"),
        ([], {"a": None}, "fake_analysis(a=none, b=none)"),
        ([], {"b": None}, "fake_analysis(a=none, b=none)"),
        ([], {"a": None, "b": None}, "fake_analysis(a=none, b=none)"),
        ([1], {}, "fake_analysis(a=1, b=none)"),
        ([1, 2], {}, "fake_analysis(a=1, b=2)"),
        ([], {"a": 1}, "fake_analysis(a=1, b=none)"),
        ([], {"a": 1, "b": 2}, "fake_analysis(a=1, b=2)"),
    ),
)
def test_analysis(unbuilder, fake_analysis_cls, model, args, kwargs, expected):
    script = unbuilder.unbuild(fake_analysis_cls(*args, **kwargs))
    assert script == expected
