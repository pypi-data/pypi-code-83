import pytest
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler):
    element = lambda a=None, b=None, c=None, d=None: None
    compiler.spec.register_element(
        "fake_element", {"setter": element, "getter": element}
    )
    compiler.spec.keywords = {"E", "F", "G", "H"}
    return compiler


@pytest.mark.parametrize(
    "script,graph_definition",
    (
        pytest.param(
            "fake_element myelement E F G H",
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
                        type "ELEMENT"
                        token "'fake_element'"
                        name_token "'myelement'"
                        extra_tokens "[' ', ' ', ' ', ' ', ' ']"
                    ]
                    node [
                        id 2
                        label ".script.0.0"
                        token "'E'"
                        type "KEYWORD"
                    ]
                    node [
                        id 3
                        label ".script.0.1"
                        token "'F'"
                        type "KEYWORD"
                    ]
                    node [
                        id 4
                        label ".script.0.2"
                        token "'G'"
                        type "KEYWORD"
                    ]
                    node [
                        id 5
                        label ".script.0.3"
                        token "'H'"
                        type "KEYWORD"
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
                        target 1
                        type "ARGUMENT"
                        order "1"
                    ]
                    edge [
                        source 4
                        target 1
                        type "ARGUMENT"
                        order "2"
                    ]
                    edge [
                        source 5
                        target 1
                        type "ARGUMENT"
                        order "3"
                    ]
                ]
                """
            ),
            id="element with 4 keywords",
        ),
    ),
)
def test_keywords(assert_graphs_match, script, graph_definition):
    assert_graphs_match(script, graph_definition)
