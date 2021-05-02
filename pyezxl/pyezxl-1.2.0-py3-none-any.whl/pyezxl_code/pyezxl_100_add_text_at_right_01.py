#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("activeworkbook")
activesheet_name = excel.read_activesheet_name()
rng_select = excel.read_range_select()
print (rng_select)
#선택한 영역의 각셀의 값에 글자를 추가하는것

y_start, x_start, y_end, x_end= excel.read_range_select()
bbb=excel.read_messagebox_value("Please input text")


for y1 in range(int(y_start), int(y_end+1)):
	for x1 in range(int(x_start), int(x_end+1)):
		current_data = str(excel.read_cell_value(activesheet_name,[x1, y1]))
		if current_data == "None" : current_data = ""
		excel.write_cell_value(activesheet_name,[x1, y1],(str(current_data)+str(bbb)))