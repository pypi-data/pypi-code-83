from quickey_python_sdk.config import base_url
import requests

class Auth:
    def __init__(self):
        self.__base_url = '{0}/loginRegister'.format(base_url)
    
    def getAccessToken(self, email):
        self.__email = email
        payload = {'userEmail':self.__email}
        return requests.post(self.__base_url, data=payload)
