"""Calculator, more info in Readme.md"""
from typing import NamedTuple


class Calculator:
    """Calculator which has functions:
    - add
    - subtract
    - multiply
    - divide
    - n root

    - This calculator has running memory which is manipulated after every arithmetic action taken
    - Calculator stores all the previous arithmetic actions taken in arithmetics_seq variable until it gets reset.
    - Calculator starting point is 0.0 and we manipulate from there.
    - Running result always will be float
    - Example: calculator.add(2) will set __running_res to 2 , then if we would execute calculator.subtract(1) ,
    running memory would be set to 1
    - If non integer or float value is passed to the function it will not change anything and will
    return same running memory as before
    """

    def check_type(self, y) -> bool:
        # Variable type checking, if variables is not float or int return false
        if not (type(y) == float or type(y) == int):
            print("Wrong input")
            return False
        else:
            return True

    def __init__(self, starting_input=None):
        # Set memory starting point.
        if starting_input is None or self.check_type(starting_input) is False:
            self.__starting_point = 0.0
        else:
            self.__starting_point = starting_input

        self.__running_res = self.__starting_point
        self.__actions_seq = []  # type: list[__action]
        self.__action = NamedTuple("Action", [("y", float), ("action", str), ("result", float)])

    def add(self, y: float) -> float:
        if not self.check_type(y):
            return self.__running_res
        self.__running_res = self.__running_res + y
        self.__actions_seq.append(self.__action(float(y), "+", self.__running_res))
        return self.__running_res

    def subtract(self, y: float) -> float:
        if not self.check_type(y):
            return self.__running_res
        self.__running_res = self.__running_res - y
        self.__actions_seq.append(self.__action(float(y), "-", self.__running_res))
        return self.__running_res

    def multiply(self, y: float) -> float:
        if not self.check_type(y):
            return self.__running_res
        self.__running_res = self.__running_res * y
        self.__actions_seq.append(self.__action(float(y), "*", self.__running_res))
        return self.__running_res

    def divide(self, y: float) -> float:
        if not self.check_type(y):
            return self.__running_res
        self.__running_res = self.__running_res / y
        self.__actions_seq.append(self.__action(float(y), "/", self.__running_res))
        return self.__running_res

    def n_root(self, y: float) -> float:
        if not self.check_type(y):
            return 0
        self.__running_res = self.__running_res ** (1 / float(y))
        self.__actions_seq.append(self.__action(float(y), "root", self.__running_res))
        return self.__running_res

    def get_current_result(self) -> float:
        return self.__running_res

    def get_action_seq(self) -> str:
        """returns action sequence as a string. Example: 4 + 2 + 3 - 2 = 7"""
        string_to_print = ""
        if self.__starting_point != 0.0 and self.__starting_point is not None:
            string_to_print = str(self.__starting_point) + " "

        for current_action in self.__actions_seq:
            string_to_print += str(current_action.action) + " " + str(current_action.y) + " "

        return string_to_print.strip() + " = " + str(self.__running_res)

    def reset_memory(self):
        self.__running_res = 0.0
        self.__actions_seq = []
