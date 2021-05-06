"""Core function for chardif."""

import difflib
from wasabi import color, Printer


_WASABI_PRINTER = Printer()


def chardif(a: str, b: str) -> None:
    """Prints a per-char diff of the two strings to stdout.
    Parameters
    ----------
    a : str
        The first string to compare.
    b: str
        The second string to compare
    """
    output = []
    matcher = difflib.SequenceMatcher(None, a, b)
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode == "equal":
            output.append(a[a0:a1])
        elif opcode == "insert":
            output.append(color(b[b0:b1], fg=16, bg="green"))
        elif opcode == "delete":
            output.append(color(a[a0:a1], fg=16, bg="red"))
        elif opcode == "replace":
            output.append(color(b[b0:b1], fg=16, bg="green"))
            output.append(color(a[a0:a1], fg=16, bg="red"))
    output = "".join(output)
    _WASABI_PRINTER.text(output)
