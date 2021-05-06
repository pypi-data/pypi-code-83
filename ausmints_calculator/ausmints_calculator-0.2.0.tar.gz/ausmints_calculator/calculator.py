"""
A calculator application that can do the most basic arithmetic actions -
addition, subtraction, multiplication, division, squaring and taking a square root
"""

from math import sqrt, fsum


class Calculator:
    """A class used to create a Calculator object

    ...

    Attributes
    ----------
    memory : int, float
        a variable that is being operated on by all the methods of Calculator object,
        upon the creation of Calculator object, instantiated to 0

    Methods
    -------
    add(number: float) -> float
        Adding the "number" to "memory" variable
    subtract(number: float) -> float
        Subtracting the "number" from the "memory" variable
    multiply(number: float) -> float
        Multiplying the "number" with the "memory" variable
    divide(number: float) -> float
        Dividing the "memory" variable with the "number"
    squared() -> float
        Squaring the "memory" variable
    square_root() -> float
        Taking the square root of the "memory" variable
    reset_memory() -> int
        Resetting the "memory" variable to 0
    """

    def __init__(self):
        self.memory: float = 0

    def add(self, number: float) -> float:
        """Addition using fsum for more accuracy

        The "number" parameter is added to the Calculator "memory" attribute
        and the sum is saved back into the "memory" attribute and returned

        >>> calc = Calculator()
        >>> calc.add(8)
        8.0
        >>> calc.add(-3)
        5.0
        >>> calc.add(2.25)
        7.25
        """

        self.memory = fsum([self.memory, number])
        return self.memory

    def subtract(self, number: float) -> float:
        """Subtraction using fsum for more accuracy

        The "number" parameter is multiplied by -1 and then added to the Calculator "memory" attribute
        and the sum is saved back into the "memory" attribute and returned

        >>> calc = Calculator()
        >>> calc.subtract(10)
        -10.0
        >>> calc.subtract(-24)
        14.0
        >>> calc.subtract(4.75)
        9.25
        """

        self.memory = fsum([self.memory, number*-1])
        return self.memory

    def multiply(self, number: float) -> float:
        """Multiplication

        First the "number" parameter is checked if it is a number, then
        the Calculator "memory" attribute is multiplied by the "number" parameter
        and the product is saved back into the "memory" attribute and returned

        Raises
        ------
        TypeError - if the "number" parameter provided is not int or float

        >>> calc = Calculator()
        >>> calc.add(4)
        4.0
        >>> calc.multiply(3)
        12.0
        >>> calc.multiply(0.5)
        6.0
        >>> calc.multiply(-3)
        -18.0
        """
        if isinstance(number, float) or isinstance(number, int):
            self.memory = self.memory * number
            return self.memory
        raise TypeError("Expected float or int")

    def divide(self, number: float) -> float:
        """Division

        The Calculator "memory" attribute is divided by the "number" parameter
        and the result is saved back into the "memory" attribute and returned

        >>> calc = Calculator()
        >>> calc.add(24)
        24.0
        >>> calc.divide(4)
        6.0
        >>> calc.divide(0.3)
        20.0
        >>> calc.divide(-5)
        -4.0
        """

        self.memory = self.memory / number
        return self.memory

    def squared(self) -> float:
        """Taking the square of a number

        The Calculator "memory" attribute is squared,
        the result is saved back into the "memory" attribute and returned

        >>> calc = Calculator()
        >>> calc.add(5)
        5.0
        >>> calc.squared()
        25.0
        """

        self.memory = self.memory ** 2
        return self.memory

    def square_root(self) -> float:
        """Taking the square root of a number

        Square root is taken of the Calculator "memory" attribute,
        the result is saved back into the "memory" attribute and returned

        >>> calc = Calculator()
        >>> calc.add(25)
        25.0
        >>> calc.square_root()
        5.0
        """

        self.memory = sqrt(self.memory)
        return self.memory

    def reset_memory(self) -> int:
        """Resets the Calculator "memory" attribute to 0 and returns it

        >>> calc = Calculator()
        >>> calc.add(25)
        25.0
        >>> calc.reset_memory()
        0
        """

        self.memory = 0
        return self.memory
