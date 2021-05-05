from enum import Enum


class SerialiserName(str, Enum):
    L_Z4_NUMPY = "lz4_numpy"

    def __str__(self) -> str:
        return str(self.value)
