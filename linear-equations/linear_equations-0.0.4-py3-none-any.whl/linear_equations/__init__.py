"""linear_equations
Defines classes to solve Linear Equations in one and two variables"""


class Symbol():
    """Symbol object for linear equations (lowercase letters)
    example: 'x', 'y', 'p', 'q', etc."""

    def __init__(self, symbol):
        """initialize instance"""

        if not isinstance(symbol, str):
            raise TypeError("Symbol should be 'str'")

        if len(symbol) != 1:
            raise ValueError("Symbol should be char of len() == 1")

        import string

        if symbol not in string.ascii_lowercase:
            raise ValueError("Symbol should be lowercase letter")

        self.symbol = symbol


    def __str__(self, /):
        """defines str(self)"""

        return self.symbol


    def __repr__(self, /):
        """defines repr(self)"""

        return f"Symbol('{self.symbol}')"


    def __eq__(self, value, /):
        """return self == value"""

        return self.symbol == value.symbol


################################################################################


class LinearEquation1D():
    """objects of type ax + b = 0"""

    def __init__(self, a, b, /, *, sym=Symbol("x")):
        """initialize instance"""

        values = [a, b]

        for val in a, b:
            if not isinstance(val, (int, float, complex)):
                raise TypeError(f"unsupported value: must be 'int', 'float'")
        if not a:
            raise ValueError("'a' cannot be zero")

        if not isinstance(sym, Symbol):
            raise TypeError("expected type 'Symbol' for 'sym'")

        for i in range(2):
            if float(values[i]).is_integer():
                values[i] = int(values[i])

        self.a, self.b = values
        self.values, self.sym = tuple(values), sym


    def __str__(self, /):
        """defines str(self)"""

        val = list(self.values)
        sign, plus, minus = ["", ""], "", "- "

        for i in range(2):
            sign[i] = plus if val[i] >= 0 else minus
            val[i], plus = abs(val[i]), "+ "

        if self.b:
            return f"{sign[0]}{val[0]}{self.sym} {sign[1]}{val[1]} = 0"
        else:
            return f"{sign[0]}{val[0]}{self.sym} = 0"


    def __repr__(self, /):
        """defines repr(self)"""

        return f"LinearEquation1D({self.a}, {self.b}, sym={self.sym !r})"


    def __neg__(self, /):
        """return -self"""

        return LinearEquation1D(*(-val for val in self.values), sym=self.sym)


    def __eq__(self, value, /):
        """return self == value
        scaled linear equations are considered equal"""

        if type(self) is not type(value) or (self.sym != value.sym):
            return False
        if self.b == value.b == 0:
            return True
        else:
            return solve1D(self) == solve1D(value)


    def __add__(self, value, /):
        """return self + value"""

        if self.sym != value.sym:
            raise ValueError("Symbol of left and right operands must be same")
        else:
            return LinearEquation1D(
                *(self.values[i] + value.values[i] for i in range(2)),
                sym=self.sym
            )


    def __sub__(self, value, /):
        """return self - value"""

        return self + (-value)


    def __mul__(self, value, /):
        """return self * value
        value is an int / float to scale the linear equation"""

        if not value:
            raise ValueError("can't multiply linear equation by zero")
        else:
            return LinearEquation1D(
                *(self.values[i] * value for i in range(2)), sym=self.sym
            )

    __rmul__ = __mul__


    def __truediv__(self, value, /):
        """return self / value
        value is an int / float to scale the linear equation"""

        if not value:
            raise ZeroDivisionError("can't divide linear equation by zero")
        else:
            return self * (1 / value)


################################################################################


class LinearEquation2D():
    """objects of type ax + by + c = 0"""

    def __init__(self, a, b, c, /, *, sym1=Symbol("x"), sym2=Symbol("y")):
        """initialize instance"""

        values = [a, b, c]

        for i in range(3):
            if not isinstance(values[i], (int, float, complex)):
                raise TypeError(f"unsupported value: must be 'int', 'float'")

            if i != 2 and not values[i]:
                raise ValueError(f"'{'b' if i else 'a'}' cannot be zero")

        for symbol in sym1, sym2:
            if not isinstance(symbol, Symbol):
                raise TypeError("expected type 'Symbol' for 'sym1' and 'sym2'")

        for i in range(3):
            if float(values[i]).is_integer():
                values[i] = int(values[i])

        self.a, self.b, self.c = values
        self.values = tuple(values)
        self.sym1, self.sym2, self.symbols = sym1, sym2, (sym1, sym2)


    def __str__(self, /):
        """defines str(self)"""

        val = list(self.values)
        plus, minus = "", "- "

        for i in range(3):
            val[i] = (plus if val[i] >= 0 else minus) + str(abs(val[i]))
            plus = "+ "

        if self.c:
            return f"{val[0]}{self.sym1} {val[1]}{self.sym2} {val[2]} = 0"
        else:
            return f"{val[0]}{self.sym1} {val[1]}{self.sym2} = 0"


    def __repr__(self, /):
        """defines repr(self)"""

        return " ".join((
            f"LinearEquation2D({self.a}, {self.b}, {self.c},",
            f"sym1={self.sym1 !r}, sym2={self.sym2 !r})"
        ))


    def __neg__(self, /):
        """return -self"""

        return LinearEquation2D(
            *(-val for val in self.values), sym1=self.sym1, sym2=self.sym2
        )


    def __eq__(self, value, /):
        """return self == value
        scaled linear equations are considered equal"""

        if type(self) is not type(value) or (self.symbols != value.symbols):
            return False
        try:
            return len(
                {self.values[i] / value.values[i] for i in range(3)}
            ) == 1
        except ZeroDivisionError:
            return len(
                {self.values[i] / value.values[i] for i in range(2)}
            ) == 1 and (self.c == value.c == 0)


    def __add__(self, value, /):
        """return self + value"""

        if self.symbols != value.symbols:
            raise ValueError("Symbol of left and right operands must be same")

        try:
            return LinearEquation2D(
                *(self.values[i] + value.values[i] for i in range(3)),
                sym1=self.sym1, sym2=self.sym2
            )

        except ValueError:
            if not (self.a + value.a):
                return LinearEquation1D(
                    *(self.values[i] + value.values[i] for i in range(1, 3)),
                    sym=self.sym2
                )
            if not (self.b + value.b):
                return LinearEquation1D(
                    *(self.values[i] + value.values[i] for i in range(0, 3, 2)),
                    sym=self.sym1
                )


    def __sub__(self, value, /):
        """return self - value"""

        return self + (-value)


    def __mul__(self, value, /):
        """return self * value
        value is an int / float to scale the linear equation"""

        if not value:
            raise ValueError("can't multiply linear equation by zero")
        else:
            return LinearEquation2D(
                *(self.values[i] * value for i in range(3)),
                sym1=self.sym1, sym2=self.sym2
            )

    __rmul__ = __mul__


    def __truediv__(self, value, /):
        """return self / value
        value is an int / float to scale the linear equation"""

        if not value:
            raise ZeroDivisionError("can't divide linear equation by zero")
        else:
            return self * (1 / value)


################################################################################


def solve1D(eqn: LinearEquation1D):
    """solve 1 linear equation in 1 variable
    return answer as float"""

    if not isinstance(eqn, LinearEquation1D):
        raise TypeError("solve1D expects LinearEquation1D as arg")
    else:
        return float(-eqn.b / eqn.a)


def consistency(eqn1: LinearEquation2D, eqn2: LinearEquation2D):
    """return number of solutions (0, 1 or 2) to refer to
    the consistency of 2 LinearEquation2D objects:
        • 0 -> parallel
        • 1 -> intersecting
        • 2 -> coincident"""

    for eqn in eqn1, eqn2:
        if not isinstance(eqn, LinearEquation2D):
            raise TypeError("'consistency()' expects LinearEquation2D as args")

    if eqn1 == eqn2:
        return 2
    if ((eqn1.a / eqn2.a) != (eqn1.b / eqn2.b)):
        return 1
    else:
        return 0


def solve2D(eqn1: LinearEquation2D, eqn2: LinearEquation2D):
    """solve 2 linear equations in 2 variables
    return answer as tuple of floats
    return None if no solutions exist"""

    for eqn in eqn1, eqn2:
        if not isinstance(eqn, LinearEquation2D):
            raise TypeError("solve2D expects LinearEquation2D as args")

    if not consistency(eqn1, eqn2):
        return None, None

    if consistency(eqn1, eqn2) == 2:
        return float("inf"), float("inf")

    eqn1 *= (eqn2.a / eqn1.a)
    y = solve1D(eqn1 - eqn2)
    x = solve1D(LinearEquation1D(eqn2.a, eqn2.b*y + eqn2.c))

    return x, y


def satisfies(eqn: LinearEquation2D, /, x, y):
    """returns True if given x and y values satisfy the given LinearEquation2D,
    False otherwise. x and y can be int / float."""

    if not isinstance(eqn, LinearEquation2D):
        raise TypeError(
            "invalid argument type for eqn: must be LinearEquation2D"
        )

    for num in x, y:
        if not isinstance(num, (int, float)):
            raise TypeError("x and y must be int / float")

    return not x*eqn.a + y*eqn.b + eqn.c