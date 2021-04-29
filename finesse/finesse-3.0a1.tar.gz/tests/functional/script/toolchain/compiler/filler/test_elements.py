import pytest
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler):
    element = lambda a=None, b=None, c=None, d=None: None
    compiler.spec.register_element(
        "fake_element", {"setter": element, "getter": element}
    )
    return compiler


@pytest.mark.parametrize(
    "script,graph_definition",
    (
        pytest.param(
            # Element with no arguments.
            "fake_element myelement",
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
                        name_token "'myelement'"
                        type "ELEMENT"
                        extra_tokens "[' ']"
                    ]
                    edge [
                        source 1
                        target 0
                        type "ARGUMENT"
                        order "0"
                    ]
                ]
                """
            ),
            id="element with no arguments",
        ),
        pytest.param(
            "fake_element myelement 1 2 c=3 d=4",
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
                        name_token "'myelement'"
                        type "ELEMENT"
                        extra_tokens "[' ', ' ', ' ', ' ', ' ']"
                    ]
                    node [
                        id 2
                        label ".script.0.0"
                        token "'1'"
                        type "VALUE"
                    ]
                    node [
                        id 3
                        label ".script.0.1"
                        token "'2'"
                        type "VALUE"
                    ]
                    node [
                        id 4
                        label ".script.0.2"
                        token "'3'"
                        key_token "'c'"
                        extra_tokens "['=']"
                        type "VALUE"
                    ]
                    node [
                        id 5
                        label ".script.0.3"
                        token "'4'"
                        key_token "'d'"
                        extra_tokens "['=']"
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
            id="element with arguments",
        ),
        pytest.param(
            dedent_multiline(
                """
                fake_element myelement1
                fake_element myelement2
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
                        token "'fake_element'"
                        name_token "'myelement1'"
                        type "ELEMENT"
                        extra_tokens "[' ']"
                    ]
                    node [
                        id 2
                        label ".script.1"
                        token "'fake_element'"
                        name_token "'myelement2'"
                        type "ELEMENT"
                        extra_tokens "[' ']"
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
                ]
                """
            ),
            id="multiple elements",
        ),
    ),
)
def test_element(assert_graphs_match, script, graph_definition):
    assert_graphs_match(script, graph_definition)
