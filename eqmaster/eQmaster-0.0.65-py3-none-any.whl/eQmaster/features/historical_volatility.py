import pandas, numpy

def historical_volatility(dataframe, label='Close', trading_days=252):

    try:
        if dataframe is None or dataframe.empty:
            raise Exception('dataframe is empty')
        
        if label not in dataframe.columns:
            raise Exception('Close column is required but is not found.')
        
        dataframe = dataframe.copy()
        returns = numpy.log(dataframe[label]/dataframe[label].shift(1))
        returns.fillna(0, inplace=True)
        volatility = returns.rolling(window=trading_days).std()*numpy.sqrt(trading_days)

        return volatility

    except Exception as ex:
        print(f'[ERROR]: {ex}')
        return None
