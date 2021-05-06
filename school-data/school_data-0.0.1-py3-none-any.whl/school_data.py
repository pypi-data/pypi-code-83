import asyncio
import aiohttp
from datetime import datetime
import json
from io import StringIO

# -- 서울 강월초등학교 코드 --
# 시도 교육청: 서울특별시교육청 (B10)
# 학교 코드: 7081423


async def asyncNow(): # time function
    now = datetime.now()
    return now.strftime('%Y%m%d')

def now(loop=asyncio.get_event_loop()): # get now
    return loop.run_until_complete(asyncNow())


async def asyncMealData(country_code, school_code, meal_code=2, date=now()): # 급식 데이터
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?&Type=json&ATPT_OFCDC_SC_CODE={country_code}&SD_SCHUL_CODE={school_code}&MMEAL_SC_CODE={meal_code}&MLSV_YMD={date}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text() # data setting
                data = data.replace("<br/>", "")
                data = data.replace("*", ", ")
                data = StringIO(data)
                data = json.load(data)
                data = data["mealServiceDietInfo"]

                # -- meal data setting --
                school_data = data[1]['row'][0]
                return {"error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "area_name":school_data["ATPT_OFCDC_SC_NM"], "area_code":school_data["ATPT_OFCDC_SC_CODE"], "school_name": school_data["SCHUL_NM"], "school_code":school_data["SD_SCHUL_CODE"], "meal":school_data["DDISH_NM"], "nutrient": school_data["NTR_INFO"], "origin":school_data["ORPLC_INFO"]}
    except KeyError:
        return {"error": True, "code":"FORMET", "message":"입력하신 정보를 찾을수 없습니다."}

    except Exception as e:
        return {"error": True, "code":"UNKNOWN", "message":"알 수 없는 에러 발생."}

def meal_data(country_code, school_code, meal_code=2, date=now(), loop=asyncio.get_event_loop()):
    return loop.run_until_complete(asyncSchoolData(country_code=country_code, school_code=school_code, meal_code=meal_code, date=date))


async def asyncSchoolData(school_name):
    url = f"https://open.neis.go.kr/hub/schoolInfo?SCHUL_NM={school_name}&Type=json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text() # data setting
                data = StringIO(data)
                data = json.load(data)
                data = data["schoolInfo"]
                # -- school data setting --
                row = data[1]['row'][0]
                return {"error": False, "code":"SUCCESS", "message":"성공적으로 데이터를 불러왔습니다.", "area_code":row["ATPT_OFCDC_SC_CODE"], "area_code":row["ATPT_OFCDC_SC_NM"], "school_code":row["SD_SCHUL_CODE"], "school_name":row["SCHUL_NM"], "eng_school_name":row["ENG_SCHUL_NM"], "school_type":row["SCHUL_KND_SC_NM"], "phone_number":row["ORG_TELNO"], "website":row["HMPG_ADRES"], "location":row["ORG_RDNMA"], "fond":row["FOND_SC_NM"], "gender_type":row["COEDU_SC_NM"]}
    except KeyError:
        return {"error": True, "code":"FORMET", "message":"입력하신 학교를 찾을수 없습니다."}

def school_data(school_name, loop=asyncio.get_event_loop()):
    return loop.run_until_complete(asyncSchoolData(school_name=school_name))

# -- testing --