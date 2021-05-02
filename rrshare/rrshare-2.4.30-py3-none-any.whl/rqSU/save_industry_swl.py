#coding: utf-8

import pandas as pd
import tushare as ts
import jqdatasdk as jq

from rrshare.rqFetch import pro, jq
from rrshare.rqUtil import (
        rq_util_date_today,
        rq_util_date_int2str,
        rq_util_date_str2int,
        rq_util_get_last_day,
        rq_util_get_last_tradedate,
        rq_util_get_trade_gap,
        rq_util_get_trade_range,
        rq_util_get_real_datelist
        )


lastTD = rq_util_get_last_tradedate() 
#lastTD = jq.get_trade_days(count=2)[-1]
print(lastTD)
#print(type(lastTD))

def fetch_swl_index_jq(industry_type="", Date=lastTD):
    if industry_type:
        return jq.get_industries(name=industry_type, date=Date).reset_index()
    else:
        swl_name_all = pd.DataFrame()
        for i in ['sw_l1','sw_l2','sw_l3']:
            swl_name = jq.get_industries(name=i, date=Date).reset_index()
            swl_name['level_jq'] = i.split("_", )[-1].upper()
            swl_name_all = swl_name_all.append(swl_name)
        return swl_name_all

def fetch_swl_index_tspro():
    df_tspro = pro.index_classify()
    df_tspro['index'] = df_tspro['index_code'].map(lambda x: x[:6])
    #print(df_tspro)
    return df_tspro 

"""
def fetch_stock_belong_swl_all_jq(types=['sw_l1','sw_l2','sw_l3']):
    from rrshare.rqUtil.jq_basic import (jq, allAStocks, lastTD) 
    #print(allAStocks)
    swl_all: pd.DataFrame=None
    d = jq.get_industry(allAStocks(), lastTD)
    for l in types:
        indus = {}
        for i in d.keys():
            if str(l) in(d[i].keys()):
                indus[i] = d[i][str(l)]['industry_name']
            else:
                indus[i] = None
        df = pd.DataFrame([indus]).T
        df.columns= [f'{l}']
        swl_all = pd.concat([swl_all, df], axis=1, sort=True)
    stock_swl = swl_all.reset_index()
    stock_swl = stock_swl.rename(columns={'index':'jq_code'})
    stock_swl['code'] = stock_swl['jq_code'].map(lambda x: x[:6])
    return stock_swl
"""

def fetch_swl_daily_tspro(start_date="",end_date=lastTD):

    """ 无trade_date输入；
        如果end_date不给值，为最后交易日
        swl_daily 数据比stock_daily要晚，晚上10以后？？
    """
    swl_day_all =  pd.DataFrame()
    #print(rq_util_get_real_datelist(start_date, end_date))
    for td in rq_util_get_trade_range(start_date, end_date):
        swl_day = pro.sw_daily(trade_date=rq_util_date_str2int(td))
        try:
            swl_day = swl_day[~swl_day['ts_code'].str.contains('802600.SI')]
        except Exception as e:
            print(e)
        finally:
            swl_day_all = swl_day_all.append(swl_day)
    return swl_day_all 
    
def fetch_swl_daily_tspro_oneday(trade_date=""):
    for _ in range(5):
        try:
            if trade_date:
                df = pro.sw_daily(trade_date=rq_util_date_str2int(trade_date))
        except:
            time.sleep(1)
        else:
            swl_day = df
    try:
        swl_day = swl_day[~swl_day['ts_code'].str.contains('802600.SI')]
    except Exception as e:
        print(e)
    else:
        return swl_day 

def fetch_swl_list_adv():
        df_jq = fetch_swl_index_jq()
        df_tspro = fetch_swl_index_tspro()
        df_swl = df_jq.merge(df_tspro, how='inner', on='index')
        df_swl = df_swl.drop(['level_jq'], axis=1)
        return df_swl

def fetch_swl_daily_tspro_adv(start_date="",end_date=lastTD):
    df_jq = fetch_swl_index_jq()
    df_tspro = fetch_swl_index_tspro()
    df_swl = df_jq.merge(df_tspro, how='inner', on='index')
    df_swl_day = fetch_swl_daily_tspro(start_date=start_date,end_date=end_date)
    df_swl_day['index'] = df_swl_day['ts_code'].map(lambda x: x.split(".")[0])
    df_swl_day_L = df_swl.merge(df_swl_day, how='inner', on='index')
    df_swl_day_tspro = df_swl.merge(df_swl_day, how='outer', on='index')
    df_swl_day_tspro.drop(columns=['index_code','level_jq','industry_name'], inplace=True)
    df_swl_day_tspro.rename(columns={'name_x':'name','name_y':'industry_name'}, inplace=True)
    #df_swl_day_tspro['trade_date']= df_swl_day_tspro['trade_date'].map(lambda x: rq_util_date_int2str(x))
    df_swl_day_tspro['trade_date'] = pd.to_datetime(df_swl_day_tspro['trade_date'], format='%Y-%m-%d')
    df_swl_day_tspro  = df_swl_day_tspro[['trade_date', 'index','name','level','ts_code','industry_name',\
           'open','low','high','close','change','pct_change','vol','amount','pe','pb']] 
    # df_swl_day_tspro.sort_values(by=['trade_date','index'], ascending=False)
    #df_swl_day_tspro.to_csv("/tmp/wsl_day_tspro.csv", encoding='utf_8_sig')
    #print(df_swl_day_tspro)
    return df_swl_day_tspro
    
def fetch_swl_daily_tspro_adv_oneday(trade_date =""):
    df_jq = fetch_swl_index_jq()
    df_tspro = fetch_swl_index_tspro()
    df_swl = df_jq.merge(df_tspro, how='inner', on='index')
    df_swl_day = fetch_swl_daily_tspro_oneday(trade_date=trade_date)
    df_swl_day['index'] = df_swl_day['ts_code'].map(lambda x: x.split(".")[0])
    df_swl_day_L = df_swl.merge(df_swl_day, how='inner', on='index')
    df_swl_day_tspro = df_swl.merge(df_swl_day, how='outer', on='index')
    df_swl_day_tspro.drop(columns=['index_code','level_jq','industry_name'], inplace=True)
    df_swl_day_tspro.rename(columns={'name_x':'name','name_y':'industry_name'}, inplace=True)
    #df_swl_day_tspro['trade_date']= df_swl_day_tspro['trade_date'].map(lambda x: rq_util_date_int2str(x))
    df_swl_day_tspro['trade_date'] = pd.to_datetime(df_swl_day_tspro['trade_date'], format='%Y-%m-%d')
    df_swl_day_tspro  = df_swl_day_tspro[['trade_date', 'index','name','level','ts_code','industry_name',\
           'open','low','high','close','change','pct_change','vol','amount','pe','pb']] 
    df_swl_day_tspro['trade_date'] = pd.to_datetime(df_swl_day_tspro['trade_date'], format='%Y-%m-%d')
    df_swl_day_tspro = df_swl_day_tspro.dropna(subset=['amount'],axis=0)
    # df_swl_day_tspro.sort_values(by=['trade_date','index'], ascending=False)
    #df_swl_day_tspro.to_csv("/tmp/wsl_day_tspro.csv", encoding='utf_8_sig')
    #print(df_swl_day_tspro)
    return df_swl_day_tspro
       

if __name__ == '__main__':
    #print(fetch_swl_index_jq())
    print(fetch_swl_daily_tspro(start_date='2021-01-28'))
    print(fetch_swl_list_adv())
    #print(fetch_swl_daily_tspro_adv(start_date="2021-01-25"))
    print(fetch_swl_daily_tspro_adv_oneday(trade_date='2021-01-29'))
    
    pass

    

