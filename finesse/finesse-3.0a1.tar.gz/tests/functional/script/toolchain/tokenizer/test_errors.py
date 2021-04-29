"""Tests for the tokenizer without any normalization."""

import re
import pytest
from finesse.script.exceptions import KatScriptError


@pytest.mark.parametrize(
    "string,error",
    (
        ("[", ("\nline 1: unclosed '['\n" "-->1: [\n" "      ^")),
        ("(", ("\nline 1: unclosed '('\n" "-->1: (\n" "      ^")),
        ("]", ("\nline 1: extraneous ']'\n" "-->1: ]\n" "      ^")),
        (")", ("\nline 1: extraneous ')'\n" "-->1: )\n" "      ^")),
    ),
)
def test_invalid_delimiter_nesting(tokenizer, string, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        list(tokenizer.tokenize(string))
