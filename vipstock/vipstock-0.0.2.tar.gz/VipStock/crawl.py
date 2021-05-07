#coding=utf-8

import re
import io
import random
from VipStock import info
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
import urllib3
import pandas as pd
import yaml
from pandas.io import html


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


rootPath='./Data/'


class VipStock():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.langs = {}
        self.stamp = datetime.now().strftime('%Y%m%d')
        self.cookie=requests.cookies.RequestsCookieJar()
        self.session = requests.session()

        self.df_hold=None
        self.df_pred=None
        self.df_search=None

    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam
        self.langs = info.loginLang
        self.cookie.set("cookie", info.loginCookie)
        self.session.cookies.update(self.cookie)

    # 发送Get请求
    def requests_get(self, url, data=None, headers=None, encoding=None ):
        try:
            url = url if data is None else url+self.url_encode(data, encoding=encoding)
            # url = url.replace('%3D', '=').replace('%25', '%')      # encoding='gb2312' 即可
            time.sleep(random.random() * 1 + 0.1)  # 0-1区间随机数
            #没有缓存就开始抓取
            print('--> ' + url)
            # response = requests.get(url, verify=False)
            # response = self.session.get(url, headers=headers, verify=False)
            response = requests.get(url, headers=headers, verify=False)
            # self.session.keep_alive = False
            # response.encoding = encoding
            value = response if response.status_code == requests.codes.ok else None
        except Exception as e:
            value = None
        finally:
            return value
    # 发送Post请求
    def requests_post(self, url, data=None, headers=None):
        try:
            url = url if data is None else url+parse.urlencode(data)
            url = url.replace('%3D', '=').replace('%25', '%')
            time.sleep(random.random() * 1 + 0.1)  # 0-1区间随机数
            #没有缓存就开始抓取
            print(self.urls['proxies']['https'] + ' --> ' + url)
            # response = requests.post(url, data=data,  headers=headers, verify=False)
            response = self.session.post(url, data=data, headers=headers, verify=False)
            # self.session.keep_alive = False
            response.encoding = 'utf-8'
            value = response if response.status_code == requests.codes.ok else None
        except Exception as e:
            value = None
        finally:
            return value

    def headers_eval(self, headers):
        """
        headers 转换为字典
        :param headers: 要转换的 headers
        :return: 转换成为字典的 headers
        """
        try:
            headers = headers.splitlines()  # 将每行独立为一个字符串
            headers = [item.strip() for item in headers if item.strip() and ":" in item]  # 去掉多余的信息 , 比如空行 , 非请求头内容
            headers = [item.split(':') for item in headers]  # 将 key value 分离
            headers = [[item.strip() for item in items] for items in headers]  # 去掉两边的空格
            headers = {items[0]: items[1] for items in headers}  # 粘合为字典
            headers = json.dumps(headers, indent=4, ensure_ascii=False)  # 将这个字典转换为 json 格式 , 主要是输出整齐一点
            print(headers)
        except Exception:
            print("headers eval get error ...")
            headers = dict()

        return headers

    def headers_get(self, get_headers):
        """
        headers 转换为字典
        :param headers: 要转换的 headers
        :return: 转换成为字典的 headers
        """
        try:
            get0=get_headers.split('?')[0]
            print(get0)
            get1 = get_headers.split('?')[1]
            headers = get1.replace('=',':')
            headers = headers.split('&')  # 将每行独立为一个字符串
            headers = [item.strip() for item in headers if item.strip() and ":" in item]  # 去掉多余的信息 , 比如空行 , 非请求头内容
            headers = [item.split(':') for item in headers]  # 将 key value 分离
            headers = [[item.strip() for item in items] for items in headers]  # 去掉两边的空格
            headers = {items[0]: items[1] for items in headers}  # 粘合为字典
            headers = json.dumps(headers, indent=4, ensure_ascii=False)  # 将这个字典转换为 json 格式 , 主要是输出整齐一点
            print(headers)
        except Exception:
            print("headers eval get error ...")
            headers = dict()

        return headers

    def check_contain_chinese(self, check_str):
        if not isinstance(check_str,str):
            return False
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def url_encode(self, query,  encoding=None):
        result=query.copy()
        for key in list(result.keys()):
            if result[key] is None:
                # result.pop(key)
                del result[key]
        result=parse.urlencode(result, encoding=encoding)
        return result

    def pd_stock_format(self, df):
        # 也可以通过修改html.py实现
        if not isinstance(df, pd.core.frame.DataFrame):
            return
        for strCode in ['股票代码', '证券代码', '代码', '股票代码↑', '证券代码↑', '代码↑', '股票代码↓', '证券代码↓', '代码↓']:
            if strCode in df.columns:
                df[strCode] = df[strCode].map(lambda x: "{:0>6}".format(x))

    def pd_read_html(self, io, index=0, keeps=None, attrs=None):
        # 可指定索引解析.a['href]
        html._KeepList=keeps
        dfs = pd.read_html(io, header=0, flavor='bs4', attrs=attrs)
        html._KeepList=None
        # print(dfs)
        return dfs if index < 0 else dfs[index]

    def pd_to_excel(self, path, df, first_col=None, last_col=None, width=None, cell_format=None):
        # 保存路径后缀必须为.xlsx
        if not isinstance(path, str) or not path.endswith('.xlsx'):
            print('Unable to save, the suffix should be .xlsx')
            return
        dfs=[df] if not isinstance(df, list) else df            # 可多表保存
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        for i in range(0, len(dfs)):
            dfx=dfs[i]
            if not isinstance(dfx, pd.core.frame.DataFrame):
                print('Unable to save, the df should be DataFrame')
                writer.close()
                return
            sheet_name='Sheet{}'.format(i+1)
            # Convert the dataframe to an XlsxWriter Excel object.
            dfx.to_excel(writer, sheet_name=sheet_name, index=False)
            # Get the xlsxwriter worksheet object.
            worksheet = writer.sheets[sheet_name]
            # Set the column width anfirst_col, last_col, widthd format.
            if isinstance(width, int):
                # 可指定或自动计算列的范围
                if isinstance(first_col, int) and isinstance(last_col, int):
                    worksheet.set_column(first_col, last_col, width, cell_format)  # 在这里更改宽度值
                else:
                    worksheet.set_column(0, len(dfx.columns)-1, width, cell_format)  # 在这里更改宽度值
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    # 投资参考
    def InvestConsult(self, kind='jyts', industry=None, area=None, concept=None, market=None, suggest=None, bdate=None, edate=None, symbol=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['inve']['p']>pn:
                return
        self.param['inve']['num']=num
        self.param['inve']['order']=order
        self.param['inve']['bdate'] = bdate
        self.param['inve']['edate'] = edate
        self.param['inve']['symbol']=symbol
        self.param['inve']['s_i']=self.langs[industry] if self.check_contain_chinese(industry) else industry
        self.param['inve']['s_a']=self.langs[area] if self.check_contain_chinese(area) else area
        self.param['inve']['s_c']=self.langs[concept] if self.check_contain_chinese(concept) else concept
        self.param['inve']['s_t']=self.langs[market] if self.check_contain_chinese(market) else market
        self.param['inve']['s_z']=self.langs[suggest] if self.check_contain_chinese(suggest) else suggest

        kind = self.urls['inve'][kind] if self.check_contain_chinese(kind) else kind
        # 交易提示，暂时无法搜索
        response=self.requests_get(self.urls['inve']['base'].format(kind), data=self.param['inve'])
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text, index= 1 if kind == "rzrq" and symbol is None else 0, keeps=['href', -1] if kind in ["lsfh"] else None)
        self.pd_stock_format(df)  # df格式化
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div',attrs={'class':'pages'})
        if pages is None:
            return
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if r'下一页' in next[-1].text:
            self.param['inve']['p']+=1
            self.InvestConsult(kind=kind, industry=industry, area=area, concept=concept, market=market, suggest=suggest, bdate=bdate, edate=edate, symbol=symbol, pn=pn, num=num, order=order)

    # 机构荐股池
    def IR_Rating(self, kind='vIR_RatingNewest', last=None, symbol=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['rate']['p'] > pn:
                return
        self.param['rate']['num'] = num
        self.param['rate']['order'] = order
        self.param['rate']['last'] = last

        kind = self.urls['rate'][kind] if self.check_contain_chinese(kind) else kind
        # 个股投资评级专用
        if kind == "vIR_StockSearch" and symbol is not None:
            self.urls['rate']['base'] = "http://stock.finance.sina.com.cn/stock/go.php/{}" + "/key/{}.phtml?".format(symbol)
        response = self.requests_get(self.urls['rate']['base'].format(kind), data=self.param['rate'])
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text)
        self.pd_stock_format(df)
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div', attrs={'class': 'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if r'下一页' in next[-1].text:
            self.param['rate']['p'] += 1
            self.IR_Rating(kind=kind, last=last, symbol=symbol, pn=pn, num=num, order=order)

    # 龙虎榜
    def LHBData(self, kind='lhb', last=None, bdate=None, edate=None, symbol=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['lhb']['p'] > pn:
                return
        self.param['lhb']['num'] = num
        self.param['lhb']['order'] = order
        self.param['lhb']['last'] = last
        self.param['lhb']['symbol'] = symbol
        self.param['lhb']['bdate'] = bdate
        self.param['lhb']['edate'] = edate

        kind = self.urls['lhb'][kind] if self.check_contain_chinese(kind) else kind
        # 每日详情专用模板
        if kind == "lhb":
            self.urls['lhb']['base'] = "http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/{}/index.phtml?"
        response = self.requests_get(self.urls['lhb']['base'].format(kind), data=self.param['lhb'])
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text, -1 if kind == "lhb" and symbol is None else 0)
        if kind == "lhb" and symbol is None:
            # 合并多个子Table
            dfs=None
            for df_i in df:
                dfs = df_i if dfs is None else pd.concat([dfs, df_i], axis=0, ignore_index=True)
            df=dfs
        self.pd_stock_format(df)
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div', attrs={'class': 'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if r'下一页' in next[-1].text:
            self.param['lhb']['p'] += 1
            self.LHBData(kind=kind, last=last, bdate=bdate, edate=edate, symbol=symbol, pn=pn, num=num, order=order)

    # 市场表现
    def HqStat(self, kind='Market_Center.getHQNodeDataNew', pn=None, num=None, asc=None, sort=None):
        if pn is not None:
            if self.param['stat']['page']>pn:
                return
        self.param['stat']['num']=num
        self.param['stat']['sort']=sort
        self.param['stat']['asc'] = asc

        kind = self.urls['stat'][kind] if self.check_contain_chinese(kind) else kind
        self.param['stat']['node']= "adr_hk" if kind.split('.')[0] =="StatisticsService" else "hs_a"

        response=self.requests_get(self.urls['stat']['base'].format(kind), data=self.param['stat'])
        matchObj = re.search(r'IO.XSRV2.CallbackList\((.*)\);', response.text, re.M | re.I)
        if matchObj:
            js_data = json.loads(matchObj.group(1))
            if js_data:
                df = pd.DataFrame(data=js_data)
                self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0,
                                                                             ignore_index=True)
                # 翻页
                self.param['stat']['page']+=1
                self.HqStat(kind=kind, pn=pn, num=num, asc=asc, sort=sort)
                print(self.df_search)

    # 财务分析
    def FinanceAnalyze(self, kind='profit', industry=None, area=None, concept=None, year=None, Q=None, pn=None,
                       num=None, order=None):
        if pn is not None:
            if self.param['fina']['p'] > pn:
                return
        self.param['fina']['num'] = num
        self.param['fina']['order'] = order
        self.param['fina']['reportdate'] = year
        self.param['fina']['quarter'] = Q
        self.param['fina']['s_i'] = self.langs[industry] if self.check_contain_chinese(industry) else industry
        self.param['fina']['s_a'] = self.langs[area] if self.check_contain_chinese(area) else area
        self.param['fina']['s_c'] = self.langs[concept] if self.check_contain_chinese(concept) else concept

        kind = self.urls['fina'][kind] if self.check_contain_chinese(kind) else kind

        response = self.requests_get(self.urls['fina']['base'].format(kind), data=self.param['fina'])
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text, keeps=['href', -1] if kind in ["mainindex", "performance"] else None)
        self.pd_stock_format(df)
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div', attrs={'class': 'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if '下一页' in next[-1].text:
            self.param['fina']['p'] += 1
            self.FinanceAnalyze(kind=kind, industry=industry, area=area, concept=concept, year=year, Q=Q, pn=pn,
                                num=num, order=order)

    # 业绩预测
    def PerformancePrediction(self, kind='eps', symbol=None, orgname=None, author=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['pred']['p'] > pn:
                return
        self.param['pred']['num'] = num
        self.param['pred']['order'] = order
        self.param['pred']['symbol'] = symbol
        self.param['pred']['orgname'] = orgname
        self.param['pred']['author'] = author

        kind = self.urls['pred'][kind] if self.check_contain_chinese(kind) else kind

        response = self.requests_get(self.urls['pred']['base'].format(kind), data=self.param['pred'], encoding='gb2312')
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text, keeps=['href', -1])
        if r'研报' in df.columns:
            df['研报'] = df['研报'].map(lambda x: "http://stock.finance.sina.com.cn{}".format(x))
        # self.pd_stock_format(df)
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div', attrs={'class': 'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if r'下一页' in next[-1].text:
            self.param['pred']['p'] += 1
            self.PerformancePrediction(kind=kind, symbol=symbol, orgname=orgname, author=author, pn=pn, num=num,
                                       order=order)

    # 机构持股
    def ComStockHold(self, kind='jgcg', symbol=None, year=None, Q=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['hold']['p'] > pn:
                return
        self.param['hold']['num'] = num
        self.param['hold']['order'] = order
        self.param['hold']['symbol'] = symbol
        self.param['hold']['reportdate'] = year
        self.param['hold']['quarter'] = Q

        kind = self.urls['hold'][kind] if self.check_contain_chinese(kind) else kind  # 中英转换

        response = self.requests_get(self.urls['hold']['base'].format(kind), data=self.param['hold'])
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text)
        self.pd_stock_format(df)
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div', attrs={'class': 'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if '下一页' in next[-1].text:
            self.param['hold']['p'] += 1
            self.ComStockHold(kind=kind, symbol=symbol, year=year, Q=Q, pn=pn, num=num, order=order)

    # 机构持股详情
    def Hold_getDetail(self, kind, symbol, quarter):
        result = None
        try:
            # kind = self.urls['hold'][kind] if self.check_contain_chinese(kind) else kind
            # self.param['detail'][kind]['symbol'] = symbol
            # self.param['detail'][kind]['quarter'] = quarter
            response = self.requests_get(self.urls['detail'][kind], data=self.param['detail'][kind],
                                         headers=self.headers['detail'])
            matchObj = re.search(r'var details=\((.*)\);', response.text, re.M | re.I)
            if matchObj:
                js_data = json.loads(matchObj.group(1))
                result = js_data['data']
                print(result)
        except Exception as e:
            print(e)
        finally:
            return result

    # 分析师排名
    def AnalystRank(self, kind='zjxg', industry=None, period=None, analyst=None, year=None, Q=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['anal']['p']>pn:
                return
        self.param['anal']['num']=num
        self.param['anal']['order']=order
        self.param['anal']['industry'] = industry
        self.param['anal']['period'] = period
        self.param['anal']['analyst']=analyst
        self.param['anal']['year'] = year
        self.param['anal']['quarter']=Q

        kind = self.urls['anal'][kind] if self.check_contain_chinese(kind) else kind
        response=self.requests_get(self.urls['anal']['base'].format(kind), data=self.param['anal'], encoding='gb2312')
        root = BeautifulSoup(response.text, "html.parser")
        trs = root.find_all('tr')
        if self.df_search is None:
            head=[x.text for x in trs[0].find_all('td')]
            self.df_search = pd.DataFrame(
                columns=head)
        for tr in trs[1:]:
            td=tr.find('td')
            row=[]
            for i in range(0, len(self.df_search.columns)):
                row.append(td.text)
                td=td.findNext('td')
            # print(row)
            if len(row)==len(self.df_search.columns):
                self.df_search.loc[len(self.df_search)]=row
        print(self.df_search)
        # 翻页
        pages = root.find('div',attrs={'class':'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if '下一页' in next[-1].text:
            self.param['anal']['p']+=1
            self.AnalystRank(kind=kind, industry=industry, period=period, analyst=analyst, year=year, Q=Q, pn=pn, num=num, order=order)

    # 投资评级选股
    def IR_CustomSearch(self, kind='vIR_CustomSearch', market=None, industry=None, area=None, concept=None, last=None, suggest=None, suggest2=None, sprice=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['cust']['p']>pn:
                return
        # 中英翻译
        suggest_dict={"全部":"", "买入":10, "增持":13, "中性":20, "减持":30, "卖出":33}
        suggest2_dict={"全部":"", "买入":5, "增持":4, "中性":3, "减持":2, "卖出":1}
        price_dict={"全部":"", "<-0.1":5, "0.1-0.2":4, "0.2-0.3":3, "0.3-0.5":2, "0.5->":1}

        self.param['cust']['num']=num
        self.param['cust']['order']=order
        self.param['cust']['sr_p'] = last
        self.param['cust']['rating'] = suggest_dict[suggest] if self.check_contain_chinese(suggest) else suggest
        self.param['cust']['srating'] = suggest2_dict[suggest2] if self.check_contain_chinese(suggest2) else suggest2
        self.param['cust']['sprice'] = price_dict[sprice] if isinstance(sprice,str) else sprice
        self.param['cust']['market']=self.langs[market] if self.check_contain_chinese(market) else market
        self.param['cust']['industry']=self.langs[industry] if self.check_contain_chinese(industry) else industry
        self.param['cust']['zone']=self.langs[area] if self.check_contain_chinese(area) else area
        self.param['cust']['concept']=self.langs[concept] if self.check_contain_chinese(concept) else concept

        kind = self.urls['cust'][kind] if self.check_contain_chinese(kind) else kind

        response=self.requests_get(self.urls['cust']['base'].format(kind), data=self.param['cust'])
        root = BeautifulSoup(response.text, "html.parser")
        # 解析html_table
        df=self.pd_read_html(response.text)
        self.pd_stock_format(df)
        self.df_search = df if self.df_search is None else pd.concat([self.df_search, df], axis=0, ignore_index=True)
        print(self.df_search)
        # 翻页
        pages = root.find('div',attrs={'class':'pages'})
        next = pages.find_all('a', attrs={'class': 'page', 'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if r'下一页' in next[-1].text:
            self.param['cust']['p']+=1
            self.IR_CustomSearch(kind=kind, market=market, industry=industry, area=area, concept=concept, last=last, suggest=suggest, suggest2=suggest2, sprice=sprice, pn=pn, num=num, order=order)

    # 财报下载
    def IR_StockDown(self, kind=None, symbol=None, pn=None, num=None, order=None):
        kind = self.urls['down'][kind] if self.check_contain_chinese(kind) else kind

        response=self.requests_get(self.urls['down']['base'].format(kind, symbol))
        csv_str=response.text.replace('\t\n','\n')
        buffer = io.StringIO(csv_str)
        df=pd.read_csv(buffer, sep='\t')
        # print(df)
        return df

    # ISSUE搜索
    def Crop_Search(self, kind=None, symbol=None, pn=None, num=None, order=None):
        kind = self.urls['issue'][kind] if self.check_contain_chinese(kind) else kind
        if kind[0].startswith('vISSUE_'):
            self.urls['issue']['base']="https://vip.stock.finance.sina.com.cn/corp/go.php/{}/stockid/{}.phtml"
        elif kind[0].startswith('vFD_'):
            self.urls['issue']['base']="https://money.finance.sina.com.cn/corp/go.php/{}/stockid/{}/ctrl/part/displaytype/4.phtml"
        elif kind[0].startswith('vCI_'):
            self.urls['issue']['base']="https://vip.stock.finance.sina.com.cn/corp/go.php/{}/stockid/{}.phtml"
        elif kind[0].startswith('vGP_'):
            self.urls['issue']['base'] = "https://vip.stock.finance.sina.com.cn/corp/go.php/{}/stockid/{}.phtml"
        elif kind[0].startswith('vCO_'):
            self.urls['issue']['base'] = "https://money.finance.sina.com.cn/corp/go.php/{}/stockid/{}.phtml"
        elif kind[0].startswith('vCB_'):
            self.urls['issue']['base'] = "https://vip.stock.finance.sina.com.cn/corp/go.php/{}/stockid/{}.phtml"

        if kind[0] in ["amount", "average"]:
            self.urls['issue']['base']="https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolderAmount/code/{1}/type/{0}.phtml"
        if kind[0] =="notice":
            self.urls['issue']['base'] = "https://finance.sina.com.cn/realstock/sz/{1}_{0}.shtml"


        response=self.requests_get(self.urls['issue']['base'].format(kind[0], symbol))
        df=self.pd_read_html(response.text, index=-1, attrs=kind[1] if isinstance(kind[1], dict) else {'id': re.compile(kind[1])})
        print(len(df))

        return df

    # 研报搜索
    def Report_List(self, kind="search", orgname=None, symbol=None, industry=None, author=None, title=None, pubdate=None, pn=None, num=None, order=None):
        if pn is not None:
            if self.param['repo']['p']>pn:
                return
        self.param['repo']['num']=num
        self.param['repo']['t1']=order              #  搜索条件
        self.param['repo']['orgname']=orgname
        self.param['repo']['symbol']=symbol
        self.param['repo']['industry']=industry
        self.param['repo']['analysts']=author
        self.param['repo']['title']=title
        self.param['repo']['pubdate']=pubdate

        kind = self.urls['repo'][kind] if self.check_contain_chinese(kind) else kind

        response=self.requests_get(self.urls['repo']['base'].format(kind), data=self.param['repo'], encoding='gb2312')
        root = BeautifulSoup(response.text, "html.parser")
        trs = root.find_all('tr')
        if self.df_search is None:
            head=[x.text for x in trs[0].find_all('th')]
            self.df_search = pd.DataFrame(columns=head)
        for tr in trs[1:]:
            tds = tr.find_all('td')
            row = [x.text.strip() for x in tds]
            # print(row)
            if len(row)==len(self.df_search.columns):
                row[0]='http:'+tds[1].a['href']
                self.df_search.loc[len(self.df_search)]=row
        print(self.df_search)
        # 翻页
        pages = root.find('div',attrs={'class':'page'})
        next = pages.find_all('a', attrs={'onclick': re.compile("set_page_num")})
        if next == []:
            return
        if r'下一页' in next[-2].text:
            self.param['repo']['p']+=1
            self.Report_List(kind=kind, orgname=orgname, symbol=symbol, industry=industry, author=author, title=title, pubdate=pubdate, pn=pn, num=num, order=order)



    def Imatate(self):
        # 同步配置参数
        self.update_info()
        for kind in ['jgcg', 'jjzc', 'sbzc', 'qfii']:
            for year in range(2007,2021):
                for q in range(1,5):
                    title='{}_{}_{}'.format(kind, year, q)
                    print(title)
                    self.df_hold=None
                    self.param['home']['p']=1
                    self.ComStockHold(year, q, kind)

                    self.df_hold.to_excel(rootPath + '2/df_{}.xlsx'.format(title))

    def Imatate2(self):
        # 同步配置参数
        self.update_info()
        # self.InvestConsult(kind='融资融券', symbol=None, pn=1)
        # self.InvestConsult(kind='千股千评', industry=None, concept="光伏概念", suggest="买入",
        #                   bdate="2020-04-30", edate="2021-04-30", symbol=None, pn=3, num=600, order="symbol|1")
        # self.IR_Rating(kind='个股投资评级', last=90, symbol="000568", pn=3, num=None, order=None)
        # self.LHBData(kind='每日详情', last=None, symbol=None, bdate="2020-04-30", edate="2021-04-30", pn=1, num=None)
        # self.HqStat(kind='连续放量个股', pn=3, num=500, sort="day_con", asc=0)
        # self.FinanceAnalyze(kind='业绩报表', industry='金融行业', area='上海市', year='2021', Q=1, pn=1, order=None)
        # self.PerformancePrediction(kind='净资产收益率预测', symbol=None, orgname=None, pn=1, num=None)
        # self.ComStockHold(kind='基金重仓股', symbol=None, year='2021', Q=1, pn=3, num=600, order='num|2')
        # self.AnalystRank(kind='券商研究力量排行', industry=None, period=None, analyst=None, year=2015, Q=1, pn=3, num=None, order=None)
        # self.IR_CustomSearch(kind='投资评级选股', market=None, industry=None, area=None, concept=None, last=30, suggest='中性', suggest2='中性', sprice=None, pn=None, num=None, order=None)

        df=self.IR_StockDown(kind='利润表', symbol='600207', num=600)

        # df=self.Crop_Search(kind='公司公告', symbol='000002', num=None)
        # print(df)
        self.pd_to_excel("out.xlsx", df, width=None)


        # self.Report_List(kind='研报搜索', orgname="兴业证券股份有限公司", symbol=None, author=None, pubdate=None, pn=3, num=600, order="1")

        # self.df_search.to_excel(rootPath + '2/df_{}.xlsx'.format('eps'))
        # self.pd_to_excel(rootPath + '2/df_{}.xlsx'.format('eps'), self.df_search, width=15)


    def Imatate3(self):
        # url='http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/qgqp/index.phtml'
        url='http://stock.finance.sina.com.cn/stock/go.php/vIR_CustomSearch/index.phtml?market=sh&industry=sw2_420200&zone=diyu_310000&sr_p=90&rating=10&srating=5&sprice=4'
        response=requests.get(url)
        root = BeautifulSoup(response.text, "html.parser")
        ops = root.find('div', class_='main').find_all('option')

        ops_dict=dict(zip([x.text for x in ops], [x['value'] for x in ops]))
        print(ops_dict)

    def Imatate4(self):
        url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhb/index.phtml'
        page=requests.get(url).text
        # print(page)
        df=self.pd_read_html(page, -1)
        # df['股票代码']=df['股票代码'].map(lambda x: "{:0>6}".format(x))
        print(df)
        self.pd_to_excel('out.xlsx', df, width=20)








# 主程序入口
if __name__ == '__main__':

    spider = VipStock()
    spider.Imatate2()

    # page=requests.get('http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/002547/ctrl/all.phtml')
    # print(page.text.split('\t\n'))
    # spider.q_download('sbzc', 2007, 2)
    # spider.q_export('df_sbzc_2007_2.xlsx', org='社保')





    # spider.df_merge(rootPath+'3\sbzc')


