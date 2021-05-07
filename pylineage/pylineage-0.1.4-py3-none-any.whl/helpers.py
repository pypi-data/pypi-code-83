from functools import wraps
from typing import Any, Callable, Dict, List

import regex


# Wrapper to allow constructed decorator to use parameters
def parametrized(dec: Any) -> Callable:
    def layer(*args: Any, **kwargs: Any):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parametrized
def substitute_by_regex(func: Callable, reg: str) -> Callable:
    @wraps(func)
    def wrapper(self: Any, string: str, *args: Any, **kwargs: Any) -> List[Any]:
        counter = -1

        def count() -> int:
            nonlocal counter
            counter += 1
            return counter

        # Substitute groups
        groups = regex.findall(reg, string)
        substituted = regex.sub(reg, lambda x: "{" + str(count()) + "}", string)

        # Use substitution in function
        result = func(self, substituted, *args, **kwargs)

        # Allow robust indexing
        if isinstance(result, tuple):
            result = list(result)
        else:
            result = [result]

        # Reapply groups (assume last variable needs substitution)
        if isinstance(result[-1], str):
            result[-1] = result[-1].format(*groups)
        elif isinstance(result[-1], list):
            result[-1] = [string.format(*groups) for string in result[-1]]
        elif isinstance(result[-1], dict):
            result[-1] = {
                key: value.format(*groups) for key, value in result[-1].items()
            }

        if len(result) == 1:
            return result[0]
        return result

    return wrapper


def substitute_brackets(func: Callable) -> Callable:
    return substitute_by_regex(r"(\((?>[^()]+|(?1))*\))")(func)


def substitute_quotes(func: Callable) -> Callable:
    return substitute_by_regex(r"('[^']+'|\"[^\"]+\")")(func)


def replace_regex_groups_with_non_capturing_groups(reg: str) -> str:
    non_capturing_reg = regex.sub(
        r"(?<!\\)(\((?>[^()]+|(?1))*\))", lambda x: f"(?:{x.group()[1:]}", reg
    )
    return non_capturing_reg


def string_replace_with_dict(string: str, replace_dict: Dict[str, str]) -> str:
    applied = {key: False for key in replace_dict}

    while not all(applied.values()):
        for rgx in replace_dict:
            if applied[rgx]:
                continue
            string, n = regex.subn(rgx, replace_dict[rgx], string)
            if n > 0:
                applied[rgx] = True
    return string
