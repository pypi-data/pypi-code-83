import re
import pytest
from finesse.script.exceptions import KatScriptError


@pytest.fixture
def compiler(compiler):
    # Register an element.
    element = lambda a=None, b=None, c=None, d=None: None
    compiler.spec.register_element(
        "fake_element", {"setter": element, "getter": element}
    )
    return compiler


@pytest.mark.parametrize(
    "script,error",
    (
        pytest.param(
            "fake_element myelement a=1 a=2",
            (
                "\nline 1: duplicate arguments with key 'a'\n"
                "-->1: fake_element myelement a=1 a=2\n"
                "                             ^   ^"
            ),
            id="duplicate keyword argument",
        ),
        pytest.param(
            "fake_element myelement a=1 b=2 a=3",
            (
                "\nline 1: duplicate arguments with key 'a'\n"
                "-->1: fake_element myelement a=1 b=2 a=3\n"
                "                             ^       ^"
            ),
            id="duplicate keyword argument, out of order",
        ),
        pytest.param(
            "fake_element myelement a=1 b=2 a=3 b=4",
            (
                "\nline 1: duplicate arguments with keys 'a' and 'b'\n"
                "-->1: fake_element myelement a=1 b=2 a=3 b=4\n"
                "                             ^   ^   ^   ^"
            ),
            id="multiple duplicate keyword arguments",
        ),
    ),
)
def test_duplicate_argument_error(compiler, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(script)
