def __validate_and_return_number(n):
    """RETURNS A FUNCTION which on execution raises a TypeError"""

    def raise_TypeError_func(n):
        def raise_TypeError():
            raise TypeError(f"{n} is not a number")

        return raise_TypeError

    def check_and_convert_string_func(s):
        """RETURNS A FUNCTION which on execution checks the string passed is a valid number or not"""

        def check_and_convert_string():
            if s.isdigit():
                return int(s)
            try:
                return float(s)
            except:
                raise_TypeError_func(s)()

        return check_and_convert_string

    return {
        "str": check_and_convert_string_func(n),
        "int": lambda: n,
        "float": lambda: n,
    }.get(type(n).__name__, raise_TypeError_func(n))()


def add(a, b):
    a = __validate_and_return_number(a)
    b = __validate_and_return_number(b)
    result = a + b
    if isinstance(result, float):
        return round(result, 16)
    return result


def sub(a, b):
    a = __validate_and_return_number(a)
    b = __validate_and_return_number(b)
    result = a - b
    if isinstance(result, float):
        return round(result, 16)
    return result


def mul(a, b):
    a = __validate_and_return_number(a)
    b = __validate_and_return_number(b)
    result = a * b
    if isinstance(result, float):
        return round(result, 16)
    return result


def div(a, b):
    a = __validate_and_return_number(a)
    b = __validate_and_return_number(b)
    result = a / b
    if isinstance(result, float):
        return round(result, 16)
    return result
