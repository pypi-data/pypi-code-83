from typing import Any, Callable, List, TypeVar

T = TypeVar("T")  # pylint: disable = C0103


def whitelist(
    lst: List[Any],
    includes: List[Any],
    transform: Callable[[Any], Any] = lambda x: x,
) -> List[Any]:
    """
    >>> whitelist([1, 2, 3], [1, 2])
    [1, 2]

    >>> whitelist([1, 2, 3], [])
    [1, 2, 3]

    >>> whitelist([1, 2, 3], ['1', '2'], lambda x: str(x))
    [1, 2]
    """
    if len(includes) == 0:
        return lst

    return list(filter(lambda x: transform(x) in includes, lst))
