# coding=utf-8

import subprocess
import pandas as pd

from rrshare.rqUtil.rqSetting import DATABASE
from rrshare.rqUtil.rqLogs import rq_util_log_info


def rq_util_mongo_initial(db=DATABASE):

    db.drop_collection('stock_day')
    db.drop_collection('stock_list')
    db.drop_collection('stock_info')
    db.drop_collection('trade_date')
    db.drop_collection('stock_min')
    db.drop_collection('stock_transaction')
    db.drop_collection('stock_xdxr')


def rq_util_mongo_status(db=DATABASE):
    rq_util_log_info(db.collection_names())
    rq_util_log_info(db.last_status())
    rq_util_log_info(subprocess.call('mongostat', shell=True))


def rq_util_mongo_infos(db=DATABASE):

    data_struct = []

    for item in db.collection_names():
        value = []
        value.append(item)
        value.append(eval('db.' + str(item) + '.find({}).count()'))
        value.append(list(eval('db.' + str(item) + '.find_one()').keys()))
        data_struct.append(value)
    return pd.DataFrame(data_struct, columns=['collection_name', 'counts', 'columns']).set_index('collection_name')


if __name__ == '__main__':
    #print(rq_util_mongo_infos())
    rq_util_mongo_status()
