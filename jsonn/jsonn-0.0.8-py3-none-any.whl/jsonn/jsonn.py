import os
import io
import numpy
import chardet
import pandas as pd

class Jsonn:
    def __init__(self):
        self.__data_frame = None
        self.__file = None
        self.__array = None
    def load_file(self,file,path=None):
        if path==None:
            self.__file = file
        else:
            self.__file = os.path.join(path,file)
        self.__data_frame = pd.read_json(self.__file)

    def load_string(self,txt):
        self.__data_frame = pd.read_json(txt)

    def display(self):
        print(self.__data_frame)

    def get_data_frame(self):
        return self.__data_frame

    def get_rows_count(self):
        return len(self.__data_frame.index)

    def get_cols_count(self):
        return len(self.__data_frame.columns)

    def skip_rows(self, n):
        self.__data_frame = self.__data_frame.iloc[n:]

    def get_column_names(self):
        return self.__data_frame.columns

    def get_column_data(self,column_name):
        columns = self.get_column_names()
        if column_name in columns:
            return self.__data_frame[column_name]
        else:
            return None

    def __to_series(self):
        return self.__data_frame.stack()

    def set_data(self, data):
        self.__data_frame = pd.DataFrame(data)

    def get_head_rows(self,num_rows):
        return self.__data_frame.head(num_rows)

    def get_row_at(self,row_id):
        return self.__to_series().loc[row_id]

    def get_row_col_at(self,row_id,col_id):
        return self.__to_series().loc[row_id].iat[col_id]

    def convert_to_csv(self,sep=',',line_terminator=os.linesep):
        return self.__data_frame.to_csv()

    def convert_to_html(self):
        return self.__data_frame.to_html()

    def convert_to_numpy(self):
        return self.__data_frame.to_numpy()

    def convert_to_json(self):
        return self.__data_frame.to_json()

    def save_to_file(self, name, data, encoding='utf-8'):
        with io.open(name,'w',encoding=encoding) as file:
            file.write(data)
            file.close()

    def save_html_file(self,name):
        with open(name, "w", encoding="utf-8") as file:
            file.writelines('<meta charset="UTF-8">\n')
            file.write(self.convert_to_html())
            file.close()


