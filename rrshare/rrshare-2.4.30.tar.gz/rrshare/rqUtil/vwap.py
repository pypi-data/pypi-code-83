def vwap(secs):
    secslist = []
    secslist.append(secs)
    secs = secslist if isinstance(secs, str)  else secs
    lasttradeDate = lastHKCN_tradedate()
    df = get_price(secs,end_date=lasttradeDate,count=3)
    df['vwap'] = (df.money/df.volume).apply(lambda x: round(x,2))
    vwap = df['vwap'].T
    vwap['vwap'] = vwap.iloc[:,-1:]
    vwap = vwap[['vwap']]
    vwap = vwap.sort_index()
    return vwap
