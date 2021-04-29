import re
import pytest
from finesse.script.exceptions import KatScriptError


@pytest.mark.parametrize(
    "script,error",
    (
        (
            "fake_element el1 a=1 1 b=2",
            "\nline 1: positional argument follows keyword argument\n"
            "-->1: fake_element el1 a=1 1 b=2\n"
            "                           ^",
        ),
        (
            "fake_element el1 1 2 a=1 3",
            "\nline 1: positional argument follows keyword argument\n"
            "-->1: fake_element el1 1 2 a=1 3\n"
            "                               ^",
        ),
    ),
)
def test_positional_arg_after_keyword_arg_invalid(parser, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        parser.parse(script)


@pytest.mark.parametrize(
    "script,error",
    (
        (
            "fake_element el1 1 a=2 b=",
            "\nline 1: missing value\n"
            "-->1: fake_element el1 1 a=2 b=\n"
            "                              ^",
        ),
        (
            "fake_element el1 1 a= 2b=3",
            "\nline 1: missing value\n"
            "-->1: fake_element el1 1 a= 2b=3\n"
            "                          ^",
        ),
    ),
)
def test_hanging_equals_kwarg_invalid(parser, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        parser.parse(script)
