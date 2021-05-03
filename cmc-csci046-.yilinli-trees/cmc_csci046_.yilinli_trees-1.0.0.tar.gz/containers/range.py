def range(a, b=None, c=None):
    '''
    This function should behave exactly like
    the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    HINT:
    If you can figure out how to use the built-in range
    function (without modifying the test cases!),
    then feel free to do so.
    That's fairly difficult to do, however,
    and it's much easier to just implement this
    function normally using the yield syntax.
    '''
    if a is None:
        return []
    else:
        if b is None and c is None:
            r0 = 0
            r1 = a
            while r0 < r1:
                yield r0
                r0 += 1
        if b is None and c is not None:
            return []
        if b is not None and c is None:
            r0 = a
            r1 = b - 1
            while r0 <= r1:
                yield r0
                r0 += 1
        if b is not None and c is not None:
            r0 = a
            r1 = b - 1
            if r0 > r1:
                if c > 0:
                    return []
                if c < 0:
                    while r0 > r1 + 1:
                        yield r0
                        r0 += c
            else:
                while r0 <= r1:
                    if c < 0:
                        return []
                    else:
                        yield r0
                        r0 += c
