from rrshare.rqUtil import read_data_from_pg

def stock_code_name_all(index='',df=False):
    stocks = read_data_from_pg(table_name='stock_list')[['code', 'name']]
    if df:
        if index == 'name':
            return stocks.set_index('name')
        return stocks.set_index('code')
    else:
        if index == 'name':
            return  dict(zip(stocks.name,stocks.code))
        return dict(zip(stocks.code,stocks.name))


def swl_index_name_all(index='',df=False):
    swl = read_data_from_pg('swl_list')[['code','name']]
    if df:
        if index == 'name':
            return swl.set_index('name')
        return swl.set_index('code')
    else:
        if index == 'name':
            return dict(zip(swl.name, swl.code))
    return dict(zip(swl.code, swl.name))

def stock_code_to_name(symbol):
    stocks = read_data_from_pg(table_name='stock_list')[['code', 'name']]
    if isinstance(symbol ,list):
        data = stocks[stocks['code'].isin(symbol)] 
    else:
        data = stocks[stocks['code'].isin([symbol])]
    return list(dict(zip(data.code,data.name)).values()) 

def swl_index_to_name(index):
    swls = read_data_from_pg('swl_list')[['code','name']]
    if isinstance(index, list):
        swl = swls[swls['code'].isin(index)]
    else:
        swl = swls[swls['code'].isin([index])]
    swl_d = dict(zip(swl.code,swl.name))
    return list(swl_d.values())


if __name__ == '__main__':
    #print(swl_index_name(index='',df=True))
    #print(swl_index_name('name')['钨III'])
    #print(stock_code_name()['000831'])
    print(stock_code_to_name('000831'))
    print(stock_code_to_name(['000001','300674']))
    print(swl_index_to_name('850541'))
    print(swl_index_to_name(['850543', '850542']))


