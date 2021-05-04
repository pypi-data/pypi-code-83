from urllib.parse import unquote

import pandas as pd
import requests


class LrsrCldInfoService:
    """
    음력일정보, 양력일정보, 특정음력일정보, 율리우스적일정보를 조회하는 서비스 입니다.
    """

    def __init__(self, serviceKey):
        if "%" in serviceKey:
            serviceKey = unquote(serviceKey)
        self._endpoint = (
            "http://apis.data.go.kr/B090041/openapi/service/LrsrCldInfoService"
        )
        self._serviceKey = serviceKey
        self._headers = {
            "Accept": "application/json",
        }

    def getLunCalInfo(
        self, solYear, solMonth=None, solDay=None, numOfRows=None, pageNo=None
    ):
        """
        양력일을 기준으로 음력날짜, 요일, 윤년, 평달/윤달 여부, 음력 간지, 율리우스 적일 등의 정보를 제공한다.
        날짜 입력 시 1582년 10월 4일까지는 율리우스력, 1582년 10월 5일부터는 그레고리력 기준
        입력범위: 1391년 2월 5일 ~ 2050년 12월 31일
        """
        if solMonth is None and solDay is None and not isinstance(solMonth, int):
            date = pd.Timestamp(solYear)
            solYear = date.year
            solMonth = date.month
            solDay = date.day
        assert solMonth is not None
        params = {
            "solYear": "%04d" % solYear,
            "solMonth": "%02d" % solMonth,
            "solDay": "%02d" % solDay if solDay is not None else "",
        }
        if numOfRows is not None:
            params["numOfRows"] = numOfRows
        if pageNo is not None:
            params["pageNo"] = pageNo
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getLunCalInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result

    def getSolCalInfo(self, lunYear, lunMonth, lunDay):
        """
        음력일을 기준으로 양력날짜, 요일, 윤년, 평달/윤달 여부, 음력 간지, 율리우스 적일 등의 정보를 제공한다.
        날짜 입력 시 1582년 9월 8일까지는 율리우스력으로 변환, 1582년 9월 9일부터 9월 18일까지는 율리우스력과 그레고리력으로 모두 변환,
        이 때 두 번째 변환 날짜가 그레고리력. 1582년 9월 19일부터는 그레고리력으로 변환
        입력범위: 1391년 1월 1일 ~ 2050년 11월 18일
        """
        params = {
            "lunYear": "%04d" % lunYear,
            "lunMonth": "%02d" % lunMonth,
            "lunDay": "%02d" % lunDay,
        }
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getSolCalInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result

    def getSpcifyLunCalInfo(
        self,
        fromSolYear,
        toSolYear,
        lunMonth,
        lunDay,
        leapMonth,
        numOfRows=None,
        pageNo=None,
    ):
        """
        양력연월일(내역), 요일 등의 정보를 제공한다.
        1582년 9월 8일까지는 율리우스력, 1582년 9월 9일부터 9월 18일까지는 두 개의 날짜로 변환,
        이 때 첫 번째는 율리우스력, 두 번째는 그레고리력 기준. 1582년 9월 19일부터는 그레고리력 기준
        양력년도 입력범위: 1391년 1월 1일 ∼ 2050년 11월 18일
        """
        assert leapMonth in ["평", "윤"]
        params = {
            "fromSolYear": "%04d" % fromSolYear,
            "toSolYear": "%04d" % toSolYear,
            "lunMonth": "%02d" % lunMonth,
            "lunDay": "%02d" % lunDay,
            "leapMonth": leapMonth,
        }
        if numOfRows is not None:
            params["numOfRows"] = numOfRows
        if pageNo is not None:
            params["pageNo"] = pageNo
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getSpcifyLunCalInfo",
            params=params,
            headers=self._headers,
        )
        result = response.json()
        return result

    def getJulDayInfo(self, solJd):
        """
        율리우스 적일을 기준으로 양력날짜, 음력날짜, 요일, 윤년, 평달/윤달 여부,
        음력 간지 등의 정보를 제공한다.
        검색 결과에서 양력날짜는 2299150일까지는 율리우스력 기준,
        2299161일부터는 그레고리력 기준 (참고로 2299151~2299160일 사이는 검색 결과 없음)
        입력범위: 제 2229156일 ∼ 제 2470172일
        """
        params = {
            "solJd": solJd,
        }
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getJulDayInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result
