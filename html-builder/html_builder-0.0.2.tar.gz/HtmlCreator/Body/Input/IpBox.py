from HtmlCreator.Body.Input.Input import Input


# Single
class IpBoxS(Input):

    def _getType(self):
        return 'radio'


# Multiple
class IpBoxM(Input):

    def _getType(self):
        return 'checkbox'
