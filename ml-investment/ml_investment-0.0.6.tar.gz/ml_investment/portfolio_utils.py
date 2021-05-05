import time
import numpy as np
import pandas as pd
from tqdm import tqdm
from ml_investment.download import TinkoffDownloader

def balance_portfolio(portfolio_df, data_loader, prop_col):
    sectors = [
            {'sector': 'Basic Materials', 'sector_part': 0.06931405604649113},
            {'sector': 'Communication Services', 'sector_part': 0.12239164380419218},
            {'sector': 'Consumer Cyclical', 'sector_part': 0.08560895832599877},
            {'sector': 'Consumer Defensive', 'sector_part': 0.13342669998029802},
            {'sector': 'Energy', 'sector_part': 0.055189129343203504},
            {'sector': 'Financial Services', 'sector_part': 0.07863521155719683},
            {'sector': 'Healthcare', 'sector_part': 0.05953360680576723},
            {'sector': 'Industrials', 'sector_part': 0.043649199983053354},
            {'sector': 'Real Estate', 'sector_part': 0.054883199803837886},
            {'sector': 'Technology', 'sector_part': 0.17515194593480288},
            {'sector': 'Utilities', 'sector_part': 0.12221634841515819}
        ]  
    sectors_df = pd.DataFrame(sectors)

    portfolio_df = portfolio_df[['ticker', prop_col]]
    tmp = data_loader.load_base_data()[['ticker', 'sector']]
    portfolio_df = pd.merge(portfolio_df, tmp, on='ticker', how='left')
    portfolio_df = pd.merge(portfolio_df, sectors_df, on='sector', how='left')

    tmp = portfolio_df.groupby('sector')[prop_col].sum().reset_index().rename({prop_col:'sum'}, axis=1)
    portfolio_df = pd.merge(portfolio_df, tmp, on='sector', how='left')
    portfolio_df['part'] = portfolio_df[prop_col] / portfolio_df['sum'] * portfolio_df['sector_part'] #* 52_000
    
    return portfolio_df['part'].values


def enrich_tinkoff_portfolio(portfolio_df, tinkoff_downloader):
    tinkoff_portfolio_df = pd.DataFrame(tinkoff_downloader.get_portfolio())[['ticker', 'balance']]

    prices = []
    for ticker in tqdm(portfolio_df['ticker'].values):
        try:
            prices.append(tinkoff_downloader.get_last_price(ticker))
        except:
            prices.append(None)
        time.sleep(0.2)

    portfolio_df['price'] = prices
    portfolio_df['share_cnt'] = (portfolio_df['part'] / portfolio_df['price']).apply(lambda x: None if np.isnan(x) else round(x))
    portfolio_df = pd.merge(portfolio_df, tinkoff_portfolio_df, on='ticker', how='left')
    portfolio_df['balance'] = portfolio_df['balance'].fillna(0)
    portfolio_df['diff'] = portfolio_df['share_cnt'] - portfolio_df['balance']
    
    return portfolio_df