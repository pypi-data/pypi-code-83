from abc import ABC, abstractmethod

from HtmlCreator import EmptyElement


class Input(EmptyElement, ABC):
    def __init__(self):
        self.__name: str = None
        self.__value: str = None

    def _getEleKey(self):
        return 'input'

    @abstractmethod
    def _getType(self):
        return ''

    def _getAttrs(self) -> dict:
        rt = super(Input, self)._getAttrs()
        rt['type'] = self._getType()
        if self.__name is not None:
            rt['name'] = self.__name
        return rt


    def name(self, name: str):
        self.__name = name
        return self


    def value(self, value: str):
        self.__value = value
        return self
