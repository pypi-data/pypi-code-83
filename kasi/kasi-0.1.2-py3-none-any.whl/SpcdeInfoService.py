from urllib.parse import unquote

import requests


class SpcdeInfoService:
    """
    국경일정보, 공휴일정보, 24절기정보, 잡절정보를 조회하는 서비스 입니다.
    """

    def __init__(self, serviceKey):
        if "%" in serviceKey:
            serviceKey = unquote(serviceKey)
        self._endpoint = (
            "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService"
        )
        self._serviceKey = serviceKey
        self._headers = {
            "Accept": "application/json",
        }

    def getHoliDeInfo(self, solYear, solMonth=None, numOfRows=None, pageNo=None):
        """
        월별로 구분(국경일), 요일, 공휴일 여부 등의 정보를 제공한다.
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
            self._endpoint + "/getHoliDeInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result

    def getRestDeInfo(self, solYear, solMonth=None, numOfRows=None, pageNo=None):
        """
        월별로 구분(공휴일), 요일, 공휴일 여부 등의 정보를 제공한다.
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
            self._endpoint + "/getRestDeInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result

    def get24DivisionsInfo(self, solYear, solMonth=None, numOfRows=None, pageNo=None):
        """
        월별로 구분(24절기), 요일, 공휴일 여부 등의 정보를 제공한다.
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
            self._endpoint + "/get24DivisionsInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result

    def getSundryDayInfo(self, solYear, solMonth=None, numOfRows=None, pageNo=None):
        """
        월별로 구분(잡절), 요일, 공휴일 여부 등의 정보를 제공한다.
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
            self._endpoint + "/getSundryDayInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result
