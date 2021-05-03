from time import monotonic

from hypothesis.strategies import (  # type: ignore
    composite,
    dictionaries,
    floats,
    integers,
    lists,
    none,
    sampled_from,
    sets,
    text,
    tuples,
)

elements = integers() | floats() | text() | none()
anything = (
    elements
    | lists(elements)
    | tuples(elements)
    | dictionaries(elements, elements)
    | sets(elements)
)
builtin_exceptions = list(
    exc for exc in Exception.__subclasses__() if exc.__module__ == "builtins"
)


def get_func_with_fuse(fuse: float):
    now = monotonic()

    def tester():
        return monotonic() - now >= fuse

    return tester


def get_awaitable_with_fuse(fuse: float):
    now = monotonic()

    async def tester():
        return monotonic() - now >= fuse

    return tester


@composite
def func_and_parameters(
    draw,
    func=sampled_from(
        [
            lambda: False,
            lambda a: a < 0,
            lambda a, b: a + b < 0,
            lambda a, b, c: a + b + c < 0,
        ]
    ),
):
    f = draw(func)
    args = []
    for _ in range(4):
        try:
            f(*args)
        except TypeError:
            args.append(draw(integers(min_value=-10, max_value=10)))
        else:
            return f, args
    raise ValueError("custom strategy is broken")


class MutableBoolean:
    def __init__(self, countdown: int):
        self.counter = countdown

    def __bool__(self):
        self.counter -= 1
        return self.counter == 0
