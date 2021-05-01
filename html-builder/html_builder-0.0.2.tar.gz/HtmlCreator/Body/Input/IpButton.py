from HtmlCreator.Body.Input.Input import Input


class IpButton(Input):
    TYPE_BUTTON = 'button'
    TYPE_SUBMIT = 'submit'
    TYPE_RESET = 'reset'


    def __init__(self,type:str = 'button'):
        self.__type = type

    def _getType(self):
        return self.__type