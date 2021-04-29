import pytest
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler, fake_binop_cls, fake_unop_cls):
    element = lambda a, b: None
    compiler.spec.register_element(
        "fake_element", {"setter": element, "getter": element}
    )
    compiler.spec.register_element(
        "fake_build_last", {"setter": element, "getter": element, "build_last": True},
    )
    analysis = lambda a: None
    compiler.spec.register_analysis(
        "fake_analysis", {"setter": analysis, "getter": analysis}
    )
    compiler.spec.binary_operators["+"] = lambda a, b: fake_binop_cls("+", a, b)
    compiler.spec.binary_operators["-"] = lambda a, b: fake_binop_cls("-", a, b)
    compiler.spec.unary_operators["-"] = lambda a: fake_unop_cls("-", a)

    return compiler


@pytest.mark.parametrize(
    "script,expected",
    (
        pytest.param(
            # el2 is a dependency to el1.
            dedent_multiline(
                """
                fake_element el1 &el2.a
                fake_element el2
                """
            ),
            [".script.1", ".script.0"],
            id="dependency to another element",
        ),
        pytest.param(
            # el1 is a dependency to el2. el2 also contains a self-reference but this edge is not
            # added to the graph and is instead stored separately.
            dedent_multiline(
                """
                fake_element el1 1 2
                fake_element el2 &el1.a 1-&el2.a
                """
            ),
            [".script.0", ".script.1"],
            id="dependency to another element and self",
        ),
        pytest.param(
            # The nested analysis should not appear in the dependency graph.
            dedent_multiline(
                """
                fake_analysis(fake_analysis())
                """
            ),
            [".script.0"],
            id="nested dependency",
        ),
        pytest.param(
            dedent_multiline(
                """
                fake_analysis(param=-5000+&el1.a)
                fake_element el1 1e5
                """
            ),
            [".script.1", ".script.0"],
            id="nested expression with dependency",
        ),
        pytest.param(
            dedent_multiline(
                """
                fake_build_last el1
                fake_element el2 1e5
                """
            ),
            [".script.1", ".script.0"],
            id="directive with `build_last` flag",
        ),
    ),
)
def test_build_order(compiler, script, expected):
    compiler.compile(script)
    build_order = sorted(
        compiler.graph.dependent_argument_nodes(compiler.graph.ROOT_NODE_NAME),
        key=compiler.graph.argument_node_order,
    )
    assert build_order == expected
