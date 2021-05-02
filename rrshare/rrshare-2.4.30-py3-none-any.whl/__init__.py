# -*- coding: utf-8 -*-

#_version__ = '1.1.1'

#init setting
from rrshare.RQSetting.rqLocalize import (cache_path, log_path, rq_path, setting_path, make_dir_path)

# rqUtil code , date, tradedate
from rrshare.rqUtil import (rq_util_if_trade, rq_util_if_tradetime, is_trade_time_secs_cn, rq_util_get_last_tradedate)

# api
from rrshare.rqFetch import pro, jq

# sql-util
from rrshare.rqUtil import PgsqlClass

#rqFactor
from rrshare.rqFactor.stock_RS_OH_MA import update_stock_PRS_day, update_stock_PRS_new

# record data
from rrshare.rqUpdate import (record_roe_cf_sr_inc, record_stock_day, record_stock_PRS, 
                    record_stock_PRS_new, record_swl_day,record_swl_rs_valuation)

# to streamlit
from rrshare.rqWeb import main_st, main_echart

from rrshare.cli import main

#record data all
from rrshare.record_all_data import main_record

__str__ = """\n
******* RRSHARE ******
"""
