import pandas as pd
import tushare as ts

from rrshare.rqUtil import (
        rq_util_date_today,
        rq_util_date_int2str,
        rq_util_date_str2int,
        rq_util_get_last_day,
        rq_util_get_trade_gap,
        rq_util_get_trade_range,
        rq_util_get_real_datelist,
        rq_util_get_last_tradedate
        )

from rrshare.rqFetch import  jq , pro
from rrshare.rqUtil import setting
from rrshare.rqUtil import (rq_util_code_tosrccode,rq_util_code_tostr)
from rrshare.rqFetch.rqCodeName import (swl_index_to_name, stock_code_to_name)


def fetch_swl_index_jq(name=""):
    if name:
        return jq.get_industries(name=name).reset_index()
    else:
        swl_name_all = pd.DataFrame()
        for i in ['sw_l1','sw_l2','sw_l3']:
            swl_name = jq.get_industries(name=i).reset_index()
            swl_name['level_jq'] = i.split("_", )[-1].upper()
            swl_name_all = swl_name_all.append(swl_name)
        return swl_name_all


def all_stock_list_code(trade_date=rq_util_get_last_tradedate()):
    trade_date = str(trade_date).replace('-','')
    df = pro.adj_factor(trade_date=trade_date)
    return list(df['ts_code'].apply(lambda x: x[0:6]).values)

    
def fetch_swl_index_tspro():
    df_tspro = pro.index_classify()
    df_tspro['index'] = df_tspro['index_code'].map(lambda x: x[:6])
    #print(df_tspro)
    return df_tspro 


def swl_index_name(level="",df=True):
    df_jq = fetch_swl_index_jq()
    df_tspro = fetch_swl_index_tspro()
    df_l = df_jq.merge(df_tspro, how='inner', on='index')
    df_l = df_l[['index','name','level']].set_index('index')
    if level:
        df_l = df_l[df_l['level']==level]
    if df:
        return df_l
    return dict(zip(df_l['index'].values,df_l['name'].values))


def stock_belong_swl(symbol,industry_type='sw_l1',industry_code_name='industry_name'):
    '''industry_type : sw_l1, sw_l2, sw_l3, zjw(default)
       industry_code_name : industry_name, industry_code 
    '''
    jq_code = rq_util_code_tosrccode(symbol,src='joinquant')
    #print(jq_code)
    d = jq.get_industry(jq_code)
    #print(d)
    if str(industry_type) in d[str(jq_code)].keys():
        indus = d[str(jq_code)][str(industry_type)][str(industry_code_name)]
    else:
        indus = None
    return indus 


def stock_belong_swl_all_level(types=['sw_l1','sw_l2','sw_l3']): # sw_l1, sw_l2, sw_l3, zjw
    swl_all: pd.DataFrame=None
    #print(len(all_stock_list_code()))
    allAStocks = list(map(lambda x: rq_util_code_tosrccode(x,src='joinquant'),\
                            all_stock_list_code()))
    d = jq.get_industry(allAStocks, rq_util_get_last_tradedate())
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

def fetch_swl_stocks(industry_code, date=None):
        data = jq.get_industry_stocks(industry_code)
        data = list(map(rq_util_code_tostr, data))
        data = list(map(lambda x: stock_code_to_name(x), data))
        return data


def fetch_swl_daily_tspro(start_date="",end_date=rq_util_get_last_tradedate()):

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


def fetch_swl_daily_tspro_adv(start_date="",end_date=rq_util_get_last_tradedate()):
    df_jq = fetch_swl_index_jq()
    df_tspro = fetch_swl_index_tspro()
    df_swl = df_jq.merge(df_tspro, how='inner', on='index')
    df_swl_day = fetch_swl_daily_tspro(start_date=start_date,end_date=end_date)
    df_swl_day['index'] = df_swl_day['ts_code'].map(lambda x: x.split(".")[0])
    df_swl_day_L = df_swl.merge(df_swl_day, how='inner', on='index')
    df_swl_day_tspro = df_swl.merge(df_swl_day, how='outer', on='index')
    df_swl_day_tspro.drop(columns=['index_code','level_jq','industry_name'], inplace=True)
    df_swl_day_tspro.rename(columns={'name_x':'name','name_y':'industry_name'}, inplace=True)
    df_swl_day_tspro['trade_date'] = pd.to_datetime(df_swl_day_tspro['trade_date'], format='%Y-%m-%d')
    df_swl_day_tspro  = df_swl_day_tspro[['trade_date', 'index','name','level','ts_code','industry_name',\
           'open','low','high','close','change','pct_change','vol','amount','pe','pb']] 
    # df_swl_day_tspro.sort_values(by=['trade_date','index'], ascending=False)
    #df_swl_day_tspro.to_csv("/tmp/wsl_day_tspro.csv", encoding='utf_8_sig')
    #print(df_swl_day_tspro)
    return df_swl_day_tspro
    


if __name__ == '__main__':
    #print(all_stock_list_code())
    print(fetch_swl_index_jq(''))
    #print(swl_index_name(level="L1"))
    #print(code_to_jq_code(['600519']))
    #print(stock_belong_swl('600519','sw_l1'))
    print(stock_belong_swl_all_level())
    #print(fetch_swl_daily_tspro(start_date='2021-01-28'))
    #print(fetch_swl_daily_tspro_adv(start_date="2021-01-25"))
    #print(fetch_swl_stocks('850541','name'))
    pass

    

