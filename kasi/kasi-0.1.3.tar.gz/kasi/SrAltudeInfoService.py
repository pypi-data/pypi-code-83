import re

from urllib.parse import unquote

import pandas as pd
import requests


class SrAltudeInfoService:
    """
    지역별 태양고도 정보, 위치별 태양고도 정보를 조회하는 서비스 입니다.
    """

    locations = re.split(
        r",\s+",
        """
        강릉, 강화도, 거제, 거창, 경산, 경주,
        고성(강원), 고양, 고흥, 광양, 광주, 광주(경기), 구미, 군산, 김천, 김해, 남원,
        남해, 대관령, 대구, 대덕, 대전, 독도, 동해, 마산, 목포, 무안, 밀양, 변산,
        보령, 보성, 보현산, 부산, 부안, 부천, 사천, 삼척, 상주, 서귀포, 서산, 서울,
        서천, 성산일출봉, 세종, 소백산, 속초, 수원, 순천, 승주, 시흥, 아산, 안동,
        안산, 안양, 양양, 양평, 여수, 여수공항, 여주, 영광, 영덕, 영월, 영주, 영천,
        완도, 용인, 울릉도, 울산, 울진, 원주, 의성, 익산, 인천, 임실, 장수, 장흥,
        전주, 정읍, 제주, 제주(레), 제천, 주문진, 진도, 진주, 진해, 창원, 천안, 청주,
        청주공항, 추풍령, 춘양, 춘천, 충주, 태백, 태안, 통영, 파주, 평택, 포항, 해남,
        화성, 흑산도
        """.strip(),
    )

    def __init__(self, serviceKey):
        if "%" in serviceKey:
            serviceKey = unquote(serviceKey)
        self._endpoint = (
            "http://apis.data.go.kr/B090041/openapi/service/SrAltudeInfoService"
        )
        self._serviceKey = serviceKey
        self._headers = {
            "Accept": "application/json",
        }

    def getAreaSrAltudeInfo(self, locdate, location):
        """
        날짜와 지역을 기준으로 월별로 시간별 방위각, 태양고도, 남중고도 등의 정보를 제공한다.
        """
        if isinstance(locdate, int):
            locdate = str(locdate)
        assert location in self.locations
        params = {
            "locdate": pd.Timestamp(locdate).strftime("%Y%m%d"),
            "location": location,
        }
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getAreaSrAltudeInfo",
            params=params,
            headers=self._headers,
        )
        result = response.json()
        return result

    def getLCSrAltudeInfo(self, locdate, longitude, latitude, dnYn=None):
        """
        오퍼레이션 설명	날짜와 위치를 기준으로 월별로 시간별 방위각, 태양고도, 남중고도 등의 정보를 제공한다.
        """
        if isinstance(locdate, int):
            locdate = str(locdate)
        if dnYn is None:
            dnYn = "y"
        params = {
            "locdate": pd.Timestamp(locdate).strftime("%Y%m%d"),
            "longitude": longitude,
            "latitude": latitude,
            "dnYn": dnYn,
        }
        params["ServiceKey"] = self._serviceKey
        response = requests.get(
            self._endpoint + "/getLCSrAltudeInfo", params=params, headers=self._headers
        )
        result = response.json()
        return result
