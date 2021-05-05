from enum import Enum


class TradingAlgoParamType(str, Enum):
    STR_ = "str_"
    INT_ = "int_"
    FLOAT_ = "float_"
    BOOL_ = "bool_"

    def __str__(self) -> str:
        return str(self.value)
