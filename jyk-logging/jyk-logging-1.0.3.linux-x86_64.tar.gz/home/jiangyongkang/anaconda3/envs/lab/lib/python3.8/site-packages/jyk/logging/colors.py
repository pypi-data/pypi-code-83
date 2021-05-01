"""jyk color"""

import os
import sys


def color(text: str, color_code: int) -> str:
    """Colorize text.
    Args:
        text: text.
        color_code: color.
    Returns:
        colorized text.
    """
    # $TERM under Windows:
    # cmd.exe -> "" (what would you expect..?)
    # cygwin -> "cygwin" (should support colors, but doesn't work somehow)
    # mintty -> "xterm" (supports colors)
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text
    return "\x1b[%dm%s\x1b[0m" % (color_code, text)


def black(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        black text.
    """
    return color(text, 30)


def red(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        red text.
    """
    return color(text, 31)


def green(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Return:
        green text.
    """
    return color(text, 32)


def yellow(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Return:
        yellow text.
    """
    return color(text, 33)


def blue(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        blue text.
    """
    return color(text, 34)


def magenta(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        magenta text.
    """
    return color(text, 35)


def cyan(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        cyan text.
    """
    return color(text, 36)


def white(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        white text.
    """
    return color(text, 37)


def bold(text: str) -> str:
    """Colorize text.
    Args:
        text: text.
    Returns:
        bold text.
    """
    return color(text, 1)