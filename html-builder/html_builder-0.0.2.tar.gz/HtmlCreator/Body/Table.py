from HtmlCreator import ExistElement

class Table(ExistElement):
    def __init__(self,border:int=1,caption:str=None,headings:list = []):
        self.__border = border
        self.__caption = caption
        self.__headings = headings

    def _getAttrs(self):
        return {
            'border':self.__border,
        }

class TableElement(ExistElement):
    ...

class TCaption(TableElement):
    ...

class Tr(TableElement):
    ...

class Th(TableElement):
    ...

class Td(TableElement):
    ...