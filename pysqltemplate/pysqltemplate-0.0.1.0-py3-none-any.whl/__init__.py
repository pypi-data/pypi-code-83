def flatten(array):
    """ Returns: an array of strings that are the recursive flattening of phrases and nested objects that themselves contain multiple phrases """
    result = []
    for item in array:
        if type(item) in (list, tuple):
            result.extend(flatten(item))
        elif isinstance(item, Clause):
            result.append(item.sql())
        else:
            result.append(item)
    return(result)

from .clause import *
from .query import Query

