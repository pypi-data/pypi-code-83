"""Data for use in tests.

Most data contains tuples with 3 values: the input (parsed) string, the output (generated) string
and the Python representation. This allows the same data to be used for both parser and generator
tests.
"""


SI_PREFICES = {
    # Taken from lexer NUMBER tokeniser.
    "p": -12,
    "n": -9,
    "u": -6,
    "m": -3,
    "k": 3,
    "M": 6,
    "G": 9,
    "T": 12,
}


NONE = (("none", "none", None),)


BOOLEANS = (
    ("false", "false", False),
    ("true", "true", True),
)


STRINGS = (
    # Single quotes.
    (r"'my string'", "'my string'", "my string"),
    (r"' my string'", "' my string'", " my string"),
    (r"'  my   string  '", "'  my   string  '", "  my   string  "),
    (r"'\"my string'", "'\"my string'", '"my string'),
    (r"'\"\"my \'string'", r"""'""my \'string'""", '""my \'string'),
    # Double quotes.
    (r'"my string"', "'my string'", "my string"),
    (r'" my string"', "' my string'", " my string"),
    (r'"  my   string  "', "'  my   string  '", "  my   string  "),
    (r'"\"my string"', "'\"my string'", '"my string'),
    (r'"\"\"my \'string"', r"""'""my \'string'""", '""my \'string'),
)


# No signs allowed!
INTEGERS = (
    ("0", "0", 0),
    ("50505", "50505", 50505),
    ("123141242151251616110", "123141242151251616110", 123141242151251616110),
)


# No signs allowed!
FLOATS_STD = (
    ("0.0", "0.0", 0.0),
    ("15.151", "15.151", 15.151),
)
FLOATS_SCIENTIFIC = (
    ("0.e7", "0.0", 0e7),
    ("0.0e7", "0.0", 0e7),
    ("1.23e7", "12300000.0", 1.23e7),
    ("1.23e+7", "12300000.0", 1.23e7),
    ("1.23e-7", "1.23e-07", 1.23e-7),
)
FLOATS_INF = (("inf", "inf", float("inf")),)
FLOATS = (*FLOATS_STD, *FLOATS_SCIENTIFIC, *FLOATS_INF)


# No signs allowed!
# NOTE: the middle (generator) forms may seem counter-intuitive in places but match that of Python's
# repr() for complex numbers.
IMAGINARIES = (
    ("0j", "0j", 0j),
    ("0.j", "0j", 0.0j),
    ("0.0j", "0j", 0.0j),
    ("10j", "10j", 10j),
    ("1.32j", "1.32j", 1.32j),
    # Scientific.
    ("0e7j", "0j", 0e7j),
    ("0.e7j", "0j", 0.0e7j),
    ("0.0e7j", "0j", 0.0e7j),
    ("1.23e7j", "12300000j", 1.23e7j),
    ("1.23e+7j", "12300000j", 1.23e7j),
    ("1.23e-7j", "1.23e-07j", 1.23e-7j),
    # Infinities.
    ("infj", "infj", complex("infj")),
)


ARRAYS = (
    ("[]", []),
    ("[[]]", [[]]),
    ("[[[]]]", [[[]]]),
    ("[1]", [1]),
    ("[[1]]", [[1]]),
    ("[[[1]]]", [[[1]]]),
    ("[1, 2]", [1, 2]),
    ("[[1], 2]", [[1], 2]),
    ("[[[1], 2], 3]", [[[1], 2], 3]),
    (
        "[1, 2, [3, 4], [5, 6, [7, 8, [9, 10, [11]]]]]",
        [1, 2, [3, 4], [5, 6, [7, 8, [9, 10, [11]]]]],
    ),
    ("[[[1, 2]], [[3, 4]]]", [[[1, 2]], [[3, 4]]]),
)
