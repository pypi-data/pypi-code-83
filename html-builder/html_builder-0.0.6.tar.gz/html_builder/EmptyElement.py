from abc import ABC

from html_builder import *


class EmptyElement(Element, ABC):
    # body下的空标签
    def __str__(self):
        return f'<{self._getEleKey()}{self._getAttrStr()}>'

