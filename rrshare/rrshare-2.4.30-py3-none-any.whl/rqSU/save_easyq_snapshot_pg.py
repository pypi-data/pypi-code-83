# coding=utf-8
import time 
import datetime
import pandas as pd

from rrshare.rqFetch import fetch_realtime_price_all
from rrshare.rqUtil.pgsql import PgsqlClass
from rrshare.rqUtil.mysql import MysqlClass

t = time.localtime(time.time())
print(t)
if (int(time.strftime('%H%M%S',t))> 92900 ) and (int(time.strftime('%H%M%S',t))) < 150100:  
    while True:
        df = fetch_realtime_price_all()
        PgsqlClass().insert_to_psql(df, 'rrshare','realtime_price')
    
        MysqlClass().write_to_mysql(df, 'rrshare', 'price')

        time.sleep(2)
                                              
pass

