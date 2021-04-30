import re
import pandas as pd
from typing import Union, List

from hipar.types import Condition, Pattern


def is_discretized(p : Condition) :
    predicate_text = p[0]
    return '>' in predicate_text or '<' in predicate_text

def extract_predicate_from_single_pattern(p : Condition) :
    ## If it is a discretized condition
    if is_discretized(p) :
        match = re.search(r"([-_a-zA-Z0-9]+)[><]=?", p[0])
        return match.group(1)
    else :
        return p[0]

def extract_value_from_discretized_predicate(p : str) :
    match = re.search(r"([-_a-zA-Z0-9]+)[><]=?([0-9]*.?[0-9]+)", p)
    return float(match.group(2))

## Given two patterns, it checks whether they share conditions about the same predicate
## (This is important to avoid redundancy)
def get_predicates(p : Union[Pattern, Condition], reference_list : List[str] = None) :
    if is_single_tuple(p) :
        pred = extract_predicate_from_single_pattern(p)
        if reference_list is None or pred in reference_list:
            return [pred]
        else :
            return []
    else :
        predicates = []
        for p_c in p :
            predicates.extend(get_predicates(p_c, reference_list))

        return predicates

def share_predicate(p1 : Union[Pattern, Condition], p2 : Union[Pattern, Condition]) :
    return len(set(get_predicates(p1)) & set(get_predicates(p2))) > 0

## Check if the pattern consists of a single condition
def is_single_tuple(p : Union[Pattern, Condition]) :
    return isinstance(p, tuple) and len(p) == 2 and not isinstance(p[0], tuple) and not isinstance(p[1], tuple)

def _and_(p1 : Union[Pattern, Condition], p2 : Union[Pattern, Condition]) :
    if is_single_tuple(p1) :
        p1_prime = (p1, )
    else :
        p1_prime = p1

    if is_single_tuple(p2) :
        p2_prime = (p2, )
    else :
        p2_prime = p2

    return sorted(p1_prime + p2_prime)


def matches_condition(condition : Condition, data_point : pd.Series) :
    predicate = extract_predicate_from_single_pattern(condition)
    if predicate == condition[0] :
        value = data_point[predicate]
        return value == condition[1]
    else :
        ## It is a discretized
        value = data_point[predicate]
        return eval(condition[0], {predicate : value}, {}) == condition[1]

def matches(pattern : Pattern, data_point : pd.Series):
    for condition in pattern:
        if not matches_condition(condition, data_point):
            return False
    return True

def are_correlated_discretized_patterns(p1 : Condition, p2 : Condition) :
    predicate1 = extract_predicate_from_single_pattern(p1)
    predicate2 = extract_predicate_from_single_pattern(p2)
    return predicate1 == predicate2 and p1[1] != p2[1]
