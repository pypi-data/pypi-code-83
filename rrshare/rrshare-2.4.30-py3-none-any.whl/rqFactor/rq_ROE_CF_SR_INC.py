""" ROE >7 , up change;
    CF to netprofit > 80;
    current ratio >2, quick ratio>1, receivables turnover ratio , debt_to_assets_ratio  < 60
    (current ratio = total_crrunt_assets / total_current_liability )
    goodwill to book < 20%;
    canslim_ A , C 
    inc_revenue_year_on_year in first;
    then in next Q inc_net_profit_year_on_year upchange
    industry: comsume--food demein, IT   TODO
    join forecast and fast reports (tushare) TODO
    check  TODO
"""
import pandas as pd
from datetime import datetime, timedelta
from rrshare.rqUtil import rq_util_get_last_tradedate,rq_util_log_info
from rrshare.rqUtil import  client_pgsql 
from rrshare.rqFactor.rq_report_Y_Q  import Y_list, Q_list
from rrshare.rqFetch import jq
from jqdatasdk import *

lastTD = rq_util_get_last_tradedate()
allAStocksInfo = jq.get_all_securities(types=['stock'], date = lastTD)  # include (ipo, st, susps)
allAStocks = allAStocksInfo.index.tolist()

def stockIndustry(security_list, industry_type='sw_l3'): # sw_l1, sw_l2, sw_l3, zjw #TODO
    d = jq.get_industry(security_list,date = lastTD)
    indus = {}
    for i in d.keys():
        if str(industry_type) in(d[i].keys()):
            indus[i] = d[i][str(industry_type)]['industry_name']
        else:
            indus[i] = None
    df = pd.DataFrame([indus]).T
    df.columns= ['Industry']
    rq_util_log_info(f'\n {df}')
    return df

def roe_goodwill_netprofittoCF_inc(years=4,enddate = lastTD,securties=None):
    # roe
    roe = pd.DataFrame()
    for y in Y_list(years):
        df_y = jq.get_fundamentals(jq.query(indicator.code,indicator.roe), statDate=str(y))
        df_y = df_y.set_index('code')
        df_y = df_y.rename(columns={'roe':'roe_'+str(y)})
        roe = pd.concat([roe,df_y], axis=1, sort=True)

    name = jq.get_all_securities('stock')['display_name']
            
    roe = pd.concat([roe,name], axis=1, sort=True)
    rq_util_log_info(f'\n {roe}')

    # goodwill to book
    gw = jq.get_fundamentals(
            jq.query(balance.code,
                balance.good_will,
                  balance.total_owner_equities,
                  (balance.good_will/balance.total_owner_equities)*100
                 ))
    gw =gw.set_index(['code'])
    gw = pd.DataFrame(gw,columns = ['anon_1'])
    gw = gw.rename(columns={'anon_1':'goodwilltobook'})
    gw = gw.fillna(0)
    #sl = pd.concat([roe,gw], axis=1, sort=True)
    rq_util_log_info(f'\n {gw}')
    # security_ratio
    sr = pd.DataFrame()
    for q in Q_list(enddate,2):
        df_sr = jq.get_fundamentals(
                jq.query(balance.code,
                    balance.total_current_assets,
                    balance.total_current_liability,
                    balance.total_liability,
                    balance.total_owner_equities,
                    balance.total_sheet_owner_equities,
                (balance.total_current_assets / balance.total_current_liability),
               # (balance.total_owner_equities / balance.total_liability)*100,
                (balance.total_liability / balance.total_sheet_owner_equities)*100
                ), statDate =q
                )
        df_sr = df_sr.set_index('code')
        df_sr = df_sr[['anon_1','anon_2']]
        df_sr = df_sr.rename(columns={'anon_1':f'current_ratio_{str(q)}'})
        df_sr = df_sr.rename(columns={'anon_2':f'debt_ratio_{str(q)}'})
        sr = pd.concat([sr, df_sr], axis=1, sort=True)
    rq_util_log_info(f'\n {sr}')

    # netprofittoCF
    cf = pd.DataFrame()
    for y in Y_list(years):
        df_cf = jq.get_fundamentals(jq.query(indicator.code,cash_flow.net_operate_cash_flow,
                                       income.net_profit,
                        (cash_flow.net_operate_cash_flow/income.net_profit)*100
                                      ),
                                statDate=str(y))
        df_cf = df_cf.set_index('code')
        df_cf = pd.DataFrame(df_cf,columns=['anon_1'])
        df_cf = df_cf.rename(columns={'anon_1':'cftonetprofit_'+str(y)})
        cf = pd.concat([cf,df_cf], axis=1, sort=True)
    rq_util_log_info(f'\n {cf}')

    # inc
    inc = pd.DataFrame()
    for y in Y_list(years):
        df_inc = jq.get_fundamentals(jq.query(indicator.code, indicator.inc_revenue_year_on_year,
                                        indicator.inc_net_profit_year_on_year,
                ), statDate=str(y))
        df_inc = df_inc.set_index('code')
        df_inc = df_inc.rename(columns={'inc_revenue_year_on_year':'inc_revenue_year_on_year_'+str(y)})
        df_inc = df_inc.rename(columns={'inc_net_profit_year_on_year':'inc_net_profit_year_on_year_'+str(y)})
        inc = pd.concat([inc, df_inc], axis=1, sort=True)
    rq_util_log_info(f'\n {inc}')

    # inc_Q
    inc_Q = pd.DataFrame()
    for q in Q_list(enddate,4):
        df_q = jq.get_fundamentals(jq.query(indicator.code, indicator.inc_revenue_year_on_year,
                                        indicator.inc_net_profit_year_on_year,
                                        indicator.gross_profit_margin,
                                        indicator.pubDate,
                ), statDate=q)
        df_q = df_q.set_index(['code'])
        df_q = df_q.rename(columns={'inc_revenue_year_on_year':'inc_revenue_year_on_year_'+str(q)})
        df_q = df_q.rename(columns={'inc_net_profit_year_on_year':'inc_net_profit_year_on_year_'+str(q)})
        df_q = df_q.rename(columns={'gross_profit_margin':'gross_profit_margin_'+str(q)})
        df_q = df_q.rename(columns={'pubDate':'pubDate_last'}) #+str(q)}) 
        inc_Q = pd.concat([inc_Q, df_q], axis=1, sort=True)
    rq_util_log_info(f'\n {inc_Q}')

    #Indistry
    sec_inc = inc_Q.index.tolist()
    indus1 = stockIndustry(sec_inc, industry_type='sw_l1')
    indus2 = stockIndustry(sec_inc, industry_type='sw_l2')
    indus3 = stockIndustry(sec_inc, industry_type='sw_l3')

    # concat
    sl = pd.concat([roe, gw, sr, cf, inc, inc_Q, name, indus3], axis=1, sort=True).round(2)
    sl = sl.sort_values(by='Industry').dropna(subset=['display_name'])
    #if isinstance(sl, pd.DataFrame):
    sl = sl[sl.index.isin(allAStocks)]
    df = sl.reset_index()
    df['code'] = df['index'].apply(lambda x : x[0:6])
    #df = df.drop('index', axis=1)
    df = df.rename(columns={'index':'jq_code'})
    rq_util_log_info(f'\n {df}')
    return df


def save_Fundmental_to_pg(table_name="",data="", con=client_pgsql('rrfactor'), if_exists='replace'):
    #写入数据，table_name为表名，‘replace’表示如果同名表存在就替换掉
    try:
        data.to_sql(table_name, con, index=False, if_exists=if_exists)
        print(f'写入数据库的表{table_name} , ok')
    except Exception as e:
        print(e)

def update_roe_cf_sr_inc():
    df = roe_goodwill_netprofittoCF_inc(years=4,enddate=lastTD,securties=None)
    save_Fundmental_to_pg(table_name='ROE_CF_SR_INC', data=df,  con=client_pgsql('rrfactor'), if_exists='replace')



if __name__ == "__main__":  
    #print(stockIndustry(allAStocks))
    update_roe_cf_sr_inc()
    pass

