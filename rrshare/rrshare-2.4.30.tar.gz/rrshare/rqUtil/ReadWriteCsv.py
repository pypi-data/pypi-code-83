#coding:utf-8
import pandas as pd 
import os, platform
from rrshare.rqFetch import jq

class ReadWriteCSV():

    def __init__(self, path_name, file_name=None, data=None):
        self.path_name = path_name
        self.file_name = file_name
        self.data = data

    def get_path_name(self):
        path = os.path.expanduser('~')
        path_name_chg = ''.join([path,self.path_name, '/']) if platform.system() == 'Linux' else ''.join([path,"\\",self.path_name, "\\"])
        print(path_name_chg)
        return path_name_chg

    def read_csv(self):
        path_name_2 = self.get_path_name()
        path_file = os.path.join(path_name_2, self.file_name)
        print(path_file)
        if  not os.path.exists(path_file):
            print('file is not exist!')
        else:
            df = pd.read_csv(path_file, encoding='gbk')
            print('from %s read file to df '%(path_file))
            print('df info: ',df.head())
            return df

    def save_to_csv(self):
        df = self.data
        path_name_2 = self.get_path_name()
        path_file = os.path.join(path_name_2, self.file_name)
        #path_file = ''.join([path_file,'.csv'])
        print(path_file)
        if os.path.exists(path_file):
            print("path_file is exist, will back.")
            if os.path.exists(path_file + '.bak'):
                os.remove(path_file + '.bak')
                os.rename(path_file, path_file + '.bak')
        try:
            df.to_csv(path_file, encoding='gbk')
        except:
            print('Please cheak , maybe file  is opening!')
        else:
            print(f'save file to {path_file} ok!')

    def read_input_csv(self):  # out secs lists
        '''
        input security code in csv file, note: input columns name==t_code
        read input df file by pd.read_csv()
        normelize input_code to jq_code use string's method and zfill(6)
        # platform.system(): Windows or Linux
        '''
        path_name_chg = self.get_path_name()
        path_file = ''.join([path_name_chg, self.file_name])  
        print(path_file)
        selectSecs = pd.read_csv(path_file, encoding='utf-8')
        #print(selectSecs)
        df = selectSecs
        df['trade_code'] = df['input_code'].apply(lambda x: str(x).zfill(6))
        df['code'] = df['trade_code'].apply(lambda x : ''.join([str(x), '.XSHG']) if x.startswith('6')  else ''.join([str(x),'.XSHE']))
        path_file_save = ''.join([path_name_chg, 'normelize_%s'%(self.file_name)])
        print(path_file_save)
        df['short_name'] = df['code'].apply(lambda x: jq.get_security_info(x).display_name)
        #df['Industry'] = df['code'].apply(lambda x: stockIndustry(x).Industry)
        print(df)
        df.to_csv(path_file_save, encoding='gbk')
        return df.code.values.tolist()

def save_to_excel(fileName, sheetName_list, df_list): #TODO
    dicts = dict(zip(sheetName_list, df_list))
    #print(dicts)
    with pd.ExcelWriter('/tmp/%s.xlsx'%(fileName)) as writer:
        for sh,df in dicts.items():
            try:
                df.to_excel(writer, sheet_name=sh)
                print(f'{sh} save to {fileName}')
            except:
                print('something is wrong, check!')



