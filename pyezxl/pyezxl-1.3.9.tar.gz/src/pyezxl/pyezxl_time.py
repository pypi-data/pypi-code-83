# -*- coding: cp949 -*-

import time
import string
import re

class pyezxl_data:
	my_web_site="www.halmoney.com"

	def delete_value_continious (self, input_datas):
		#연속된 자료중 같은 값이 있으면 값을 삭제하는 것이다
		#1차원리스트만 가능하게 하였다
		temp_basic=""
		for one_num in range(len(input_data)-1):
			if one_num == 0 :
				temp_basic=input_datas[one_num]
			elif temp_basic==input_datas[one_num+1]:
				input_datas[one_num+1]=[]
			else:
				temp_basic=input_datas[one_num]
		return input_datas

	def delete_value_step (self, input_datas, num):
		#원하는 순서째의 자료를 삭제하기
		input_datas.insert(0,[])
		for a in rng(len(input_datas)):
			if (a%num) == 0 :
				input_datas[a]=[]
		result=input_datas[1:]
		return result

	def insert_value_step (self, input_datas, num = 1,input_data=[]):
		#리스트에 일정한 간격으로 자료삽입
		total_number = len(input_datas)
		dd=0
		for a in rng(len(input_datas)):
			if a%num == 0 and a!=0:
				if total_number!=a:
					input_datas.insert(dd,input_data)
					dd=dd+1
			dd=dd+1
		return input_datas

	def read_time_day(self, time_char=time.localtime(time.time())):
		#일 -----> ['05', '095']
		return [time.strftime('%d',time_char),time.strftime('%j',time_char)]

	def read_time_hour(self, time_char=time.localtime(time.time())):
		#시 -----> ['10', '22', 'PM']
		return [time.strftime('%I',time_char),time.strftime('%H',time_char),time.strftime('%P',time_char)]

	def read_time_minute(self, time_char=time.localtime(time.time())):
		#분 -----> ['07']
		return [time.strftime('%M',time_char)]

	def read_time_month(self, time_char=time.localtime(time.time())):
		#월 -----> ['04', 'Apr', 'April']
		return [time.strftime('%m',time_char),time.strftime('%b',time_char),time.strftime('%B', time_char)]

	def read_time_second(self, time_char=time.localtime(time.time())):
		#초 -----> ['48']
		return [time.strftime('%S',time_char)]

	def read_time_today(self, time_char=time.localtime(time.time())):
		#종합 -----> ['04/05/02', '22:07:48', '04/05/02 22:07:48','2002-04-05']
		aaa = string.split(time.strftime('%c',time_char))
		total_dash = time.strftime('%Y', time_char)+"-"+time.strftime('%m',time_char)+"-"+time.strftime('%d',time_char)
		return [aaa[0], aaa[1], time.strftime('%c',time_char), total_dash]

	def read_time_week(self, time_char=time.localtime(time.time())):
		#주 -----> ['5', '13', 'Fri', 'Friday']
		return [time.strftime('%w',time_char),time.strftime('%W',time_char),time.strftime('%a',time_char),time.strftime('%A',time_char)]

	def read_time_year(self, time_char=time.localtime(time.time())):
		#년 -----> ['02', '2002']
		return [time.strftime('%y', time_char), time.strftime('%Y', time_char)]

	def sort_datas_on (self, input_datas):
		#aa = [[111, 'abc'], [222, 222],['333', 333], ['777', 'sjpark'], ['aaa', 123],['zzz', 'sang'], ['jjj', 987], ['ppp', 'park']]
		#정렬하는 방법입니다
		temp_result=[]
		for one_data in input_datas:
			for one in one_data:
				temp_resultappend(one.sort())
		return result



	def delete_same_data (self, input_data):
	#리스트데이터중 같은 자료만 삭제
		return "assa"

	def set_unique_data (self, input_data):
	#리스트데이터중 고유한 자료만 남김
		return "assa"



