import re
import pytest
from finesse.script.exceptions import KatScriptError
from finesse.symbols import OPERATORS, FUNCTIONS


@pytest.fixture
def compiler(compiler, fake_element_cls, fake_binop_cls, fake_unop_cls):
    # Define a command setter with fixed positional arg requirements so we can test incorrect
    # arguments.
    command = lambda a, b, c, d: None

    def set_command(model, *args, **kwargs):
        command(*args, **kwargs)

    compiler.spec.register_element(
        "fake_element", {"setter": fake_element_cls, "getter": fake_element_cls}
    )
    compiler.spec.register_command(
        "fake_command",
        {"setter": set_command, "getter": lambda: None, "singular": True,},
    )
    # Have to use real Finesse operators here because the builder matches against Finesse
    # operations.
    compiler.spec.binary_operators["+"] = OPERATORS["__add__"]
    compiler.spec.unary_operators["-"] = FUNCTIONS["neg"]

    return compiler


@pytest.mark.parametrize(
    "value", ("1", "-1", "1+1", "(1+1)", "'string'", "none", "inf", "-inf", "1.5+2e5j"),
)
def test_invalid_keyword_argument(compiler, value):
    """Test keyword arguments that don't exist in the Python constructor cause an error.

    Error handler uses the parsed value object so we have to check different types of
    value.
    """
    error = (
        f"\nline 1: 'fake_element' got an unexpected keyword argument 'c' (expected syntax: fake_element name a=none b=none)\n"
        f"-->1: fake_element myelement c={value}\n"
        f"                             ^"
    )
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(f"fake_element myelement c={value}")


@pytest.mark.parametrize(
    "script,error",
    (
        (
            "fake_command()",
            "\nline 1: 'fake_command' missing 4 required positional arguments: 'a', 'b', 'c', and 'd'\n"
            "-->1: fake_command()\n"
            "      ^^^^^^^^^^^^",
        ),
        (
            "fake_command(1)",
            "\nline 1: 'fake_command' missing 3 required positional arguments: 'b', 'c', and 'd'\n"
            "-->1: fake_command(1)\n"
            "      ^^^^^^^^^^^^",
        ),
        (
            "fake_command(1, 2)",
            "\nline 1: 'fake_command' missing 2 required positional arguments: 'c' and 'd'\n"
            "-->1: fake_command(1, 2)\n"
            "      ^^^^^^^^^^^^",
        ),
        (
            "fake_command(1, 2, 3)",
            "\nline 1: 'fake_command' missing 1 required positional argument: 'd'\n"
            "-->1: fake_command(1, 2, 3)\n"
            "      ^^^^^^^^^^^^",
        ),
    ),
)
def test_not_enough_positional_arguments(compiler, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(script)


@pytest.mark.parametrize(
    "script,error",
    (
        (
            "fake_command(1, 2, 3, 4, 5)",
            "\nline 1: 'fake_command' takes 4 positional arguments but 5 were given\n"
            "-->1: fake_command(1, 2, 3, 4, 5)\n"
            "      ^^^^^^^^^^^^",
        ),
        (
            "fake_command(1, 2, 3, 4, 5, 6)",
            "\nline 1: 'fake_command' takes 4 positional arguments but 6 were given\n"
            "-->1: fake_command(1, 2, 3, 4, 5, 6)\n"
            "      ^^^^^^^^^^^^",
        ),
    ),
)
def test_too_many_positional_arguments(compiler, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(script)


@pytest.mark.parametrize(
    "script,error",
    (
        (
            "fake_command(1, 2, 3, 4, 5, 6, a=1)",
            "\nline 1: 'fake_command' got multiple values for argument 'a'\n"
            "-->1: fake_command(1, 2, 3, 4, 5, 6, a=1)\n"
            "      ^^^^^^^^^^^^",
        ),
    ),
)
def test_duplicate_keyword_arguments(compiler, script, error):
    with pytest.raises(KatScriptError, match=re.escape(error)):
        compiler.compile(script)
