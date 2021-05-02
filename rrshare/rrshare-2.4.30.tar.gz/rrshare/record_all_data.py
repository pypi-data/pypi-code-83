from rrshare.rqUpdate.update_ROE_CF_SR_INC import record_roe_cf_sr_inc 

from rrshare.rqUpdate.update_stock_day import record_stock_day
from rrshare.rqUpdate.update_swl_day import record_swl_day
from rrshare.rqUpdate.update_swl_rs_valuation import record_swl_rs_valuation

from rrshare.rqUpdate.update_stock_RS_OH_MA import record_stock_PRS, record_stock_PRS_new


def main_record():
    record_roe_cf_sr_inc()

    record_stock_day()
    record_swl_day()

    record_stock_PRS()
    record_stock_PRS_new()

    record_swl_rs_valuation()


if __name__ == '__main__':
    main_record()
