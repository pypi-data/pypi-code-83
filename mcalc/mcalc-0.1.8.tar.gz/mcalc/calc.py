from typing import Any


class Calculator:
    """
    Calculator class for simple arithmetic operations.

    Default initialization value is 0, but other values can be provided.
    Default reset value is 0, but other values can be provided.
    The n_root method does not work on negative numbers in __memory, and does not have
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
        self.__memory = self.__parser(num)

    def __parser(self, value: Any) -> float:
        """Check for funny inputs"""
        try:
            return float(value)
        except Exception as e:
            print(f"Inputs should be numeric\nerror -> {e}")
            raise

    def add(self, num: float) -> float:
        self.__memory += self.__parser(num)
        return self.__memory

    def subtract(self, num: float) -> float:
        self.__memory -= self.__parser(num)
        return self.__memory

    def multiply(self, num: float) -> float:
        self.__memory *= self.__parser(num)
        return self.__memory

    def divide(self, num: float) -> float:
        self.__memory /= self.__parser(num)
        return self.__memory

    def n_root(self, n: float) -> float:
        """Takes n-th root of value stored in __memory"""
        if self.__memory < 0:
            raise NotImplementedError(
                "Can't take roots of negative numbers, complex numbers not supported"
            )
        self.__memory = self.__memory ** (1 / n)
        return self.__memory

    def reset(self, num: float = 0.0) -> float:
        self.__memory = self.__parser(num)
        return self.__memory

    def get_memory(self) -> float:
        return self.__memory
