# coding:utf-8

import pandas as pd

def normelize_code_to_jq(df): 
    '''input code like 600519, 000001
     code is 600519.XSHG, 000001.XSHE
    '''
    df['trade_code'] = df['code'].apply(lambda x: str(x).zfill(6))
    df['code'] = df['trade_code'].apply(lambda x : ''.join([str(x), '.XSHG']) if x.startswith('6')  else ''.join([str(x),'.XSHE']))
    return df
    

def normelize_code_to_tspro(df): 
    '''input code like 600519, 000001
     code is 600519.XSHG, 000001.XSHE
    '''
    df['trade_code'] = df['code'].apply(lambda x: str(x).zfill(6))
    df['ts_code'] = df['trade_code'].apply(lambda x : ''.join([str(x), '.SH']) if x.startswith('6')  else ''.join([str(x),'.SZ']))
    return df
    
