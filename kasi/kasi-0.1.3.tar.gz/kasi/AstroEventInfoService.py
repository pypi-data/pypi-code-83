from urllib.parse import unquote

import requests


class AstroEventInfoService:
    """
    서비스 설명	천문현상 정보를 조회하는 서비스 입니다.
    """

    def __init__(self, serviceKey):
        if "%" in serviceKey:
            serviceKey = unquote(serviceKey)
        self._endpoint = (
            "http://apis.data.go.kr/B090041/openapi/service/AstroEventInfoService"
        )
        self._serviceKey = serviceKey
        self._headers = {
            "Accept": "application/json",
        }

    def getAstroEventInfo(self, solYear, solMonth=None, numOfRows=None, pageNo=None):
        """
        천문현상 정보조회
        """
        params = {
            "solYear": "%04d" % solYear,
            "solMonth": "%02d" % solMonth if solMonth is not None else "",
        }
        if numOfRows is not None:
            params["numOfRows"] = numOfRows
        if pageNo is not None:
            params["pageNo"] = pageNo
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getAstroEventInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result
