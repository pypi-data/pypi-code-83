# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

from rrshare.rqFetch import jq, pro
from rrshare.rqUtil import rq_util_get_last_tradedate 

today = datetime.now().date()
lastTD = rq_util_get_last_tradedate()
dateBeforePeriod =  lambda x: today - timedelta(days=x)


Q_dict = {
        'q1':'0331',
        'q2':'630',
        'q3':'930',
        'q4':'1231'
        }
#print(Q_dict)


def Y_list(Y=5):
    q = jq.query(jq.indicator.code,
             jq.indicator.statDate,
             )
    df = jq.get_fundamentals(q)
    df = df.set_index(['code'])
    Y0 = int(df.statDate.values[-1][:4])
    y_list=range(Y0-Y,Y0+1)
    return list(y_list)


def Q_list(enddate=lastTD, Q=4):
    df = jq.get_fundamentals(jq.query(jq.indicator.code,
                jq.indicator.statDate,
                 ), date=enddate)
    qdate = np.sort(list(set(df.statDate.values)))
    #print(qdate)
    fun  = lambda x: "".join([str(pd.to_datetime(x).year),"q", str(int(pd.to_datetime(x).month / 3))])
    q_list = list(map(fun, qdate[-Q:]))
    return q_list


def forecast_Q_list(enddate=lastTD): # forecast Q
    Q_forecast = Q_list()[-1]
    this_q = list([int(Q_forecast[:4]), int(Q_forecast[-1])])
    next_q_y = lambda x:  int(x[:4]) if int(str(x)[-1]) != 4 else int(x[:4]) + 1
    next_q_q = lambda x:  int(x[-1]) + 1 if int(str(x)[-1]) != 4 else  1
    next_q = list([next_q_y(Q_forecast), next_q_q(Q_forecast)])
    return list([this_q, next_q])


def forecast_Tspro_Q_list(enddate=lastTD): # forecast Q
    Q_forecast = Q_list()[-1]
    this_q = Q_dict.get(Q_forecast[-2:])
    this_q_ts = ''.join([Q_forecast[:4],this_q])
    next_q_y = lambda x:  int(x[:4]) if int(str(x)[-1]) != 4 else int(x[:4]) + 1
    next_q_q = lambda x:  int(x[-1]) + 1 if int(str(x)[-1]) != 4 else  1
    next_q = ''.join([str(next_q_y(Q_forecast)), Q_dict.get(''.join(['q', str(next_q_q(Q_forecast))]))]) 
    return this_q_ts, next_q


def forecast_jq_Q_list(pubDate=dateBeforePeriod(365), Q=2): # forecast Q --> ['2020-03-31','2020-06-30']
    df = jq.finance.run_query(jq.query(jq.finance.STK_FIN_FORCAST.end_date).filter(
            jq.finance.STK_FIN_FORCAST.pub_date > pubDate)
        )
    qdate = np.sort(list(set(df.end_date.values)))
    Q_list = qdate[-Q:] 
    return Q_list


if __name__ == '__main__':
    print(Y_list())
    print(Q_list())
    print(forecast_Q_list())
    print(forecast_jq_Q_list())
    print(forecast_Tspro_Q_list())


