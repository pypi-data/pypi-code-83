#  -*- coding: utf-8 -*-
import pyezxl
excel = pyezxl.pyezxl("activeworkbook")

activesheet_name = excel.read_activesheet_name()
y_start, x_start, y_end, x_end= excel.read_range_select()[1]


#영역 안의 자료를 
selection_range=excel.read_range_select()[0]
datas=list(excel.read_range_value("activesheet",selection_range ))

temp=[]
result=[]
min_value=[]

print (datas)

input_text = excel.read_messagebox_value()

for data_xx in datas:
	temp_list=[]
	temp_num=0
	for data_x in data_xx:
		if str(input_text) in str(data_x) and data_x != None:
			excel.set_range_color(activesheet_name, [x_start, y_start+temp_num, x_start, y_start+temp_num], 6)
		temp_num= temp_num+1
	x_start = x_start+1






#for num_garo in range(len(datas)):
#	#리스트를 정렬하여 제일 처음의 자료와 비교를 해서, 그것과 같은 셀의값에 색깔을 넣는다
#	temp=list(datas[num_garo])
#	min_value = sorted(temp)
#	for num_sero in range(len(datas[0])):
#			if datas[num_garo][num_sero]==min_value[0]:
#				print(min_value)
#				garo = selection_range[1]+num_garo
#				sero = selection_range[0]+num_sero
#				excel.set_range_color(activesheet_name, [garo, sero], 6)
