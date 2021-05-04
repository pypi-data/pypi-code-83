from HtmlCreator.ExistElement import ExistElement


class Title(ExistElement):

    def _getEleKey(self):
        return 'title'

    def __init__(self, title: str):
        super().__init__()
        self.__title = title

    def _getContStr(self):
        return self.__title
