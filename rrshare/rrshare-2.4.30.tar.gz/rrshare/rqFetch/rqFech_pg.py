# coding: utf-8
import pandas as pd
import numpy as np
import time
import datetime
import pymongo
import tushare as ts
from sqlalchemy import create_engine
import psycopg2  
import warnings
warnings.filterwarnings("ignore")

from rrshare.rqUtil.rqLogs import (rq_util_log_debug, rq_util_log_expection,
                                     rq_util_log_info)

from rrshare.rqUtil.rqDate_trade import rq_util_get_trade_range
from rrshare.rqUtil.rqDate import (rq_util_date_str2int,rq_util_date_int2str)

from rrshare.rqUtil import PgsqlClass, setting

from rrshare.rqSU.save_industry_swl import (fetch_swl_daily_tspro_adv_oneday,
                                            fetch_swl_list_adv)

token= setting['TSPRO_TOKEN']
pro=ts.pro_api(token)

def create_pgsql(database='rrshare'):
    try:
        PgsqlClass().create_psqlDB(db_name=database)
    except Exception as e:
        print(e)

def client_pgsql(database='rrshare'):
    try:
        return PgsqlClass().client_pg(db_name=database)
    except Exception as e:
        print(e)


def save_data_to_postgresql(name_biao,data,if_exists='replace',client=client_pgsql()):
        data.to_sql(name_biao,client,index=False,if_exists=if_exists)
    
def load_data_from_postgresql(mes='',client=client_pgsql()):
    res=pd.read_sql(mes,client)
    return res

def read_data_from_pg(table_name='', client=client_pgsql()):
    res = pd.read_sql_table(table_name, client)
    return res


      
def rq_fetch_stock_day_pg(code=['000001','000002'],start_date='19000101',end_date='20500118',data='*'):
    name_biao='stock_day'
    if isinstance(code,list):
        code="','".join(code)
        mes='select '+ data+' from '+name_biao+" where  trade_date >= date_trunc('day',timestamp '"+start_date+"') \
                and trade_date <= date_trunc('day',timestamp '"+end_date+"') and code in ('"+code+"')\
                order by trade_date ASC;"
        try:   
            t=time.time()        
            res=load_data_from_postgresql(mes=mes)
            t1=time.time()
            rq_util_log_info('load '+ name_biao+ ' success,take '+str(round(t1-t,2))+' S')              
        except Exception as e:
            print(e)
            res=None
    else:
        rq_util_log_info('code type is not list, please cheack it.')         
    return res

def rq_fetch_stock_list_pg(name_biao='stock_list'):
    mes='select * from '+name_biao+";"    
    try:   
        t=time.time()        
        res=load_data_from_postgresql(mes=mes)
        t1=time.time()
        rq_util_log_info('load '+ name_biao+ ' success,take '+str(round(t1-t,2))+' S')              
    except Exception as e:
        print(e)
        res=None
    return res