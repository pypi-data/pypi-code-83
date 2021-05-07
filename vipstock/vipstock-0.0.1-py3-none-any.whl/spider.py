#coding=utf-8

import os
import pandas as pd
import yaml
import crawl


rootPath='./Data/'


class VipSpider():
    def __init__(self):
        self.sp=crawl.VipStock()
        self.df_hold=None
        self.df_pred=None

    def df_merge(self, dirpath):
        df_out = None
        print('Waiting...')
        for parent, dirnames, filenames in os.walk(dirpath):
            for file in filenames:
                # imgName = os.path.splitext(file)[0]
                # imgExt = os.path.splitext(file)[1]
                imgPath = os.path.join(parent, file).replace('\\', '/')
                print(imgPath)
                # df_in = pd.read_csv(imgPath)
                df_in = pd.read_excel(imgPath, skiprows=None, dtype=object)
                # df_in = df_in[0:-2]
                print(df_in)
                if df_out is None:
                    df_out = df_in
                else:
                    df_out = pd.concat([df_out, df_in], axis=0, ignore_index=True)
        # print('去重')
        # df_out.drop_duplicates(subset=['mid'], keep ='first', inplace = True)
        df_out.to_excel('汇总.xlsx', index=False)


    def q_export(self, filename, org=None):
        if org not in ['社保','基金','QFII']:
            return
        df_out = pd.DataFrame(
            columns=['年度', '季度', '代码', '简称', '截至日期', '家数', 'T本期持股数(万股)', 'T持股占已流通A股比例(%)', 'T同上期增减(万股)', 'T持股比例(%)',
                     '上期家数',
                     '{}代码'.format(org), '{}名称'.format(org), '本期持股数(万股)', '持股占已流通A股比例(%)', '同上期增减(万股)', '持股比例(%)', '持股比例增幅(%)'])
        qs=filename.split('.')[0].split('_')

        path=rootPath+'2/'+filename
        df=pd.read_excel(path, dtype=object)
        print(path)
        del df['Unnamed: 0']

        for index, row in df.iterrows():
            try:
                detail_list = yaml.safe_load(row['明细'])
                for detail in detail_list:
                    row1 = [qs[-2], qs[-1], row['代码'], row['简称'], row['截至日期'], row['家数'], row['本期持股数(万股)'],
                            row['持股占已流通A股比例(%)'], row['同上期增减(万股)'], row['持股比例(%)'], row['上期家数'],
                            detail['orgCode'], detail['orgFullName'], detail['stockAmount'], detail['stockPercent'],
                            detail['stockAmountBalance'], detail['stockPercentLast'], detail['stockPercentBalance']]
                    # print(row1)
                    df_out.loc[len(df_out)] = row1
            except Exception as e:
                print(e)

        # print(df_out)
        df_out.to_excel(rootPath+'3/'+filename, index=False)

    def sbzc_export(self):
        # 社保重仓股格式处理
        for filename in os.listdir(rootPath+'2/sbzc/'):
            df_out = pd.DataFrame(
                columns=['年度', '季度', '代码', '简称', '截至日期', '家数', 'T本期持股数(万股)', 'T持股占已流通A股比例(%)', 'T同上期增减(万股)', 'T持股比例(%)',
                         '上期家数',
                         '社保代码', '社保名称', '本期持股数(万股)', '持股占已流通A股比例(%)', '同上期增减(万股)', '持股比例(%)', '持股比例增幅(%)'])
            qs=filename.split('.')[0].split('_')

            path=rootPath+'2/sbzc/'+filename
            df=pd.read_excel(path, dtype=object)
            print(path)
            del df['Unnamed: 0']

            for index, row in df.iterrows():
                try:
                    detail_list = yaml.safe_load(row['明细'])
                    for detail in detail_list:
                        row1 = [qs[-2], qs[-1], row['代码'], row['简称'], row['截至日期'], row['家数'], row['本期持股数(万股)'],
                                row['持股占已流通A股比例(%)'], row['同上期增减(万股)'], row['持股比例(%)'], row['上期家数'],
                                detail['orgCode'], detail['orgFullName'], detail['stockAmount'], detail['stockPercent'],
                                detail['stockAmountBalance'], detail['stockPercentLast'], detail['stockPercentBalance']]
                        # print(row1)
                        df_out.loc[len(df_out)] = row1
                except Exception as e:
                    print(e)

            # print(df_out)
            df_out.to_excel(rootPath+'3/sbzc/'+filename, index=False)

    def jjzc_export(self):
        # 基金重仓股格式处理
        for filename in os.listdir(rootPath+'2/jjzc/'):
            df_out = pd.DataFrame(
                columns=['年度', '季度', '代码', '简称', '截至日期', '家数', 'T本期持股数(万股)', 'T持股占已流通A股比例(%)', 'T同上期增减(万股)', 'T持股比例(%)',
                         '上期家数',
                         '基金代码', '基金名称', '本期持股数(万股)', '持股占已流通A股比例(%)', '同上期增减(万股)', '持股比例(%)', '持股比例增幅(%)'])
            qs=filename.split('.')[0].split('_')

            path=rootPath+'2/jjzc/'+filename
            df=pd.read_excel(path, dtype=object)
            print(path)
            del df['Unnamed: 0']

            for index, row in df.iterrows():
                try:
                    detail_list = yaml.safe_load(row['明细'])
                    for detail in detail_list:
                        row1 = [qs[-2], qs[-1], row['代码'], row['简称'], row['截至日期'], row['家数'], row['本期持股数(万股)'],
                                row['持股占已流通A股比例(%)'], row['同上期增减(万股)'], row['持股比例(%)'], row['上期家数'],
                                detail['orgCode'], detail['orgFullName'], detail['stockAmount'], detail['stockPercent'],
                                detail['stockAmountBalance'], detail['stockPercentLast'], detail['stockPercentBalance']]
                        # print(row1)
                        df_out.loc[len(df_out)] = row1
                except Exception as e:
                    print(e)

            # print(df_out)
            df_out.to_excel(rootPath+'3/jjzc/'+filename, index=False)

    def qfii_export(self):
        # QFII重仓股格式处理
        for filename in os.listdir(rootPath+'2/qfii/'):
            df_out = pd.DataFrame(
                columns=['年度', '季度', '代码', '简称', '截至日期', '家数', 'T本期持股数(万股)', 'T持股占已流通A股比例(%)', 'T同上期增减(万股)', 'T持股比例(%)',
                         '上期家数',
                         'QFII代码', 'QFII名称', '本期持股数(万股)', '持股占已流通A股比例(%)', '同上期增减(万股)', '持股比例(%)', '持股比例增幅(%)'])
            qs = filename.split('.')[0].split('_')

            path = rootPath+'2/qfii/' + filename
            df = pd.read_excel(path, dtype=object)
            print(path)
            del df['Unnamed: 0']

            for index, row in df.iterrows():
                try:
                    detail_list = yaml.safe_load(row['明细'])
                    for detail in detail_list:
                        row1 = [qs[-2], qs[-1], row['代码'], row['简称'], row['截至日期'], row['家数'], row['本期持股数(万股)'],
                                row['持股占已流通A股比例(%)'], row['同上期增减(万股)'], row['持股比例(%)'], row['上期家数'],
                                detail['orgCode'], detail['orgFullName'], detail['stockAmount'], detail['stockPercent'],
                                detail['stockAmountBalance'], detail['stockPercentLast'], detail['stockPercentBalance']]
                        # print(row1)
                        df_out.loc[len(df_out)] = row1
                    if detail_list ==[]:
                        print('bingo')
                except Exception as e:
                    print(e)

            # print(df_out)
            df_out.to_excel(rootPath+'3/qfii/' + filename, index=False)

    def jgcg_export(self):
        # 机构持股汇总格式处理
        for filename in os.listdir(rootPath+'2/jgcg/'):
            df_out = pd.DataFrame(
                columns=['年度', '季度', '证券代码', '证券简称', '机构数', '机构数变化', 'T持股比例(%)', 'T持股比例增幅(%)', 'T占流通股比例(%)', 'T占流通股比例增幅(%)',
                         '机构种类', '机构代码', '机构名称', '持股数', '持股比例(%)', '持股比例增幅(%)', '占流通股比例(%)', '占流通股比例增幅(%)'])
            qs=filename.split('.')[0].split('_')

            path=rootPath+'2/jgcg/'+filename
            print(path)
            df=pd.read_excel(path, dtype=object)
            del df['Unnamed: 0']

            for index, row in df.iterrows():
                try:
                    detail = yaml.safe_load(row['明细'])
                    # print(detail)
                    flag=False
                    # 上市公司
                    stock=detail['stock']
                    if stock['total'] != []:
                        del stock['total']
                        flag=flag or True
                        for item in stock.values():
                            # print(item)
                            row1 = [qs[-2], qs[-1], row['证券代码'], row['证券简称'], row['机构数'], row['机构数变化'], row['持股比例(%)'],
                                    row['持股比例增幅(%)'], row['占流通股比例(%)'], row['占流通股比例增幅(%)'], '上市公司',
                                    item['orgCode'], item['orgFullName'], item['stockAmount'], item['stockPercent'],
                                    item['stockPercentBalance'], item['currentPercent'], item['currentPercentBalance']]
                            df_out.loc[len(df_out)] = row1
                    # 基金
                    fund=detail['fund']
                    if fund['total'] != []:
                        del fund['total']
                        flag = flag or True
                        for item in fund.values():
                            # print(item)
                            row2 = [qs[-2], qs[-1], row['证券代码'], row['证券简称'], row['机构数'], row['机构数变化'], row['持股比例(%)'],
                                    row['持股比例增幅(%)'], row['占流通股比例(%)'], row['占流通股比例增幅(%)'], '基金',
                                    item['orgCode'], item['orgFullName'], item['stockAmount'], item['stockPercent'],
                                    item['stockPercentBalance'], item['currentPercent'], item['currentPercentBalance']]
                            df_out.loc[len(df_out)] = row2
                    # 社保
                    socialSecurity = detail['socialSecurity']
                    if socialSecurity['total'] != []:
                        del socialSecurity['total']
                        flag = flag or True
                        for item in socialSecurity.values():
                            # print(item)
                            row3 = [qs[-2], qs[-1], row['证券代码'], row['证券简称'], row['机构数'], row['机构数变化'], row['持股比例(%)'],
                                    row['持股比例增幅(%)'], row['占流通股比例(%)'], row['占流通股比例增幅(%)'], '社保',
                                    item['orgCode'], item['orgFullName'], item['stockAmount'], item['stockPercent'],
                                    item['stockPercentBalance'], item['currentPercent'], item['currentPercentBalance']]
                            df_out.loc[len(df_out)] = row3
                    # 保险
                    insurance = detail['insurance']
                    if insurance['total'] != []:
                        del insurance['total']
                        flag = flag or True
                        for item in insurance.values():
                            # print(item)
                            row4 = [qs[-2], qs[-1], row['证券代码'], row['证券简称'], row['机构数'], row['机构数变化'], row['持股比例(%)'],
                                    row['持股比例增幅(%)'], row['占流通股比例(%)'], row['占流通股比例增幅(%)'], '保险',
                                    item['orgCode'], item['orgFullName'], item['stockAmount'], item['stockPercent'],
                                    item['stockPercentBalance'], item['currentPercent'], item['currentPercentBalance']]
                            df_out.loc[len(df_out)] = row4
                    # QFII
                    qfii = detail['qfii']
                    if qfii['total'] != []:
                        del qfii['total']
                        flag = flag or True
                        for item in qfii.values():
                            # print(item)
                            row5 = [qs[-2], qs[-1], row['证券代码'], row['证券简称'], row['机构数'], row['机构数变化'], row['持股比例(%)'],
                                    row['持股比例增幅(%)'], row['占流通股比例(%)'], row['占流通股比例增幅(%)'], 'QFII',
                                    item['orgCode'], item['orgFullName'], item['stockAmount'], item['stockPercent'],
                                    item['stockPercentBalance'], item['currentPercent'], item['currentPercentBalance']]
                            df_out.loc[len(df_out)] = row5
                    # 明细为空
                    if not flag:
                        row6 = [qs[-2], qs[-1], row['证券代码'], row['证券简称'], row['机构数'], row['机构数变化'], row['持股比例(%)'],
                                row['持股比例增幅(%)'], row['占流通股比例(%)'], row['占流通股比例增幅(%)'],'','','','','','','','']
                        df_out.loc[len(df_out)] = row6

                except Exception as e:
                    print(e)

            # print(df_out)
            df_out.to_excel(rootPath+'3/'+filename, index=False)

    def Imatate(self):
        # 同步配置参数

        self.sp.update_info()
        for kind in ['jgcg', 'jjzc', 'sbzc', 'qfii']:
            for year in range(2007,2021):
                for q in range(1,5):
                    title='{}_{}_{}'.format(kind, year, q)
                    print(title)
                    self.sp.df_hold=None
                    self.sp.param['home']['p']=1
                    self.sp.ComStockHold(year, q, kind)

                    self.sp.df_hold.to_excel(rootPath + '2/df_{}.xlsx'.format(title))

    def q_export(self, filename, org=None):
        if org not in ['社保','基金','QFII']:
            return
        df_out = pd.DataFrame(
            columns=['年度', '季度', '代码', '简称', '截至日期', '家数', 'T本期持股数(万股)', 'T持股占已流通A股比例(%)', 'T同上期增减(万股)', 'T持股比例(%)',
                     '上期家数',
                     '{}代码'.format(org), '{}名称'.format(org), '本期持股数(万股)', '持股占已流通A股比例(%)', '同上期增减(万股)', '持股比例(%)', '持股比例增幅(%)'])
        qs=filename.split('.')[0].split('_')

        path=rootPath+'2/'+filename
        df=pd.read_excel(path, dtype=object)
        print(path)
        del df['Unnamed: 0']

        for index, row in df.iterrows():
            try:
                detail_list = yaml.safe_load(row['明细'])
                for detail in detail_list:
                    row1 = [qs[-2], qs[-1], row['代码'], row['简称'], row['截至日期'], row['家数'], row['本期持股数(万股)'],
                            row['持股占已流通A股比例(%)'], row['同上期增减(万股)'], row['持股比例(%)'], row['上期家数'],
                            detail['orgCode'], detail['orgFullName'], detail['stockAmount'], detail['stockPercent'],
                            detail['stockAmountBalance'], detail['stockPercentLast'], detail['stockPercentBalance']]
                    # print(row1)
                    df_out.loc[len(df_out)] = row1
            except Exception as e:
                print(e)

        # print(df_out)
        df_out.to_excel(rootPath+'3/'+filename, index=False)

    def q_download(self, org, year, q):
        # 同步配置参数
        self.sp.update_info()
        title = '{}_{}_{}'.format(org, year, q)
        print(title)
        self.sp.param['home']['p'] = 1
        self.sp.ComStockHold(year, q, org)

        self.sp.df_hold.to_excel(rootPath + '2/df_{}.xlsx'.format(title))

    def Htmltable2Excel(self, tableHtml=None, savePath=None):
        soup = BeautifulSoup(tableHtml, 'html.parser')
        tables = soup.find_all('table')  # 查看当前html页面所有table 元素<可能含有多个>
        file_name = "export{}.xlsx".format(time.time()) if savePath is None else savePath  # 导出文件名
        # ExcelWriter is the class for writing DataFrame objects into excel sheets.
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')  # Excel 写操作对象
        workbook = writer.book  # 创建工作簿
        for idx, table in enumerate(tables):
            table_title = 'Table-' + str(idx)
            # Read HTML tables into a list of DataFrame objects.
            df_table = pd.read_html(str(table), header=0, flavor='bs4')[0]
            print(df_table)
            df_table.dropna(how='all', inplace=True)  # 当一整行都是nan时，去掉该行
            # print(df_table)
            df_table.to_excel(writer, index=False, sheet_name=table_title)  # 将df对象转换成Excel表格

            worksheet = writer.sheets[table_title] # 添加该子表
            # 对工作簿添加样式
            header_fmt = workbook.add_format({'font_size': 14, 'bold': True, 'border': 1})
            # header_fmt = workbook.add_format({'font_size': 14, 'bold': True, 'fg_color': '#D7E4BC', 'border': 1})
            # 对子表的第一行的字段设置样式
            for col_num, value in enumerate(df_table.columns.values):
                worksheet.write(0, col_num, value, header_fmt)
            # 设置工作簿列宽
            worksheet.set_column('A:Z', 25)
        # # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        print('Export End!')

# 主程序入口
if __name__ == '__main__':

    spider = VipSpider()
    # spider.Imatate()

    spider.q_download('sbzc', 2007, 2)
    # spider.q_export('df_sbzc_2007_2.xlsx', org='社保')



    # spider.df_merge(rootPath+'3\sbzc')


