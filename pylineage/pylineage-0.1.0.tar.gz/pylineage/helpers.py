from functools import wraps
from typing import Any, Callable, List

import regex


def substitute_brackets(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(self: Any, string: str, *args: Any, **kwargs: Any) -> List[Any]:
        reg = r"(\((?>[^()]+|(?1))*\))"
        counter = -1

        def count() -> int:
            nonlocal counter
            counter += 1
            return counter

        # Substitute brackets
        brackets = regex.findall(reg, string)
        substituted = regex.sub(reg, lambda x: "{" + str(count()) + "}", string)

        # Use substitution in function
        result = func(self, substituted, *args, **kwargs)

        # Allow robust indexing
        if isinstance(result, tuple):
            result = list(result)
        else:
            result = [result]

        # Reapply brackets (assume last variable needs substitution)
        if isinstance(result[-1], str):
            result[-1] = result[-1].format(*brackets)
        elif isinstance(result[-1], list):
            result[-1] = [string.format(*brackets) for string in result[-1]]
        elif isinstance(result[-1], dict):
            result[-1] = {key: value.format(*brackets) for key, value in result.items()}

        if len(result) == 1:
            return result[0]
        return result

    return wrapper
