def quote(string: str) -> str:
    """
    >>> quote('abc')
    '\"abc\"'

    >>> quote('"abc"')
    '\"abc\"'
    """
    return string if string.startswith('"') and string.endswith('"') else f'"{string}"'


def handle(string: str) -> str:
    """
    >>> handle('https://github.com/user/repo')
    'user/repo'

    >>> handle('user/repo')
    'user/repo'

    >>> handle('')
    ''
    """
    splt = string.split("/")
    return "/".join(splt[-2:] if len(splt) >= 2 else splt)


def pluralize(count: int, unit: str) -> str:
    """
    Pluralize a count and given its units.

    >>> pluralize(1, 'file')
    '1 file'

    >>> pluralize(2, 'file')
    '2 files'

    >>> pluralize(0, 'file')
    '0 files'
    """
    return f"{count} {unit}{'s' if count != 1 else ''}"


def indent_lines(string: str, indent: str) -> str:
    return indent + string.replace("\n", "\n" + indent) if string else ""


def truncate_lines(string: str, limit: int) -> str:
    return "\n".join(
        [
            line[:limit] + "..." if len(line) > limit else line
            for line in string.split("\n")
        ]
    )


def remove_prefix(string: str, prefix: str) -> str:
    """
    >>> remove_prefix('abc', 'ab')
    'c'

    >>> remove_prefix('abc', 'd')
    'abc'

    >>> remove_prefix('abc', 'abcd')
    'abc'
    """
    return string[len(prefix) :] if string.startswith(prefix) else string


def is_kebab_case(string: str) -> bool:
    """
    >>> is_kebab_case('a-b')
    True

    >>> is_kebab_case('ab')
    False

    >>> is_kebab_case('a--b')
    False

    >>> is_kebab_case('-a-b')
    False

    >>> is_kebab_case('a-b-')
    False
    """
    splt = string.split("-")
    return len(splt) > 1 and "" not in splt


def kebab_to_snake(string: str) -> str:
    """
    >>> kebab_to_snake('a-b')
    'a_b'

    >>> kebab_to_snake('ab')
    'ab'

    >>> kebab_to_snake('a--b')
    'a--b'
    """
    return string.replace("-", "_") if is_kebab_case(string) else string
