from HtmlCreator.ExistElement import ExistElement
from HtmlCreator.Head.Title import Title
from HtmlCreator.Head.Meta import MCharset


class Head(ExistElement):
    def _getEleKey(self):
        return 'head'

    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.addElement(MCharset())
        self.addElement(Title(title))
