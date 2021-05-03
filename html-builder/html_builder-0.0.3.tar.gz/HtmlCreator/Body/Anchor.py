from HtmlCreator import *


class Anchor(ExistElement):
    def __init__(self, url: str, to_url=False):
        super().__init__()
        if to_url:
            if url[:8] != 'https://':
                if url[:7] != 'http://':
                    url = 'https://' + url
        self.__href = url

    @classmethod
    def linkToId(cls, id: str):
        super().__init__()
        cls.__href = f'#{id}'

    def _getAttrs(self):
        return {
            'href': self.__href
        }

    def _getEleKey(self):
        return 'a'
