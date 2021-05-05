from html_builder import ExistElement


class Paragraph(ExistElement):
    """相当于p标签"""

    def _getEleKey(self):
        return 'p'
