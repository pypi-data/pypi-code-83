from functools import lru_cache

import pandas

from eQmaster import eQueries


@lru_cache
def get_raw_index(index_symbol, date_label, label):
    index_df = eQueries().get(search_list=[index_symbol], columns=[
        date_label, label], attr='index')
    return index_df


def price_return(df, date_label, label):
    df = df[[date_label, label]].copy()
    df.columns = [date_label, 'Price']
    df['Return'] = df['Price'].pct_change()
    return df


def rolling_std(df, period):
    return df['Return'].rolling(period).std()


def get_index_price(df, date_label, label, period):
    df = price_return(df, date_label, label)
    df['Std'] = rolling_std(df, period)
    return df


@lru_cache
def cache_get_index_price(index_symbol, date_label, label, period):
    df = get_raw_index(index_symbol, date_label, label)
    return get_index_price(df, date_label, label, period)


def market_beta(
    stock_df=None,
    index_df=None,
    index_symbol=None,
    date_label = 'Date',
    label='Close',
    period=30
):
    if stock_df is None:
        raise Exception('stock dataframe is empty')

    if index_df is None and index_symbol is None:
        raise Exception('index dataframe is empty while index symbol is not given')

    if label not in stock_df.columns:
        raise Exception('Close column is required but is not found.')

    stock_price = price_return(stock_df, date_label, label)
    stock_price['Std'] = rolling_std(stock_price, period)

    if index_df is None:
        index_price = cache_get_index_price(index_symbol, date_label, label, period)
    else:
        index_price = get_index_price(index_df, date_label, label, period)

    agg = stock_price.merge(
        index_price, on=[date_label], suffixes=[' Stock', ' Index'])

    corr = agg['Return Stock'].rolling(period).corr(agg['Return Index'])
    beta = corr*agg['Std Stock']/agg['Std Index']
    beta.rename('Beta', inplace=True)
    return pandas.concat([agg[date_label], beta], axis=1)


if __name__ == '__main__':
    from eQmaster import eQueries
    eq = eQueries()
    stock_df = eq.get(
        search_list=['2498.tw'],
        columns=['Date', 'Close'], 
        attr='stock'
    )
    b = market_beta(
        stock_df=stock_df,
        index_symbol='IX0001'
    )
    print(b)
