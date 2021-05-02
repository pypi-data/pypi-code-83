#coding: utf-8
'''
功能：计算swl（L1，L2,L3）行业指数的不同时段（periods =[5,20,60,120,250]）的回报率rt和PRS
依赖：swl的各行业指数的日行情，tusharepro，->swl_day, swl_valuation
数据库： postgresql12
tips: df.round(2)  ;  sql-> "".jion(list), rq_util_get_pre_trade_date ; rq_util_get_last_tradedate
logging replace print
swl_day, list from rrshare , swl_rs_valuation save to rrfactor
'''
import time
import pandas as pd

import warnings
warnings.filterwarnings("ignore")
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s- %(levelname)s-%(message)s')

from rrshare.rqUtil.rqLogs import (rq_util_log_debug, rq_util_log_expection, rq_util_log_info)
from rrshare.rqUtil import (rq_util_get_trade_range, rq_util_get_last_tradedate, rq_util_get_pre_trade_date)
from rrshare.rqFetch import swl_index_name
from rrshare.rqUtil import PgsqlClass, PERIODS , SWL_LEVEL
#from rrshare.rqSU.save_industry_swl import (fetch_swl_daily_tspro_adv_oneday, fetch_swl_list_adv)

L = SWL_LEVEL().LEVEL
periods = PERIODS().PERIODS

def client_pgsql(database=None): # rrdata, rrshare, rrfactor 
    try:
        return PgsqlClass().client_pg(db_name=database)
    except Exception as e:
        print(e)

def save_data_to_pg(df, table_name,if_exists='replace',client=client_pgsql('rrfactor')):
    df.to_sql(table_name,con=client,index=False,if_exists=if_exists)


def read_data_from_pg(table_name='', client=None):
    return pd.read_sql_table(table_name, client)


def read_sql_from_pg(start_date=None,data=None,table_name=None,client=None):
    '''can select columns and trade_date
    '''
    sql = ''.join(['SELECT ', data, ' FROM ', f'{table_name}', f" WHERE trade_date >= date_trunc('day', timestamp '"+start_date+"') order by trade_date ASC;"])
    #sql= 'select ' + data + ' from ' +table_name+" where trade_date >= date_trunc('day',timestamp '"+start_date+"') order by trade_date ASC;"
    try:
        t=time.time()
        res=pd.read_sql(sql,client)
        t1=time.time()
        logging.info(f'read  data from {table_name} ,take str({t1}-{t}) \n {res}')
        return res
    except Exception as e:
        logging.error(e)


def read_table_from_pg(table_name='',period=None, client=None):
    '''only select trade_date, can't select columns
    '''
    try: 
        start_date = rq_util_get_pre_trade_date(rq_util_get_last_tradedate(), period-1)
        logging.info(start_date)
        sql = ''.join(['SELECT * FROM ', f'{table_name}', f" WHERE trade_date >= date_trunc('day', timestamp '"+start_date+"') order by trade_date ASC;"])
        logging.info(sql)
        res = pd.read_sql(sql,client)
        logging.info(f'\n {res}')
        return res
    except Exception as e:
        logging.info(e)


def RS_industry_swl(level="", client=client_pgsql('rrshare')):
    RS = pd.DataFrame()
    for period in periods:
        start_date = rq_util_get_pre_trade_date(rq_util_get_last_tradedate(), period)
        df = read_sql_from_pg(start_date=start_date, data="trade_date, index, level, name, pct_change, pe, pb", table_name='swl_day',client=client)
        df = df[df['level']==level]
        df = df[['index','name', 'pct_change']]
        rt = df.groupby(by='index').sum()
        rt['rank'] = rt['pct_change'].rank(ascending=False)
        rt['rs'] = round(100*(1 - rt['rank']/len(rt)), 2)
        rt = rt.rename(columns={'pct_change': f'rt_{str(period)}'})
        rt = rt.rename(columns={'rs': f'rs_{str(period)}','rank':f'rank_{str(period)}'})
        df_name = swl_index_name(level=level, df=True)
        df_name['swl_name'] = df_name['name']
        df_name['index'] =df_name.index
        RS = pd.concat([RS,  df_name['name'], rt, df_name['index']],axis=1, sort=True)
    RS = RS.sort_values(by='rs_250', ascending=False)
    RS['trade_date'] = rq_util_get_last_tradedate()
    RS = RS.round(2)
    logging.info(f'\n{RS}')
    return RS


def industry_swl_valuation(period=1,table_name='swl_day',level='', client=client_pgsql('rrshare')):
    df = read_table_from_pg(period=period,table_name='swl_day', client=client)
    df = df[['trade_date', 'index', 'name','level','close','pct_change', 'pe', 'pb']]
    df = df[df['level']==level]
    df = df.set_index('index')
    df = df.sort_values(by='pct_change', ascending=False)
    logging.info(f'\n {df}')
    return df


def save_swl_rs_to_pg(level=''):
    swl_rs = RS_industry_swl(level=level)
    logging.info(f'swl_industry rs:  \n{swl_rs}')
    swl_val = industry_swl_valuation(level=level).reset_index()
    #写入数据，table_name为表名，‘replace’表示如果同名表存在就替换掉
    try:
        save_data_to_pg(swl_rs,f"swl_rs_{level}")
        print(f'写入数据库的表swl_rs_{level}, ok')
        save_data_to_pg(swl_val,f"swl_valuation_{level}")
        print(f'写入数据库的表swl_valuation_{level}, ok')
    except Exception as e:
        print(e)


def web_table_swl_pg(level='', client=client_pgsql('rrfactor')):
    RS = read_data_from_pg(table_name=f'swl_rs_{level}',client=client)
    RS = RS[['index','name','rs_5','rs_10','rs_20','rs_60','rs_120','rs_250']]
    logging.info(RS)
    valuation = read_data_from_pg(f'swl_valuation_{level}', client)
    df = pd.merge(RS, valuation , on='index')
    logging.info(f'\n {df}')
    return df


def save_swl_rs_valuation_pg(level=""):
    #df, table_name,if_exists='replace',client=client_pgsql('rrfactor')
    save_data_to_pg(web_table_swl_pg(level=level), f'swl_rs_valuation_{level}')
    logging.info(f'写入数据库的表swl_rs_valuation_{level}, ok')


def update_swl_rs_valuation(L=L):
    for l in L:
        save_swl_rs_to_pg(l)
    for l in L:
        save_swl_rs_valuation_pg(l)
    

if __name__ == '__main__':
    
    #start_date='2021-02-01'
    #data='trade_date,index,name,level,close,pct_change,pe, pb'
    #table_name='swl_day'
    #read_sql_from_pg(start_date, data, table_name)
    #read_table_from_pg(table_name='swl_day', period=1)
    #rs = RS_industry_swl(level='L3')
    #save_data_to_pg(rs, 'swl_rs')
    #web_table_swl_pg('L3')
    #save_data_to_pg(web_table_swl_pg("L3"), 'swl_rs_valuation')
    #save_swl_rs_valuation_pg('L2')
    update_swl_rs_valuation(L)
    pass
