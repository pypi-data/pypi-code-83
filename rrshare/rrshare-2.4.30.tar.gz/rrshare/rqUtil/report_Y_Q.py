import datetime
import numpy as np
from rrshare.rqFetch import jq
from jqdatasdk import *
from rrshare.rqUtil.rqDate_trade import rq_util_get_last_tradedate

today = datetime.datetime.now().date()
#print("today: %s"%(today))
dateBeforePeriod = lambda x: today - datetime.timedelta(days=x)

lastTD = rq_util_get_last_tradedate()

def Y_list(Y=5):
    q = query(indicator.code,
             indicator.statDate,
             )
    df = get_fundamentals(q)
    df = df.set_index(['code'])
    Y0 = int(df.statDate.values[-1][:4])
    y_list=range(Y0-Y,Y0+1)
    return list(y_list)


def Q_list(enddate=lastTD, Q=4):
    df = get_fundamentals(query(indicator.code,
                 indicator.statDate,
                 ), date=enddate)
    qdate = np.sort(list(set(df.statDate.values)))
    #print(qdate)
    fun  = lambda x: "".join([str(pd.to_datetime(x).year),"q", str(int(pd.to_datetime(x).month / 3))])
    q_list = list(map(fun, qdate[-Q:]))
    return q_list

def forecast_Q_list(enddate=lastTD, Q=3): # forecast Q
    Q_forecast = Q_list()[-1]
    this_q = list([int(Q_forecast[:4]), int(Q_forecast[-1])])
    next_q_y = lambda x:  int(x[:4]) if int(str(x)[-1]) != 4 else int(x[:4]) + 1
    next_q_q = lambda x:  int(x[-1]) + 1 if int(str(x)[-1]) != 4 else  1
    next_q = list([next_q_y(Q_forecast), next_q_q(Q_forecast)])
    return list([this_q, next_q])


def forecast_jq_Q_list(pubDate=dateBeforePeriod(365),Q=2): # forecast Q --> ['2020-03-31','2020-06-30']
    df = finance.run_query(query(finance.STK_FIN_FORCAST.end_date).filter(
            finance.STK_FIN_FORCAST.pub_date > pubDate)
        )
    qdate = np.sort(list(set(df.end_date.values)))
    Q_list = qdate[-Q:] 
    return Q_list

if __name__ == '__name__':
    print(forecast_jq_Q_list())


