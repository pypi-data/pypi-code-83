'''一季报披露时间：4月1日——4月30日;
半年报披露时间：7月1日——8月31日；
三季报披露时间：10月1日——10月30日;
年报披露时间：1月1日——4月30日。
    按照《上海证券交易所股票上市规则》的要求,对于年度报告，如果上市公司预计全年可能出现亏损、扭亏为盈、净利润较前一年度增长或下降50%以上
（基数过小的除外）等三类情况，应当在当期会计年度结束后的1月31日前披露业绩预告。
    深交所（一）主板A．业绩预告预计报告期内（第一季度、半年度、第三季度和年度）出现以下情况的，应进行业绩预告：净利润为负、扭亏为盈、实现盈利
    且净利润与上年同期相比上升或者下降50％以上（基数过小的除外）、期末净资产为负、年度营业收入低于1千万元。
    解读：如果不存在上述情况，可以不披露业绩预告。如果需要披露业绩预告， 业绩预告的时间要求为：
    1.一季度业绩预告:报告期当年的4月15日前
    2.半年度业绩预告:报告期当年的7月15日前
    3.三季度业绩预告:报告期当年的10月15日前
    4.年度业绩预告:报告期次年的1月31日前
    B.业绩快报鼓励上市公司在定期报告披露前，主动披露定期报告业绩快报。解读：主板业绩快报不是强制性披露的。
    （二）中小板A．业绩预告公司应在第一季度报告、半年度报告和第三季度报告中披露对年初至下一报告期末的业绩预告。
    公司预计第一季度业绩将出现归母净利润为负值、净利润与上年同期相比上升或者下降50％以上（基数过小的除外）、扭亏为盈，
    应不晚于3月31日（在年报摘要或临时公告）进行业绩预告。
    解读：中小板业绩预告是强制性披露的，全部上市公司均要进行业绩预告，但是并没有强制要求上市公司在年报中披露一季度业绩预告，这一点很容易被忽略。
    B.业绩快报年度报告预约披露时间在 3-4 月份的公司，应在 2 月底之前披露年度业绩快报。鼓励半年度报告预约披露时间在8月份的公司在7月底前披露半年度业绩快报。
    解读：年度报告预约披露时间在 3月份之前的公司可不披露年度业绩快报，否则需要强制性披露年度业绩快报。半年报和季报业绩快报不是强制性披露的。
    （三）创业板A．业绩预告公司未在上一次定期报告中对本报告期进行业绩预告的，应当及时以临时报告的形式披露业绩预告。
    解读：创业板业绩预告是强制性披露的，全部上市公司均要进行业绩预告。业绩预告的时间要求为：
    1.一季度业绩预告:上年度年度报告预约披露时间在3月31日之前的，应当最晚在披露年度报告的同时，披露本年度第一季度业绩预告；
    年度报告预约披露时间在4月份的，应当在4月10日之前披露第一季度业绩预告
    2. 半年度业绩预告:报告期当年的7月15日前
    3.三季度业绩预告:报告期当年的10月15日前
    4.年度业绩预告:报告期次年的1月31日前
    B.业绩快报年度报告预约披露时间在3-4月份的上市公司，应当在2月底之前披露年度业绩快报。
    解读：这一点与中小板相同。年度报告预约披露时间在 3月份之前的公司可不披露年度业绩快报，否则需要强制性披露年度业绩快报。半年报和季报业绩快报不是强制性披露的。

链接：https://www.jianshu.com/p/5fadda11cc4c
http://tushare.org/reference.html#id3

jq:
预告期编码	预告期类型
304001	一季度预告
304002	中报预告
304003	三季度预告
304004	四季度预告
'''
import os, platform
import pandas as pd
import tushare as ts
from rrshare.rqUtil import jq, rq_util_get_last_tradedate, rq_util_log_info
#from jqdatasdk import finance
from rrshare.rqFactor.rq_report_Y_Q import forecast_Q_list
from rrshare.rqFetch import stock_code_to_name

lastTD = rq_util_get_last_tradedate()
fc_Q_list = forecast_Q_list(enddate=lastTD)
print(fc_Q_list)

def forecast_jq(end_date='2021-03-31'): #end_date='2019-09-30'
    q=jq.query(jq.finance.STK_FIN_FORCAST
            ).filter(jq.finance.STK_FIN_FORCAST.end_date>=end_date,
            jq.finance.STK_FIN_FORCAST.pub_date>lastTD
            ).order_by(jq.finance.STK_FIN_FORCAST.pub_date.desc())
    df=jq.finance.run_query(q)
    print(df)
    df['profit_ratio_median'] = (df['profit_ratio_min'] + df['profit_ratio_max'])/2
    df['profit_median'] = (df['profit_min'] + df['profit_max'])/2
    print(df.columns)
    
    df['code'] = df.code.apply(lambda x: x[0:6])
    df['name'] = df.code.apply(lambda x: stock_code_to_name(x)[0])
    df = df[['code', 'name','pub_date','end_date','report_type','type','profit_last','profit_median','profit_ratio_median']]
    print(df)
    return  df


def net_profit(securities):
    q = jq.query(jq.income.code, jq.income.net_profit
    ).filter(jq.income.net_profit > 100000.0
    ).filter(jq.income.code.in_(securities))
    df = jq.get_fundamentals(q)
    print(df)
    return df

class Forecast():
    '''forecast_Q_list(enddate=lastTD, Q=3)[-1][0], [1]
    '''
    
    def __init__(self, year=forecast_Q_list(enddate=lastTD)[-1][0], 
        quarter=forecast_Q_list(enddate=lastTD)[-1][1], up_limit=20):
        self.year = year
        self.quarter = quarter
        self.up_limit = up_limit

    def forecast(self):
        try:
            df = ts.forecast_data(self.year, self.quarter)
            #df = df.set_index('code')
            df = df.dropna(how = 'any')
            #print(df)
            df['chg_range'] = df['range'].str.split('~')
            df['chg_min'] = df['chg_range'].str.get(0)
            df['chg_min'] = df['chg_min'].str.replace('%','')
            df['chg_max'] = df['chg_range'].str.get(-1)
            df['chg_max'] = df['chg_max'].str.replace('%','')
            df['chg_min'] = df['chg_min'].apply(lambda x: float(x))
            df['chg_max'] = df['chg_max'].apply(lambda x: float(x))
            df['chg_median'] = (df['chg_min'] + df['chg_max']) / 2
            print(f'业绩预告：{len(df)}')
            df['trade_code'] = df['code'].apply(lambda x: str(x).zfill(6))
            df['code'] = df['trade_code'].apply(lambda x : ''.join([str(x), '.XSHG']) if x.startswith('6')  else ''.join([str(x),'.XSHE']))
            df = df.set_index('code')
            df = df.sort_values(by='report_date', ascending=False)
            #print(len(df))
            #inds = stockIndustry(df.index.tolist(),'sw_l2')
            #print(len(inds))
       
            #df_f = pd.concat([df, inds], axis=1, sort=True)
            print(df)
            return df_f
        except:
            print(df.head())
            return df

    def forecastUp(self):
        df = self.forecast()
        df = df[((df['type'] == '预增' ) | (df['type'] == '预盈' ) |(df['type'] == '预升' )) & (df['chg_min'] >= 0)]
        print(df)
        return df

    def forecastHighUp(self):
        df = self.forecast()
        df = df[(df['pre_eps'] > 0) & (df['chg_min'] >= self.up_limit)]
        print(df)
        return df

    def forecastDown(self):
        df = self.forecast()
        df = df[(df['type'] == '预亏' ) | (df['type'] == '预减' ) |(df['type'] == '预降' )]
        print(df)
        return df

if __name__ == "__main__":

    # for i, l in enumerate(fc_Q_list):
    #     y, q = l[0], l[1]
    #     sheetname = f'forcast_{y}Q{q}'
    #     print(sheetname)
    #     f = Forecast(y,q)
    #     fs = f.forecast().sort_values(by='report_date', ascending=False)

    y1, q1 = fc_Q_list[0][0], fc_Q_list[0][-1]
    #f1 = Forecast(y1,q1)
    #fs1 = f1.forecast().sort_values(by='report_date', ascending=False)  
    #rq_util_log_info(f'\n {fs1}')
    y2, q2 = fc_Q_list[1][0], fc_Q_list[1][1]
    #f2 = Forecast(y2,q2)
    #fs2 = f2.forecast().sort_values(by='report_date', ascending=False)  
    #rq_util_log_info(f'\n {fs2}')

    forecast_jq()
    pass
