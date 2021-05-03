# -*- coding: utf-8 -*-

import win32com.client
import re
import string
import win32gui

class pyezxl:
    my_web_site = "www.halmoney.com"

    def __init__(self, filename=None):
        # 만약 화일의 경로가 있으면 그 화일을 열도록 한다
        self.xlApp = win32com.client.dynamic.Dispatch('Excel.Application')
        self.xlApp.Visible = 1
        self.filename = filename.lower()

        if self.filename == 'activeworkbook' or self.filename == '':
            # activeworkbook으로 된경우는 현재 활성화된 workbook을 그대로 사용한다
            self.xlBook = self.xlApp.ActiveWorkbook
            if self.xlBook == None:
                # 만약 activework북을 부르면서도 화일이 존재하지 않으면 새로운 workbook을 만드는것이다
                try:
                    self.xlApp.WindowState = -4137
                    self.xlBook = self.xlApp.WorkBooks.Add()
                except:
                    win32gui.MessageBox(0, "There is no Activeworkbook", self.my_web_site, 0)

        elif not (self.filename == 'activeworkbook') and self.filename:
            # 만약 화일이름이 따로 주어지면 그화일을 연다
            try:
                self.xlApp.WindowState = -4137
                self.xlBook = self.xlApp.Workbooks.Open(self.filename)
            except:
                win32gui.MessageBox(0, "Please check file path", self.my_web_site, 0)
        else:
            # 빈것으로 된경우는 새로운 workbook을 하나 열도록 한다
            self.xlApp.WindowState = -4137
            self.xlBook = self.xlApp.WorkBooks.Add()

    def change_char_num(self, input_data):
        # input_data : aa => result : 27
        # 문자를 숫자로 바꿔주는 것
        if input_data.isalpha():
            input_data = input_data.lower()
            reversed_input_data = ''.join(reversed(input_data))
            temp_result = [ord(letter) - 96 for letter in reversed_input_data]
            result = 0
            for one in range(len(temp_result)):
                result = result + pow(26, one) * temp_result[one]
        else:
            result = input_data
        return int(result)

    def change_num_char(self, input_data):
        base_number = int(input_data)
        result_01 = ''
        result = []
        while base_number > 0:
            div = base_number // 26
            mod = base_number % 26
            if mod == 0:
                mod = 26
                div = div - 1
            base_number = div
            result.append(mod)
        for one_data in result:
            result_01 = string.ascii_lowercase[one_data - 1] + result_01
        return result_01

    def change_sheet_name(self, sheet_name_old, sheet_name_new):
        # 시트이름을 바꿉니다
        self.xlBook.Worksheets(sheet_name_old).Name = sheet_name_new

    def change_x_y(self, input_data):
        result = self.swap_list_data(input_data)
        return result

    def check_address_value(self, address):
        # input_data : [1,2],[1,1,2,3],[$A$1], [$A$1:$B$2], [$1:$7], [$A:$B], [A1]
        # output_data : [1,2],[1,1,2,3],[1,1], [1,1,2,2], [1,0,7.0], [0,1,0,2], [1,1]
        # 결과값은 [x1, y1, x2, y2]의 형태이다
        check_string = re.compile(r"([:$a-zA-Z]+)")
        check_range = re.compile(r"([:]+)")
        check_num = re.compile(r"([0-9]+)")

        result_final = []
        result_final_01 = []
        result_final_02 = []

        #빈것이면 현재 선택한 영역을 돌려준다
        if address == "":
            address = self.read_range_select()
        elif type(address) != type([]):
            address = [address]

        for one_data in address:
            one_data = str(one_data)
            one_data = one_data.replace('$', '')
            result_temp = []
            result_final_01=[]
            result_final_02=[]
            data_type = {"range": "no", "num_only": "no", "string_only": "no"}
            # 어떤 형태의 주소인지 확인한다

            if check_range.findall(one_data):
                data_type["range"] = "yes"
            if check_num.findall(one_data.split(":")[0]):
                data_type["num_only"] = "yes"
            if check_string.findall(one_data.split(":")[0]):
                data_type["string_only"] = "yes"

            if data_type["range"] == "no" and data_type["num_only"] == "yes" and data_type["string_only"] == "no":
                # [1, 2], [1, 1, 2, 3] => 이런형태이므로 그대로 값을 넣어준다
                result_temp.append(one_data)

            if data_type["range"] == "no" and data_type["num_only"] == "no" and data_type["string_only"] == "yes":
                # [$A$1], [A1] => 이런형태
                temp_value = self.split_eng_num(one_data)
                temp_value1 = self.change_char_num(temp_value[0])
                result_temp.append(int(temp_value[1]))
                result_temp.append(int(temp_value1))

            if data_type["range"] == "no" and data_type["num_only"] == "yes" and data_type["string_only"] == "yes":
                # [$A$1], [A1] => 이런형태
                temp_value = self.split_eng_num(one_data)
                temp_value1 = self.change_char_num(temp_value[0])
                result_temp.append(int(temp_value[1]))
                result_temp.append(int(temp_value1))

            if data_type["range"] == "yes" and data_type["num_only"] == "yes" and data_type["string_only"] == "yes":
                # [$A$1:$B$2] => 이런형태
                for data_001 in one_data.split(":"):
                    temp_value = self.split_eng_num(data_001)
                    temp_value1 = self.change_char_num(temp_value[0])
                    result_temp.append(int(temp_value[1]))
                    result_temp.append(int(temp_value1))

            if data_type["range"] == "yes" and data_type["num_only"] == "no" and data_type["string_only"] == "yes":
                # [$A:$B] => 이런형태
                for data_001 in one_data.split(":"):
                    result_temp.append(int(0))
                    temp_value = self.change_char_num(data_001)
                    result_temp.append(int(temp_value))

            if data_type["range"] == "yes" and data_type["num_only"] == "yes" and data_type["string_only"] == "no":
                # [$1:$7] => 이런형태
                aaa = one_data.split(":")
                for data_001 in aaa:
                    result_temp.append(int(data_001))
                    result_temp.append(int(0))

            result_final.extend(result_temp)
        if len(result_final) == 2: result_final_01=[int(result_final[0]), int(result_final[1]), int(result_final[0]), int(result_final[1])]
        if len(result_final) == 4: result_final_01=[int(result_final[0]), int(result_final[1]), int(result_final[2]), int(result_final[3])]

        #혹시 입력한 자료가 [1,2,3,4]의 형태가 아닌 [3,4,1,2]로 되어잇을때 정렬을 다시하는것이다
        temp1 = [result_final_01[0], result_final_01[2]]
        temp1.sort()

        temp2 = [result_final_01[1], result_final_01[3]]
        temp2.sort()

        result_final_02 = [temp1[0], temp2[0], temp1[1], temp2[1]]

        return result_final_02

    def check_range_value(self, xyxy):
        if xyxy == "":
            result = self.read_activecell_range()
        else:
            x1, y1, x2, y2 = self.check_address_value(xyxy)
            result= x1, y1, x2, y2
        return result

    def check_range_address(self, xyxy):
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        xyxy_new = x1, y1, x2, y2
        return xyxy_new

    def check_sheet_name(self, sheet_name=""):
        # sheet이름을 확인해서 돌려준다. 아무것도 없으면 activesheet를 돌려준다
        if str(sheet_name).lower() == "activesheet" or sheet_name == "":
            sheet = self.xlApp.ActiveSheet
        else:
            sheet = self.xlBook.Worksheets(sheet_name)
        return sheet

    def check_y_empty(self, sheet_name, y):
        # 열전체가 빈 것인지 확인해서 돌려준다
        # 전체가 비었을때는 0을 돌려준다
        sheet = self.check_sheet_name(sheet_name)
        result = self.xlApp.WorksheetFunction.CountA(sheet.Columns(y).EntireColumn)
        return result

    def check_x_empty(self, sheet_name, x):
        # 열전체가 빈 것인지 확인해서 돌려준다
        # 전체가 비었을때는 0을 돌려준다
        sheet = self.check_sheet_name(sheet_name)
        result = self.xlApp.WorksheetFunction.CountA(sheet.Rows(x).EntireRow)
        return result

    def copy_range_x(self, sheet_name1, sheet_name2, cut_num, paste_num):
        # row의 값을 복사합니다
        sheet1 = self.check_sheet_name(sheet_name1)
        sheet2 = self.check_sheet_name(sheet_name2)

        self.xlBook.Worksheets(sheet_name1).Columns(str(cut_num) + ':' + str(cut_num)).Copy()
        self.xlBook.Worksheets(sheet_name2).Columns(str(paste_num) + ':' + str(paste_num)).Select()
        self.xlBook.Selection.PasteSpecial(Paste=-4163)

    def copy_range_y(self, sheet_name1, sheet_name2, cut_num, paste_num):
        sheet1 = self.check_sheet_name(sheet_name1)
        sheet2 = self.check_sheet_name(sheet_name2)

        num_r1 = self.change_num_char(cut_num)
        num_r2 = self.change_num_char(paste_num)

        sheet1.Range(str(num_r1) + ':' + str(num_r1)).Copy()
        sheet2.Range(str(num_r2) + ':' + str(num_r2)).Select()
        sheet2.Paste()

    def delete_range_color(self, sheet_name, xyxy):
        # 영역의 모든 색을 지운다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Interior.Pattern = -4142
        my_range.Interior.TintAndShade = 0
        my_range.Interior.PatternTintAndShade = 0

    def delete_line_x(self, sheet_name, num):
        # 한줄삭제하기
        #num = self.change_char_num(num)
        sheet = self.check_sheet_name(sheet_name)
        sheet.Rows(str(num) + ':' + str(num)).Delete(-4121)

    def delete_line_y(self, sheet_name, num):
        # 한줄삭제하기
        sheet = self.check_sheet_name(sheet_name)
        num_check = self.change_num_char(num)
        sheet.Columns(str(num_check) + ':' + str(num_check)).Delete()

    def delete_range_line(self, sheet_name, xyxy):
        # 영역의 모든 선을 지운다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        for each in [5, 6, 7, 8, 9, 10, 11, 12]:
            sheet.Range(sheet.Cells(int(x1), int(y1)), sheet.Cells(int(x2), int(y2))).Borders(each).LineStyle = -4142

    def delete_range_name(self, range_name):
        result = self.xlBook.Names(range_name).Delete()
        return result

    def delete_range_samevalue(self, xyxy):
        # 같은값이 있으면 그자리를 비우는 것이다
        temp_result = []
        select_range = self.read_range_select()
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        sheet = self.check_sheet_name("")

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                temp_data = self.read_cell_value(sheet, [x, y])
                if temp_data in temp_result:
                    self.write_cell_value(sheet, [x, y], "")
                else:
                    temp_result.append(temp_data)

    def delete_range_value(self, sheet_name, xyxy):
        # 선택한영역에서 값을 clear기능을 한다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.ClearContents()

    def delete_range_x(self, sheet_name, num):
        # 한줄삭제하기
        num = self.change_char_num(num)
        sheet = self.check_sheet_name(sheet_name)
        sheet.Rows(str(num) + ':' + str(num)).Delete(-4121)

    def delete_range_y(self, sheet_name, num):
        # 한줄삭제하기
        sheet = self.check_sheet_name(sheet_name)
        num_check = self.change_num_char(num)
        sheet.Columns(str(num_check) + ':' + str(num_check)).Delete()

    def delete_sheet(self, sheet_name=""):
        # 시트하나 삭제하기
        sheet = self.check_sheet_name(sheet_name)
        self.xlApp.DisplayAlerts = False
        sheet.Delete()
        self.xlApp.DisplayAlerts = True

    def delete_sheet_drawing(self, sheet_name=""):
        sheet = self.check_sheet_name(sheet_name)
        for aa in range(sheet.Shapes.Count, 0, -1):
            # Range를 앞에서부터하니 삭제하자마자 번호가 다시 매겨져서, 뒤에서부터 삭제하니 잘된다
            sheet.Shapes(aa).Delete()
        return

    def delete_sheet_value(self, sheet_name):
        # 시트의 모든 값을 삭제한다
        sheet = self.check_sheet_name(sheet_name)
        sheet.Cells.ClearContents()

    def fun_trim(self, input_data):
        aaa = self.xlApp.WorksheetFunction.Trim(input_data)
        return aaa

    def fun_ltrim(self, input_data):
        aaa = self.xlApp.WorksheetFunction.LTrim(input_data)
        return aaa

    def fun_rtrim(self, input_data):
        aaa = self.xlApp.WorksheetFunction.RTrim(input_data)
        return aaa

    def insert_line_x(self, sheet_name, num):
        # 한줄삽입하기
        sheet = self.check_sheet_name(sheet_name)
        sheet.Range(str(num_r1) + ':' + str(num_r1)).Insert()

    def insert_line_y(self, sheet_name, num):
        # 한줄삽입하기
        sheet = self.check_sheet_name(sheet_name)
        num_r1 = self.change_num_char(num)
        sheet.Columns(str(num_r1) + ':' + str(num_r1)).Insert()

    def insert_range_button(self, sheet_name, xyxy, macro, title):
        # 버튼을 만들어서 그 버튼에 매크로를 연결하는 것이다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        new_btn = sheet.Buttons()
        new_btn.Add(x1, x2, y1, y2)
        new_btn.OnAction = macro
        new_btn.Text = title

    def insert_range_picture(self, sheet_name="", file_name=""):
        sheet = self.check_sheet_name(sheet_name)
        sheet.Shapes.AddPicture(file_name, 0, 1, 541.5, 92.25, 192.75, 180)

    def insert_sheet_new(self):
        # 시트하나 추가하기
        self.xlBook.Worksheets.Add()

    def intersect_range1_range2(self, rng1, rng2):
        # 두개의 영역에서 교차하는 구간을 돌려준다
        # 만약 교차하는게 없으면 ""을 돌려준다
        range_1= self.check_range_address(rng1)
        range_2 = self.check_range_address(rng2)

        x11, y11, x12, y12 = range_1
        x21, y21, x22, y22 = range_2

        if x11==0 :
           x11 = 1
           x12=1048576
        if x21==0 :
           x21 = 1
           x22=1048576
        if y11==0 :
           y11 = 1
           y12=16384
        if y21==0 :
           y21 = 1
           y22=16384

        new_range_x = [x11, x21, x12, x22]
        new_range_y = [y11, y21, y12, y22]

        new_range_x.sort()
        new_range_y.sort()

        if x11<= new_range_x[1] and x12>= new_range_x[2] and y11<= new_range_y[1] and y12>= new_range_y[1] :
            result = [new_range_x[1], new_range_y[1], new_range_x[2], new_range_y[2]]
        else:
            result ="교차점없음"
        return result


    def move_down_end(self, sheet_name="", xyxy=""):
        # 선택한 위치에서 끝부분으로 이동하는것
        # xlDown  : - 4121,  xlToLeft : - 4159, xlToRight  : - 4161, xlUp : - 4162
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        sheet.Cells(x1, y1).End(- 4121).Select()
        return "ok"

    def move_left_end(self, sheet_name="", xyxy=""):
        # 선택한 위치에서 끝부분으로 이동하는것
        # xlDown  : - 4121,  xlToLeft : - 4159, xlToRight  : - 4161, xlUp : - 4162
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        sheet.Cells(x1, y1).End(- 4159).Select()
        return "ok"

    def move_right_end(self, sheet_name="", xyxy=""):
        # 선택한 위치에서 끝부분으로 이동하는것
        # xlDown  : - 4121,  xlToLeft : - 4159, xlToRight  : - 4161, xlUp : - 4162
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        sheet.Cells(x1, y1).End(- 4161).Select()
        return "ok"

    def move_up_end(self, sheet_name="", xyxy=""):
        # 선택한 위치에서 끝부분으로 이동하는것
        # xlDown  : - 4121,  xlToLeft : - 4159, xlToRight  : - 4161, xlUp : - 4162
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        sheet.Cells(x1, y1).End(- 4162).Select()
        return "ok"

    def read_activesheet_name(self):
        # 현재의 엑셀중에서 활성화된 시트의 이름을 돌려준다
        return self.xlApp.ActiveSheet.Name

    def read_activecell_value(self):
        # 돌려주는 값 ['행번호','열번호','현재셀의 값']
        value = self.xlApp.ActiveCell.Value
        xy = self.check_address_value(self.xlApp.ActiveCell.Address)
        return [xy[1], xy[0], value]

    def read_activecell_range(self):
        # 돌려주는 값 [x, y]
        xyxy = self.check_address_value(self.xlApp.ActiveCell.Address)
        return xyxy

    def read_cell_value(self, sheet_name, xy):
        # 값을 일정한 영역에서 갖고온다
        # 만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
        sheet = self.check_sheet_name(sheet_name)
        result = sheet.Cells(int(xy[0]), int(xy[1])).value
        return result

    def read_continousrange_value(self, sheet_name, xyxy):
        # 현재선택된 셀을 기준으로 연속된 영역을 가지고 오는 것입니다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)

        bottom = row  # 아래의 행을 찾는다
        while sheet.Cells(bottom + 1, col).Value not in [None, '']:
            bottom = bottom + 1
        right = col  # 오른쪽 열
        while sheet.Cells(row, right + 1).Value not in [None, '']:
            right = right + 1
        return sheet.Range(sheet.Cells(x1, y1), sheet.Cells(bottom, right)).Value

    def read_messagebox_value(self, text_01="www.halmoney.com"):
        result = self.xlApp.InputBox(text_01)
        return result

    def read_range_currentregion(self):
        # 이것은 현재의 셀에서 공백과 공백열로 둘러싸인 활성셀영역을 돌려준다
        result = self.check_address_value(self.xlApp.ActiveCell.CurrentRegion.Address)[1]
        return result

    def read_range_name(self):
        names_count = self.xlBook.Names.Count
        result = []
        if names_count > 0:
            for aaa in range(1, names_count + 1):
                name_name = self.xlBook.Names(aaa).Name
                name_range = self.xlBook.Names(aaa)
                result.append([aaa, str(name_name), str(name_range)])
        return result

    def read_range_name_01(self):
        # 이름을 삭제한다
        aaa = self.xlApp.Names
        return aaa

    def read_range_select(self):
        # 현재선택된 영역의 주소값을 돌려준다
        result = self.check_address_value(self.xlApp.Selection.Address)
        print (result)
        return result

    def read_range_usedrange(self, sheet_name=""):
        # 이것은 usedrange를 돌려주는 것이다. 값은 리스트이며 처음은
        # usedrange의 시작셀 ,두번째는 마지막셀값이며 세번째는 전체영역을 돌려주는 것이다
        sheet = self.check_sheet_name(sheet_name)
        result = self.check_address_value(sheet.usedrange.address)
        return result

    def read_range_value(self, sheet_name, xyxy):
        # 값을 일정한 영역에서 갖고온다
        # 만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        print(x1, y1, x2, y2)
        result = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Value
        return result

    def read_sheet_count(self):
        # 시트의 갯수를 돌려준다
        return self.xlBook.Worksheets.Count

    def read_sheet_name(self):
        # 현재 워크북의 모든 시트알아내기
        temp_list = []
        for var_02 in range(1, self.read_sheet_count() + 1):
            temp_list.append(self.xlBook.Worksheets(var_02).Name)
        return temp_list

    def read_workbook_fullname(self):
        # application의 이름과 전체경로를 돌려준다
        return self.xlBook.FullName

    def read_workbook_name(self):
        # application의 이름을 돌려준다
        return self.xlBook.Name

    def read_workbook_path(self):
        # application의 경로를 돌려준다
        return self.xlBook.Path

    def read_workbook_username(self):
        return self.xlApp.Username

    def read_x_value(self, sheet_name, x):
        # 한 가로행의 전체값을 갖고온다
        sheet = self.check_sheet_name(sheet_name)
        result = sheet.Cells(x, 1).EntireRow.Value
        return result

    def select_sheet_range(self, sheet_name, xyxy):
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Select()

    def set_range_select(self, sheet_name, xyxy):
        self.select_sheet_range(sheet_name, xyxy)

    def set_cell_bold(self, sheet_name, xyxy):
        # 셀안의 값을 진하게 만든다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Font.Bold = True

    def set_range_autofilter(self, sheet_name, row1, row2=None):
        # 엑셀의 자동필터 기능을 추가한 것입니다
        sheet = self.check_sheet_name(sheet_name)
        if row2 == None:
            row2 = row1
        a = str(row1) + ':' + str(row2)
        sheet.Rows(a).Select()
        sheet.Range(a).AutoFilter(1)

    def set_cell_color(self, sheet_name, xy, input_data):
        # 영역에 색깔을 입힌다
        sheet = self.check_sheet_name(sheet_name)
        my_range = sheet.Cells(xy[0], xy[1])
        my_range.Interior.ColorIndex = input_data

    def set_range_color(self, sheet_name, xyxy, input_data):
        # 영역에 색깔을 입힌다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Interior.ColorIndex = input_data

    def set_range_font(self, sheet_name, xyxy, font):
        # 영역에 글씨체를 설정한다
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.font.Name = font

    def set_range_fontsize(self, sheet_name, xyxy, input_data):
        # 영역에 글씨크기를 설정한다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.font.Size = input_data

    def set_range_formula(self, sheet_name, xyxy, input_data):
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Formula = input_data

    def set_range_line(self, sheet_name, xyxy, value):
        # 안쪽의 선들지정
        # [선의위치, 라인스타일, 굵기, 색깔]
        # 선의위치 (5-대각선 오른쪽, 6-왼쪽대각선, 7:왼쪽, 8;위쪽, 9:아래쪽, 10:오른쪽, 11:안쪽세로, 12:안쪽가로)
        # 라인스타일 (1-실선, 2-점선, 3-가는점선, 6-굵은실선,
        # 굵기 (0-이중, 1-얇게, 2-굵게)
        # 색깔 (0-검정, 1-검정3-빨강),
        # [[7,1,2,1],[8,1,2,1],[9,1,2,1],[10,1,2,1], [12,3,1,1], [11,1,2,1] ]

        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))

        for data in value:
            my_range.Borders(data[0]).LineStyle = data[1]
            my_range.Borders(data[0]).Weight = data[2]
            my_range.Borders(data[0]).ColorIndex = data[3]

    def set_range_merge(self):
        # 2004년 10월 08일 추가
        area = self.read_range_select()
        worksheet_name = self.read_activesheet_name()
        for a in range(area[3] - area[1] + 1):
            arange = [area[0], area[1] + a, area[2], area[1] + a]
            self.write_range_merge(worksheet_name, arange)

    def set_range_merge_v01(self, sheet_name, xyxy):
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        for a in range(y2 - y1 + 1):
            arange = [x1, y1 + a, x2, y1 + a]
            self.write_range_merge(sheet, arange)

    def set_range_numberformat(self, sheet_name, xyxy, numberformat):
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.NumberFormat = numberformat

    def set_range_wellusedline(self):
        # 자주 사용하는 테두리선을 지정해 놓고 사용을 하는것
        # 이 코드는 선택된 영역의 테두리선을 긋는 것과 맨앞부분에 글자가 있는 부분을 색깔을 칠하는것
        # 만약 화일의 경로가 있으면 그 화일을 열도록 한다
        # [위치, 선종류, 스타일, 색깔, 굵기]

        # Borders위치 (7:왼쪽, 8;위쪽, 9:아래쪽, 10:오른쪽, 11:안쪽세로, 12:안쪽가로)
        # Weight 선종류 ( 1: 많이 얇은,  2: 얇은선, -4138: 보통, 4:두꺼운
        # LineStyle 선스타일 (1 : 실선, -4115 : 점선, -4119: 이중라인)
        # ColorIndex선색 (1: 검정, 3:빨강)

        well_used_line = [[12, 1, 1, 1], [11, 2, 1, 1], [8, -4138, 1, 1], [10, -4138, 1, 1], [9, -4138, 1, 1],
                          [7, -4138, 1, 1]]

        sheet = self.check_sheet_name()
        x1, y1, x2, y2 = self.read_range_select()
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range_top = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x1, y2))
        my_range_bottom = sheet.Range(sheet.Cells(x2, y1), sheet.Cells(x2, y2))

        for data in well_used_line:
            for range_data in [my_range, my_range_top, my_range_bottom]:
                range_data.Borders(data[0]).Weight = data[1]
                range_data.Borders(data[0]).LineStyle = data[2]
                range_data.Borders(data[0]).ColorIndex = data[3]

    def set_sheet_fullscreen(self, fullscreen=1):
        # 전체화면으로 보기
        self.xlApp.DisplayFullScreen = fullscreen

    def set_sheet_gridline(self):
        # 그리드 라인을 계속 바꾼다
        if self.xlApp.ActiveWindow.DisplayGridlines == 0:
            self.xlApp.ActiveWindow.DisplayGridlines = 1
        else:
            self.xlApp.ActiveWindow.DisplayGridlines = 0

    def set_sheet_preview(self, sheet_name=""):
        # 미리보기기능입니다
        sheet = self.check_sheet_name(sheet_name)
        sheet.PrintPreview()

    def set_sheet_visible(self, input_data=0):
        # 실행되어있는 엑셀을 화면에 보이지 않도록 설정합니다
        self.xlApp.Visible = input_data

    def set_x_length(self, sheet_name, x, height=13.5):
        sheet = self.check_sheet_name(sheet_name)
        sheet.Cells(x, 1).EntireRow.RowHeight = height

    def set_y_length(self, sheet_name, y, length=8.38):
        # 열이나 행의 넓이를 조절한다
        # 엑셀은 기본적으로 넓이는 8.38 로, 높이는 13.5로 되어있읍니다
        sheet = self.check_sheet_name(sheet_name)
        sheet.Cells(1, y).EntireColumn.ColumnWidth = length

    def set_y_numberproperty(self, sheet_name, y, style):
        # 각 열을 기준으로 셀의 속성을 설정하는 것이다
        sheet = self.check_sheet_name(sheet_name)
        if style == 1:  # 날짜의 설정
            sheet.Columns(y).NumberFormatLocal = "mm/dd/yy"
        elif style == 2:  # 숫자의 설정
            sheet.Columns(y).NumberFormatLocal = "_-* #,##0.00_-;-* #,##0.00_-;_-* '-'_-;_-@_-"
        elif style == 3:  # 문자의 설정
            sheet.Columns(y).NumberFormatLocal = "@"

    def set_workbook_close(self):
        # 현재는 close를 시키면 엑셀워크북만이 아니라 엑셀자체도 종료 시킵니다
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def set_workbook_fullscreen(self, fullscreen=1):
        # 전체화면으로 보기
        self.xlApp.DisplayFullScreen = fullscreen

    def set_workbook_hide(self):
        # 실행되어있는 엑셀을 화면에 보이지 않도록 설정합니다
        # visible로 통합
        self.xlApp.Visible = 0

    def set_workbook_save(self, newfilename=None):
        # 별도의 지정이 없으면 기존의 화일이름으로 저장합니다
        if newfilename:
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()

    def set_range_name(self, sheet_name):
        sheet = self.check_sheet_name(sheet_name)
        sheet.Range("B1:B10").Name = "asdasd"
        return "ok"

    def set_wrap_on(self, sheet_name, xyxy, input_data):
        # 셀의 줄바꿈을 설정할때 사용한다
        # 만약 status를 false로 하면 줄바꿈이 실행되지 않는다.
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        sheet = self.check_sheet_name(sheet_name)
        my_range.WrapText = input_data

    def show_messagebox_value(self, input_data, web="www.halmoney.com"):
        win32gui.MessageBox(0, input_data, web, 0)

    def sort_range_unique(self, sheet_name, xyxy):
        # 선택한 자료중에서 고유한 자료만을 골라내는 것이다
        # 자료중에서 고유한것을 찾아내서, 선택영역에 다시 쓴다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        temp_datas = self.read_range_value(sheet, xyxy)
        temp_result = []
        for one_list_data in temp_datas:
            for one_data in one_list_data:
                if one_data in temp_result or type(one_data) == type(None):
                    pass
                else:
                    temp_result.append(one_data)
        self.delete_range_value(sheet, xyxy)

        for num in range(len(temp_result)):
            mox, namuji = divmod(num, x2 - x1 + 1)
            self.write_cell_value(sheet, [x1 + namuji, y1 + mox], temp_result[num])

    def split_eng_num(self, data):
        # 단어중에 나와있는 숫자, 영어를 분리하는기능
        re_compile = re.compile(r"([a-zA-Z]+)([0-9]+)")
        result = re_compile.findall(data)
        new_result = []
        for dim1_data in result:
            for dim2_data in dim1_data:
                new_result.append(dim2_data)
        return new_result

    def split_range_unmerge(self, sheet_name, xyxy):
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Range(xyxy).UnMerge()

    def swap(self, a, b):
        t = a
        a = b
        b = t
        return [a, b]

    def swap_cap_small(self, sheet_name, xyxy):
        temp_result = []
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                temp_data = self.read_cell_value(sheet, [x, y])
                self.write_cell_value(sheet, [x, y], string.swapcase(temp_data))

    def swap_list_data(self, input_data):
        # input_data : [a, b, c, d]
        # result : [b, a, d, c]
        # 두개의 자료들에 대해서만 자리를 바꾸는 것이다
        result = []
        for one_data in range(int(len(input_data) / 2)):
            result.append(input_data[one_data * 2 + 1])
            result.append(input_data[one_data * 2])
        return result

    def write_cell_picture(self, sheet_name, xy, full_path):
        sheet = self.check_sheet_name(sheet_name)
        sheet.Cells(xy[0], xy[1]).Select()
        aaa = sheet.Pictures
        aaa.Insert(full_path).Select()

    def write_cell_value(self, sheet_name, xy, value):
        # 값을 셀에 넣는다. (사용법) write_cell(시트이름, 행번호, 열번호, 넣을값)
        sheet = self.check_sheet_name(sheet_name)
        sheet.Cells(xy[0], xy[1]).Value = value

    def write_line_merge(self, sheet_name, xyxy):
        # 셀들을 합하는 것이다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        if x1 == x2:
            sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Merge(0)
        else:
            for a in xyxy(y2 - y1 + 1):
                sheet.Range(sheet.Cells(y1 + a, x1), sheet.Cells(y1 + a, x2)).Merge(0)

    def write_range_clear(self, sheet_name, xyxy):
        # clear기능을 한다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.ClearContents()

    def write_range_list(self, sheet_name, xyxy, list_datas):
        x_length = 0
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)

        for line in list_datas:
            sheet.Range(sheet.Cells(x1 + x_length, y1),
                        sheet.Cells(x1 + x_length, y1 + len(line) - 1)).value = line
            x_length = x_length + 1

    def write_range_merge(self, sheet_name, xyxy):
        # 셀들을 합하는 것이다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Merge(0)

    def write_range_name(self, name, xyxy):
        # 영역을 이름으로 설정하는 기능
        self.xlBook.Names.Add(name, xyxy)

    def write_range_value(self, sheet_name, xyxy, input_datas):
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        y_count = len(input_datas)
        step_y = 0

        for one_value in input_datas:
            step_x = len(one_value)
            if y_count + 1 < step_y:
                return
            else:
                y1_new = y1 + step_y

            if x2 - x1 + 1 > step_x:
                x2_new = x1 + step_x - 1
            else:
                x2_new = x2

            sheet.Range(sheet.Cells(y1_new, x1), sheet.Cells(y1_new, x2_new)).value = one_value
            step_y = step_y + 1

    def write_range_wrap(self, sheet_name, xyxy, input_data):
        # 셀의 줄바꿈을 설정할때 사용한다
        # 만약 status를 false로 하면 줄바꿈이 실행되지 않는다.
        sheet = self.check_sheet_name(sheet_name)
        sheet.Range(xyxy).WrapText = input_data


    def intersect_range1_range2(self, rng1, rng2):
        # 두개의 영역에서 교차하는 구간을 돌려준다
        # 만약 교차하는게 없으면 ""을 돌려준다
        rng11 = self.check_range_address(rng1)
        rng21 = self.check_range_address(rng2)
        rx11, ry11, rx12, ry12 = rng11
        rx21, ry21, rx22, ry22 = rng21

        new_range = [1,1,1,1]
        if rx21 > rx11 and rx21 < rx12: new_range[0] = rx21
        if rx22 > rx11 and rx22 < rx12: new_range[2] = rx22

        if ry21 > ry11 and ry21 < ry12: new_range[1] = ry21
        if ry22 > ry11 and ry22 < ry12: new_range[3] = ry22

        if new_range == rng1:
            new_range = ""
        return new_range


    def set_range_rgbcolor(self, sheet_name, xyxy, input_data):
        # 영역에 색깔을 입힌다
        # 엑셀에서의 색깔의 번호는 아래의 공식처럼 만들어 진다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        rgb_to_int = (int(input_data[2]))*(256**2)+(int(input_data[1]))*(256)+int(input_data[0])
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Interior.Color = rgb_to_int

    def set_range_nocolor(self, sheet_name, xyxy):
        # 영역에 선의색을 다 없애는것
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = xyxy
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Interior.Pattern = 0
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Interior.PatternTintAndShade = 0

    def delete_range_line (self, sheet_name, xyxy):
        # 영역에 선의색을 다 없애는것
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = xyxy
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Borders.LineStyle = 0
        #sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2)).Interior.PatternTintAndShade = 0

    def delete_range_link(self, sheet_name, xyxy):
        # 영역의 모든 색을 지운다
        sheet = self.check_sheet_name(sheet_name)
        x1, y1, x2, y2 = self.check_address_value(xyxy)
        my_range = sheet.Range(sheet.Cells(x1, y1), sheet.Cells(x2, y2))
        my_range.Hyperlinks.Delete()

    def set_range_fontsize(self, sheet_name, xyxy, input_data):
        # 영역에 글씨크기를 설정한다
        sheet = self.check_sheet_name(sheet_name)
        y1, x1, y2, x2 = xyxy
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(y2, x2)).font.Size = int(input_data)

    def set_range_font(self, sheet_name, xyxy, font):
        # 영역에 글씨체를 설정한다
        sheet = self.check_sheet_name(sheet_name)
        y1, x1, y2, x2 = xyxy
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(y2, x2)).font.Name = font


    def set_range_fontcolor(self, sheet_name, xyxy, font_name):
        # 영역에 글씨체를 설정한다
        sheet = self.check_sheet_name(sheet_name)
        y1, x1, y2, x2 = xyxy
        sheet.Range(sheet.Cells(x1, y1), sheet.Cells(y2, x2)).Font.ColorIndex = font_name

