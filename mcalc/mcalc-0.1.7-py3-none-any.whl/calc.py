class Calculator:
    """
    Calculator class for simple arithmetic operations.

    Default initialization value is 0, but other values can be provided.
    Default reset value is 0, but other values can be provided.
    The n_root method does not work on negative numbers in _memory, and does not have
    high accuracy, user discretion advised.

    Usage examples:

    >>> Calculator(0)
    0.0
    >>> Calculator(1)
    1.0
    >>> cal1 = Calculator(10)
    >>> cal1.add(5)
    15.0
    >>> cal1.subtract(10)
    5.0
    >>> cal1.multiply(-5)
    -25.0
    >>> cal1.divide(-5)
    5.0
    >>> cal1.n_root(3)
    1.7099759466766968
    >>> cal1.reset(9)
    9.0
    >>> cal1.n_root(2)
    3.0
    >>> cal1.n_root(0.2)
    243.0
    """

    def __init__(self, num: float = 0) -> None:
        self._memory = float(num)

    def add(self, num: float) -> float:
        self._memory += num
        return self._memory

    def subtract(self, num: float) -> float:
        self._memory -= num
        return self._memory

    def multiply(self, num: float) -> float:
        self._memory *= num
        return self._memory

    def divide(self, num: float) -> float:
        self._memory /= num
        return self._memory

    def n_root(self, n: float) -> float:
        "Takes n-th root of value stored in _memory"
        if self._memory < 0:
            raise NotImplementedError(
                "Can't take roots of negative numbers, complex numbers not supported"
            )
        self._memory = self._memory ** (1 / n)
        return self._memory

    def reset(self, num: float = 0.0) -> float:
        self._memory = float(num)
        return self._memory

    def get_memory(self) -> float:
        return self._memory
