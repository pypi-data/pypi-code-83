import pytest
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler, fake_binop_cls):
    element = lambda a=None, b=None, c=None, d=None: None
    compiler.spec.register_element(
        "fake_element", {"setter": element, "getter": element}
    )
    compiler.spec.binary_operators["+"] = lambda a, b: fake_binop_cls("+", a, b)
    return compiler


@pytest.mark.parametrize(
    "script,graph_definition",
    (
        pytest.param(
            "fake_element el1 1+2",
            dedent_multiline(
                """
                graph [
                    directed 1
                    node [
                        id 0
                        label ".script"
                        type "ROOT"
                        extra_tokens "[]"
                    ]
                    node [
                        id 1
                        label ".script.0"
                        token "'fake_element'"
                        name_token "'el1'"
                        type "ELEMENT"
                        extra_tokens "[' ', ' ']"
                    ]
                    node [
                        id 2
                        label ".script.0.0"
                        token "'+'"
                        type "EXPRESSION"
                    ]
                    node [
                        id 3
                        label ".script.0.0.0"
                        token "'1'"
                        type "VALUE"
                    ]
                    node [
                        id 4
                        label ".script.0.0.1"
                        token "'2'"
                        type "VALUE"
                    ]
                    edge [
                        source 1
                        target 0
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 2
                        target 1
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 3
                        target 2
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 4
                        target 2
                        type "ARGUMENT"
                        order "1"
                    ]
                ]
                """
            ),
            id="1+2",
        ),
        pytest.param(
            "fake_element el1 (1)",
            dedent_multiline(
                """
                graph [
                    directed 1
                    node [
                        id 0
                        label ".script"
                        type "ROOT"
                        extra_tokens "[]"
                    ]
                    node [
                        id 1
                        label ".script.0"
                        token "'fake_element'"
                        name_token "'el1'"
                        type "ELEMENT"
                        extra_tokens "[' ', ' ']"
                    ]
                    node [
                        id 2
                        label ".script.0.0"
                        type "GROUPED_EXPRESSION"
                        extra_tokens "['(', ')']"
                    ]
                    node [
                        id 3
                        label ".script.0.0.0"
                        token "'1'"
                        type "VALUE"
                    ]
                    edge [
                        source 1
                        target 0
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 2
                        target 1
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 3
                        target 2
                        type "ARGUMENT"
                        order "0"
                    ]
                ]
                """
            ),
            id="grouped expression",
        ),
    ),
)
def test_expression(assert_graphs_match, script, graph_definition):
    assert_graphs_match(script, graph_definition)
