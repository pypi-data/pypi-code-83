from quickey_python_sdk.config import base_url
import requests

class App:
    def __init__(self, apiKey):
        self.__apiKey = apiKey
        self.__base_url = '{0}/loginRegister'.format(base_url)

    def getAppMetaData(self):
        payload = {'apiKey':self.__apiKey}
        return requests.post(self.__base_url, data=payload)

