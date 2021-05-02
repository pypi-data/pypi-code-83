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
业绩预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)
'''
import pandas as pd
#import h5py
from rrshare.rqFetch import pro
from rrshare.rqUtil import rq_util_log_info, rq_util_get_last_tradedate, save_data_to_postgresql
from rrshare.rqFactor.rq_report_Y_Q  import forecast_Tspro_Q_list 

up_limit = 20.
bundle_path = '/home/rome/bundle/'

forecast_Q_list = forecast_Tspro_Q_list()
rq_util_log_info(forecast_Q_list)

def forecast(ann_date="", period=forecast_Q_list[-1]):
    """ 当前接口只能按单只股票获取其历史数据，如果需要获取某一季度全部上市公司数据，请使用forecast_vip接口（参数一致）
    输入参数
    名称    类型    必选    描述
    ts_code str N   股票代码(二选一)
    ann_date    str N   公告日期 (二选一)
    start_date  str N   公告开始日期
    end_date    str N   公告结束日期
    period  str N   报告期(每个季度最后一天的日期，比如20171231表示年报)
    type    str N   预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)
    
    输出参数
    名称    类型    描述
    ts_code str TS股票代码
    ann_date    str 公告日期
    end_date    str 报告期
    type    str 业绩预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)
    p_change_min    float   预告净利润变动幅度下限（%）
    p_change_max    float   预告净利润变动幅度上限（%）
    net_profit_min  float   预告净利润下限（万元）
    net_profit_max  float   预告净利润上限（万元）
    last_parent_net float   上年同期归属母公司净利润
    first_ann_date  str 首次公告日
    summary str 业绩预告摘要
    change_reason   str 业绩变动原因
    """
    if ann_date:
        ann_date = rq_util_get_last_tradedate().replace('-','')
        df = pro.forecast_vip(ann_date=ann_date, \
                fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
    else:
        df = pro.forecast_vip(period=period,fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
    """
    try:
        df.to_hdf(f'{bundle_path}forecast_{period}.h5', 'forecast', format='table')
        rq_util_log_info(f'\n save df to h5 on {bundle_path}')
    except Exception as e:
        print(e)
    else:
        return df
    """
    return df


def save_forecast_tspro_to_h5_pg(df=None,file_path=None, period=None):
    try:
        #f = pd.HDFStore(f'{file_path}forecast_{period}.h5')
        #f[f'forecast_{period}'] = df
        df.to_hdf(f'{file_path}forecast_{period}.h5', f'forecast', format='table')
        rq_util_log_info(f'\n save df to h5 {period} on {file_path}')
        #save_data_to_postgresql('forecast', df, 'append')
        #rq_util_log_info(f'save forecast_{period} to forecast on pg')
    except Exception as e:
        print(e)

def save_forecast_tspro_to_pg(df=None, period=None):
    try:
        save_data_to_postgresql('forecast', df, 'append')
        rq_util_log_info(f'save forecast_{period} to forecast on pg')
    except Exception as e:
        print(e)

"""

with h5py.File(os.path.join(d, 'st_stock_days.h5'), 'w') as h5:
            for order_book_id, days in st_days.items():
                        h5[order_book_id] = days

with h5py.File(os.path.join(d, 'yield_curve.h5'), 'w') as f:
            f.create_dataset('data', data=yield_curve.to_records())

with open(os.path.join(d, 'instruments.pk'), 'wb') as out:
            pickle.dump(instruments, out, protocol=2)

with h5py.File(os.path.join(d, 'dividends.h5'), 'w') as h5:
            for order_book_id in dividend.index.levels[0]:
                        h5[order_book_id] = dividend.loc[order_book_id].to_records()

  with open(json_file, 'w') as f:
          f.write(df.to_json(orient='index'))


"""

    
def forecastUp():
    df = forecast()
    df = df[((df['type'] == '预增' ) | (df['type'] == '预盈' ) |(df['type'] == '预升' )) & (df['p_change_min'] >= 0)]
    print(df)
    return df
    
def forecastHighUp():
    df = forecast()
    df = df[(df['net_profit_min'] > 5000) & (df['p_change_min'] >= up_limit)]
    print(df)
    return df

def forecastDown():
    df = forecast()
    df = df[(df['type'] == '预亏' ) | (df['type'] == '预减' ) |(df['type'] == '预降' ) |(df['p_change_min'] < 0)]
    print(df)
    return df

def update_forecast():
    for q in forecast_Q_list:
        print(q)
        df = forecast(period=q)
        save_forecast_tspro_to_pg(df,period=q)
        


if __name__ == "__main__":
    #forecast()
    #forecastHighUp()
    update_forecast()
        
    pass
