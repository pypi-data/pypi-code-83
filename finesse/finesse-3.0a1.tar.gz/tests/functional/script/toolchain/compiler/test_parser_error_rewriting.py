"""Test `reraise_in_spec_context` which rewrites parsing errors with more spec-specific
information."""

import re
import pytest
from finesse.script.exceptions import KatScriptError


@pytest.fixture
def compiler(compiler):
    element = lambda instance, a=None, b=None, c=None, d=None: None
    compiler.spec.register_element(
        "fake_element", {"setter": element, "getter": element}
    )
    cmd = lambda model, a, b: None
    compiler.spec.register_command(
        "fake_command", {"setter": cmd, "getter": cmd, "singular": True},
    )
    analysis = lambda instance, a: None
    compiler.spec.register_analysis(
        "fake_analysis", {"setter": analysis, "getter": analysis}
    )

    return compiler


@pytest.mark.parametrize(
    "script,error",
    (
        pytest.param(
            "fake_element myparam=1",
            "\nline 1: 'fake_element' should be written in the form 'fake_element a b c d'\n"
            "-->1: fake_element myparam=1\n"
            "      ^^^^^^^^^^^^",
            id="element-without-name",
        ),
        pytest.param(
            "fake_command 1",
            "\nline 1: 'fake_command' should be written in the form 'fake_command(a, b)'\n"
            "-->1: fake_command 1\n"
            "      ^^^^^^^^^^^^",
            id="command-without-opening-parenthesis-arg",
        ),
        pytest.param(
            "fake_command even 4",
            "\nline 1: 'fake_command' should be written in the form 'fake_command(a, b)'\n"
            "-->1: fake_command even 4\n"
            "      ^^^^^^^^^^^^",
            id="command-without-opening-parenthesis-args",
        ),
        pytest.param(
            "fake_command myparam=1",
            "\nline 1: 'fake_command' should be written in the form 'fake_command(a, b)'\n"
            "-->1: fake_command myparam=1\n"
            "      ^^^^^^^^^^^^",
            id="command-without-opening-parenthesis-kwarg",
        ),
        pytest.param(
            "fake_analysis myparam=1",
            "\nline 1: 'fake_analysis' should be written in the form 'fake_analysis(a)'\n"
            "-->1: fake_analysis myparam=1\n"
            "      ^^^^^^^^^^^^",
            id="analysis-without-opening-parenthesis",
        ),
        # Even though a name or '(' is missing, the earlier error is thrown.
        pytest.param(
            "__unregistered_directive__ myparam=1",
            "\nline 1: unknown element or function '__unregistered_directive__'\n"
            "-->1: __unregistered_directive__ myparam=1\n"
            "      ^^^^^^^^^^^^^^^^^^^^^^^^^^",
            id="unregistered-directive",
        ),
    ),
)
def test_directive_missing_name_or_parenthesis_syntax_error(compiler, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(script)
