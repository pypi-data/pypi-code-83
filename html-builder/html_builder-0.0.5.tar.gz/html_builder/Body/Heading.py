
from html_builder import ExistElement


class Heading(ExistElement):
    def __init__(self, size: int):
        # 传入1至6的数来创建大小
        super().__init__()

        if size < 1 or size > 6:
            raise ValueError("Heading over 1~6")
        self.__size = size

    def _getEleKey(self):
        return f'h{self.__size}'
