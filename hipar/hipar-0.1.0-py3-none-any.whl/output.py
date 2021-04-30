import pandas as pd
from hipar.types import Pattern
from hipar.patterns import extract_predicate_from_single_pattern, is_discretized


def output_ids_list(alist : list, n=10) :
    '''
    It outputs the first 'n' elements of a list.
    :param alist: list,
    :param n: int
    :return: A string representation of the first 'n' elements of the list.
    '''
    if len(alist) <= n :
        return str(alist)
    else :
        missing = len(alist) - n
        return str(alist[:n]).replace(']', ', ...] (' + str(missing) + ' more)')

def simplify_pattern_for_output(pattern : Pattern) :
    '''
    It removes A tuple of atomic conditions
    :param pattern: A tuple of atomic conditions such as (('ETP_sum_4w<78.0999984741211', False), ('ETP_sum_4w>=152.10000610351562', False))
    :return: A new tuple of atomic conditions where redundant conditions for the same attribute are removed. In the previous
    example the first condition would be removed (positive conditions are preferred over negative conditions)
    '''
    pred_to_conditions_dict = {}
    for p in pattern :
        pred = extract_predicate_from_single_pattern(p)
        if pred not in pred_to_conditions_dict :
            pred_to_conditions_dict[pred] = []

        pred_to_conditions_dict[pred].append(p)

    new_pattern = []
    for pred, conditions in pred_to_conditions_dict.items() :
        ## It must be discretized
        ## Search for the positive condition
        add_everything = True
        for p in conditions :
            if is_discretized(p) and p[1] == True :
                new_pattern.append(p)
                add_everything = False
                break


        if add_everything :
            new_pattern.extend(conditions)

    return tuple(new_pattern)

def clean_for_display(df: pd.DataFrame) :
    '''
    It takes the output of HiPaR and creates a new data frame with user-friendly versions of the columns
    'condition' and 'model'
    :param df: A Pandas dataframe containing a set of hybrid rules as output by HiPaR.get_selected_rules() or
    Hipar.all_rules
    :return: DataFrame
    '''
    cleaned_conditions = []
    for index, row in df.iterrows() :
        cleaned_conditions.append((index, simplify_pattern_for_output(row['condition'])))