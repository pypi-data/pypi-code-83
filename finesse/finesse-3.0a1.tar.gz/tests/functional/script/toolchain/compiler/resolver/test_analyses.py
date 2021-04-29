import re
import pytest
from finesse.script.exceptions import KatParsingError
from ....util import dedent_multiline


@pytest.fixture
def compiler(compiler):
    analysis = lambda a: None
    compiler.spec.register_analysis(
        "fake_analysis", {"setter": analysis, "getter": analysis}
    )
    return compiler


@pytest.mark.parametrize(
    "script,error",
    (
        pytest.param(
            dedent_multiline(
                """
                fake_analysis()
                fake_analysis()
                """
            ),
            "\nlines 1-2: duplicate analysis trees (combine with 'series' or 'parallel')\n"
            "-->1: fake_analysis()\n"
            "      ^^^^^^^^^^^^^\n"
            "-->2: fake_analysis()\n"
            "      ^^^^^^^^^^^^^",
            id="xaxis",
        ),
    ),
)
def test_multiple_analyses_invalid(compiler, script, error):
    with pytest.raises(KatParsingError, match=re.escape(error)):
        compiler.compile(script)
