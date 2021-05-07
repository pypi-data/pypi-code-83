from hbshare.asset_allocation.macro import TradingCRNCalculator


def update_job():
    # today = datetime.datetime.today().strftime('%Y%m%d')
    today = '20210506'
    # 更新数据
    TradingCRNCalculator(today, today).get_construct_result()


if __name__ == '__main__':
    update_job()
