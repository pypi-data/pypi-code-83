from HtmlCreator import Element


class Text(Element):
    def _getEleKey(self):
        return ''

    def __str__(self):
        return self.text

    def __init__(self, text: str):
        text = self.replace(text)
        self.text = text

    @staticmethod
    def replace(text: str) -> str:
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&#39;')
        text = text.replace(" ", '&nbsp;')
        return text


