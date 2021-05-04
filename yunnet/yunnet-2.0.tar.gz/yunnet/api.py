import httpx as requests
from .errors import *
import json


class Unt:

    __api_domain = "https://api.yunnet.ru/"
    __current_key = None

    def __init__(self, accessKey):
        if len(accessKey) != 75:
            raise AuthError("Access key must be provided")

        res = json.loads(
            requests.post(
                self.__api_domain + str("users.get?key=") + str(accessKey)
            ).text
        )
        if "error" in res:
            raise AuthError("Access key is incorrect")

        self.__current_key = accessKey

    """
        CALL THE API METHOD HERE
    """

    def execute(self, methodName, params={}):
        res = json.loads(
            requests.post(
                self.__api_domain + str(methodName) + "?key=" + str(self.__current_key),
                params=params,
            ).text
        )
        if "error" in res:
            raise APIError(res)

        return res
