"""Regular expressions for matching tokens of different types in kat script."""


def group(*choices):
    """Match any of the specified choices."""
    return f"({'|'.join(choices)})"


def any(*choices):
    """Specify that there should be zero or more of the specified choices."""
    return f"{group(*choices)}*"


def maybe(*choices):
    """Specify that there should be zero or one of the specified choices."""
    return f"{group(*choices)}?"


WHITESPACE = r"[ \f\t]+"
NEWLINE = r"\r?\n+"
COMMENT = r"#[^\r\n]*"
NONE = group(r"None", r"none")
BOOLEAN = group(r"True", r"true", r"False", r"false")
REFERENCE = r"&[a-zA-Z_][a-zA-Z0-9_.]*"  # Reference to element name or property.
NAME = r"[a-zA-Z_][a-zA-Z0-9_.]*"  # Element name or property.

INTEGER_NUMBER = r"(?:0(?:_?0)*|[1-9](?:_?[0-9])*)"
EXPONENT = r"[eE][-+]?[0-9](?:_?[0-9])*"
POINT_FLOAT = group(
    r"[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?", r"\.[0-9](?:_?[0-9])*"
) + maybe(EXPONENT)
EXPONENT_FLOAT = r"[0-9](?:_?[0-9])*" + EXPONENT
FLOAT_NUMBER = group(POINT_FLOAT, EXPONENT_FLOAT)
SI_NUMBER = group(INTEGER_NUMBER, POINT_FLOAT) + r"[pnumkMGT]"
INFINITY = r"inf"
IMAGINARY_NUMBER = group(
    INFINITY + r"[jJ]", r"[0-9](?:_?[0-9])*[jJ]", FLOAT_NUMBER + r"[jJ]"
)
NUMBER = group(IMAGINARY_NUMBER, SI_NUMBER, FLOAT_NUMBER, INTEGER_NUMBER, INFINITY)

SINGLE_QUOTED_STRING = r"'[^\n'\\]*(?:\\.[^\n'\\]*)*'"
DOUBLE_QUOTED_STRING = r'"[^\n"\\]*(?:\\.[^\n"\\]*)*"'
STRING = group(SINGLE_QUOTED_STRING, DOUBLE_QUOTED_STRING)

# Types that only take one form. The order here is important (highest priority first).
LITERALS = {
    "EQUALS": "=",
    "PLUS": "+",
    "MINUS": "-",
    "POWER": "**",  # Has to be above TIMES.
    "TIMES": "*",
    "FLOORDIVIDE": "//",  # Has to be above DIVIDE.
    "DIVIDE": "/",
    "COMMA": ",",
    "LBRACKET": "[",
    "RBRACKET": "]",
    "LPAREN": "(",
    "RPAREN": ")",
}
