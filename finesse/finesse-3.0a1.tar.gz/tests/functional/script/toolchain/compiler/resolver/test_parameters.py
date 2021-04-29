import pytest
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler):
    element = lambda a=None, b=None, c=None, d=None: None
    compiler.spec.register_element(
        "fake_element1", {"setter": element, "getter": element}
    )
    compiler.spec.register_element(
        "fake_element2", {"setter": element, "getter": element}
    )
    compiler.spec.constants = {"A": 1, "B": "2", "C": object, "D": lambda: "hi"}
    compiler.spec.keywords = {"E", "F", "G", "H"}

    return compiler


@pytest.mark.parametrize(
    "script,graph_definition",
    (
        pytest.param(
            dedent_multiline(
                """
                fake_element1 myelement1
                fake_element2 myelement2 myelement1.a
                """
            ),
            dedent_multiline(
                """
                graph [
                    directed 1
                    node [
                        id 0
                        label ".script"
                        type "ROOT"
                        extra_tokens "['\\n']"
                    ]
                    node [
                        id 1
                        label ".script.0"
                        type "ELEMENT"
                        token "'fake_element1'"
                        name_token "'myelement1'"
                        extra_tokens "[' ']"
                    ]
                    node [
                        id 2
                        label ".script.1"
                        type "ELEMENT"
                        token "'fake_element2'"
                        name_token "'myelement2'"
                        extra_tokens "[' ', ' ']"
                    ]
                    node [
                        id 3
                        label ".script.1.0"
                        token "'myelement1.a'"
                        type "PARAMETER"
                    ]
                    edge [
                        source 1
                        target 0
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 2
                        target 0
                        type "ARGUMENT"
                        order "1"
                    ]
                    edge [
                        source 3
                        target 2
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 1
                        target 3
                        type "DEPENDENCY"
                    ]
                ]
                """
            ),
            id="parameter between two elements",
        ),
    ),
)
def test_parameter(assert_graphs_match, script, graph_definition):
    assert_graphs_match(script, graph_definition)


@pytest.mark.parametrize(
    "script,graph_definition",
    (
        pytest.param(
            dedent_multiline(
                """
                fake_element1 myelement1
                fake_element2 myelement2 &myelement1.a
                """
            ),
            dedent_multiline(
                """
                graph [
                    directed 1
                    node [
                        id 0
                        label ".script"
                        type "ROOT"
                        extra_tokens "['\\n']"
                    ]
                    node [
                        id 1
                        label ".script.0"
                        type "ELEMENT"
                        token "'fake_element1'"
                        name_token "'myelement1'"
                        extra_tokens "[' ']"
                    ]
                    node [
                        id 2
                        label ".script.1"
                        type "ELEMENT"
                        token "'fake_element2'"
                        name_token "'myelement2'"
                        extra_tokens "[' ', ' ']"
                    ]
                    node [
                        id 3
                        label ".script.1.0"
                        token "'&myelement1.a'"
                        type "PARAMETER_REFERENCE"
                    ]
                    edge [
                        source 1
                        target 0
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 2
                        target 0
                        type "ARGUMENT"
                        order "1"
                    ]
                    edge [
                        source 3
                        target 2
                        type "ARGUMENT"
                        order "0"
                    ]
                    edge [
                        source 1
                        target 3
                        type "DEPENDENCY"
                    ]
                ]
                """
            ),
            id="parameter reference between two elements",
        ),
    ),
)
def test_parameter_reference(assert_graphs_match, script, graph_definition):
    assert_graphs_match(script, graph_definition)
