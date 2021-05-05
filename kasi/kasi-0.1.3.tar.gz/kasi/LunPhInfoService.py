from urllib.parse import unquote

import pandas as pd
import requests


class LunPhInfoService:
    """
    월령 정보를 조회하는 서비스 입니다.
    """

    def __init__(self, serviceKey):
        if "%" in serviceKey:
            serviceKey = unquote(serviceKey)
        self._endpoint = (
            "http://apis.data.go.kr/B090041/openapi/service/LunPhInfoService"
        )
        self._serviceKey = serviceKey
        self._headers = {
            "Accept": "application/json",
        }

    def getLunPhInfo(self, solYear, solMonth=None, solDay=None):
        """
        월령 정보조회
        """
        if solMonth is None and solDay is None:
            if isinstance(solYear, int):
                solYear = str(solYear)
            date = pd.Timetamp(solYear)
            solYear = date.year
            solMonth = date.month
            solDay = date.day
        params = {
            "solYear": "%04d" % solYear,
            "solMonth": "%02d" % solMonth,
            "solDay": "%02d" % solDay if solDay is not None else "",
        }
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getLunPhInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result
