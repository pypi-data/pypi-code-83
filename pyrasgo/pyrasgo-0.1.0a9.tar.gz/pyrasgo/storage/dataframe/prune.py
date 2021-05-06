import pandas as pd
from typing import List, Optional

from pyrasgo.api.error import APIError


def remove_columns_with_missing_data(df: pd.DataFrame, columns: List[str] = None, threshold: float = 0) -> pd.DataFrame:
    """
    Returns a copy of your dataframe after removing columns 
    containing NULL or NaN values exceeding a threshold count
    
    df: pandas DataFrame
    columns: (Optional) List of column names to check for null, Defaults to All
    threshold: (Optional) null percentage threshold above which a column will be dropped, Defaults to 0%
    """
    df_out = df.copy(deep=True)
    column_with_nan = df_out.columns[df_out.isnull().any()]
    for column in column_with_nan:
        if columns:
            if column in columns:
                if df_out[column].isnull().sum()*100.0/df_out.shape[0] >= threshold:
                    df_out = df_out.drop(column, 1)
                    print(f'Column deleted: {column}')
        else:
            if df_out[column].isnull().sum()*100.0/df_out.shape[0] >= threshold:
                df_out = df_out.drop(column, 1)
                print(f'Column deleted: {column}')
    return df_out

def remove_duplicate_rows(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
    """ 
    Returns a copy of your DataFrame with duplicate rows removed

    df: pandas DataFrame
    columns: (Optional) List of column names to check for duplicates in
    """
    df_out = df.copy(deep=True)
    #df_out = df_out.reset_index(drop=False)
    #df_out.rename(columns = {'index':'indexInOrigDF'}, inplace = True)
    if columns:
        drop_us = pd.Int64Index([])
        for column in columns:
            drop_us = drop_us.append(df_out[df_out.duplicated([column])].index)
    else:
        drop_us = df_out.index[df_out.duplicated()]
    print(f'Dropping {drop_us.shape[0]} rows')
    df_out = pd.DataFrame(df_out.drop(drop_us, 0))
    return df_out

def remove_rows_with_missing_data(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
    """
    Returns a copy of your DataFrame after removing all rows 
    containing NULL or NaN values in any of their columns
    
    df: pandas DataFrame
    columns: (Optional) List of column names to check for nulls, Defaults to All
    """
    df_out = df.copy(deep=True)
    if columns:
        index_with_nan = pd.Int64Index([])
        for column in columns:
            index_with_nan = index_with_nan.append(df_out[df_out[column].isnull()].index)
    else:
        index_with_nan = df_out.index[df_out.isnull().any(axis=1)]
    print(f'Dropping {index_with_nan.shape[0]} rows')
    df_out = pd.DataFrame(df_out.drop(index_with_nan))
    return df_out