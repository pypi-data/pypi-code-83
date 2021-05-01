from abc import ABCMeta

from typing import List, Optional, Union

from HtmlCreator import Element
from HtmlCreator.Body.Text import Text


class ExistElement(Element, metaclass=ABCMeta):
    # abstract class
    def __init__(self, content: Optional[Union[List[Element]]] = None, ):
        if content is None:
            self.elements = []
        else:
            self.elements = content

    def text(self, text:str):
        self.elements.append(Text(text))
        return self

    def addElement(self, ele: Element):
        self.elements.append(ele)
        return self

    def getElements(self):
        return self.elements

    def _getContStr(self):
        rt = ''
        for ele in self.getElements():
            rt += str(ele)
        return rt

    def __str__(self):
        return self._wrapContent()

    def _wrapContent(self):
        return f'<{self._getEleKey()}{self._getAttrStr()}>{self._getContStr()}</{self._getEleKey()}>'
