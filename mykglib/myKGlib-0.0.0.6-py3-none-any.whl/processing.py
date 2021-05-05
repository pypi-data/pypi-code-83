import re
import pandas as pd
from pandas import json_normalize
from SPARQLWrapper import SPARQLWrapper
from difflib import SequenceMatcher

def set_mode(mode_input):
    """
    check mode of the mode input

    Parameters:
        (string) mode_input: The mode input

    Returns:
        (list) mode: The available mode   
    """
    mode = None
    modes = ['ImageGrid', 'Timeline', 'Graph', 'Dimensions', 'Map', 'Tree',
                        'WordCloud', 'LineChart', 'BarChart', 'Histogram' ,'DensityPlot',
                        'TreeMap' ,'SunBurstChart', 'HeatMap' ,'PieChart', 'DonutChart',
                        'BoxPlot' ,'ViolinPlot', 'AreaChart', 'StackedAreaChart',
                         'ScatterChart', 'BubbleChart', 'Table']
    lowercase_modes = [name.lower() for name in modes]
    lowercase_input = mode_input.lower()
    
    highest_prob = 0
    for name in lowercase_modes:
        prob_now = SequenceMatcher(None, lowercase_input, name).ratio()
        if prob_now > highest_prob and prob_now >= 0.5:
            highest_prob = prob_now
            mode = name

    if lowercase_input in lowercase_modes:
        mode = lowercase_input

    if mode is None:
        raise Exception("No available mode")
    
    return mode


def set_dataframe(sparql_query, sparql_endpoint):
    """
    Query the endpoint with the given query string and format the result table

    Parameters:
        (string) sparql_query: The sparql query.
        (string) sparql_endpoint: The sparql endpoint

    Returns:
        (pandas.Dataframe) result_table: The table of result    
    """

    sparql = SPARQLWrapper(sparql_endpoint)  

    sparql.setQuery(sparql_query)
    sparql.setReturnFormat('json')

    results = sparql.query().convert()
    table  = json_normalize(results["results"]["bindings"])

    data_table = table[[column_name for column_name in table.columns if column_name.endswith('.value')]]
    data_table.columns = data_table.columns.str.rstrip('.value')

    rename_column_table = __rename_column_table(data_table)
    change_dtype_table = __change_dtypes(rename_column_table)
    result_table = change_dtype_table
    
    return result_table


def __rename_column_table(dataframe):
    """
    Rename column of dataframe based on regex validity check

    Parameters:
        (pandas.Dataframe) dataframe: The table

    Returns:
        (pandas.Dataframe) dataframe: The result table             
    """

    #Regex pattern
    pattern_url = r"^(?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$(?<!.[jpg|gif|png|JPG|PNG])" 
    pattern_img = r"^http(s)?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|jpeg|gif|png|JPG|JPEG|Jpeg)$"        
    pattern_coordinate = r"^Point"

    for i in range (len(dataframe.columns)):
        check = dataframe[dataframe.columns[i]].iloc[0]
        if re.match(pattern_url, check):
            if 'uri' in dataframe.columns:
                if 'uri2' in dataframe.columns:
                    dataframe = dataframe.rename(columns={dataframe.columns[i]: "uri_"+str(dataframe.columns[i])}, errors="raise")
                else:          
                    dataframe = dataframe.rename(columns={dataframe.columns[i]: "uri2"}, errors="raise")
            else:
                dataframe = dataframe.rename(columns={dataframe.columns[i]: "uri"}, errors="raise")
        elif re.match(pattern_img, check): 
            dataframe =  dataframe.rename(columns={dataframe.columns[i]: "picture"}, errors="raise")
        elif re.match(pattern_coordinate, check):
            dataframe =  dataframe.rename(columns={dataframe.columns[i]: "coordinate"}, errors="raise")
        else:
            pass

    return dataframe


def __change_dtypes(dataframe):
    """
    Change data type column of dataframe

    Parameters:
        (pandas.Dataframe) dataframe: The table

    Returns:
        (pandas.Dataframe) table: The result table             
    """

    for column in dataframe:
        try:
            dataframe[column] = dataframe[column].astype('datetime64')
        except ValueError:
            pass

    for column in dataframe:
        try:
            dataframe[column] = dataframe[column].astype('float64')
        except (ValueError, TypeError):
            pass

    return dataframe