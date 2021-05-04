from html_builder import EmptyElement


class Br(EmptyElement):
    """"""

    def _getEleKey(self):
        return 'br'


class Hr(EmptyElement):
    def _getEleKey(self):
        return 'hr'
