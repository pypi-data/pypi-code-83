"""Kat file parser expression parsing fuzzing tests."""

from hypothesis import given, settings, note, assume
from ......util import recursive_expressions


# Some expressions produce errors that are hard to detect before evaluating, so we
# instead define some allowed failures.
ALLOWED_ERRORS = ["can't take floor of complex number.", "complex exponentiation"]


@given(value=recursive_expressions())
@settings(deadline=1000)  # See #292.
def test_expression_fuzzing(fuzz_value_parse_compare, value):
    note(f"Expression: {value}")

    try:
        # The str() method of Operation should be Python syntax compatible.
        expected = eval(str(value))
        fuzz_value_parse_compare(value, expected, exact=False)
    except ZeroDivisionError:
        # There are infinitely many zero division errors so we catch them before the
        # general catch-all exception below.
        assume(False)
    except Exception as e:
        if str(e) in ALLOWED_ERRORS:
            assume(False)
        else:
            raise
