from rrshare.rqUtil import rq_util_get_pre_trade_date

from rrshare.rqSU import (rq_save_swl_day_pg,
        rq_save_stock_belong_swl_pg,
        rq_save_swl_list_pg)

def record_swl_day(N=255):
    rq_save_swl_list_pg()
    rq_save_stock_belong_swl_pg()
    rq_save_swl_day_pg(rq_util_get_pre_trade_date(n=N))

if __name__ == '__main__':
    record_swl_day(255)