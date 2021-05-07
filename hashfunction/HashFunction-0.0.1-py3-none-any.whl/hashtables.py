import operator as op
import itertools as ittls
from .hashfunctions import alphanumeric_hash_function, numeric_hash_function


def hash_table(data, key_index):

    def hash_function(value):

        if type(value) == str:
            return alphanumeric_hash_function(value, n)
        elif type(value) == int:
            return numeric_hash_function(value, n)
        else:
            raise SystemError

    n = len(data)
    key_list = [x for x in [
        list(vec.keys())[0]
        for vec in data
    ]]

    hash_gen = map(hash_function, key_list)
    ret = list(range(n))

    for i in iter(data):
        index = next(hash_gen)

        if type(ret[index]) == list:
            ret[index].append(i)
        else:
            ret[index] = [i]
    return ret


def hash_table_alphanumeric(data, key_index):

    n = len(data)
    key_list = [x for x in [
        list(vec.keys())[0]
        for vec in data
    ]]

    hash_gen = map(alphanumeric_hash_function,
                   key_list, ittls.repeat(n))

    ret = list(range(n))
    for i in iter(data):
        index = next(hash_gen)

        if type(ret[index]) == list:
            ret[index].append(i)
        else:
            ret[index] = [i]

    return ret


def hash_table_numeric(data, key_index):

    n = len(data)
    key_list = [x for x in [
        list(vec.keys())[0]
        for vec in data
    ]]

    hash_gen = map(numeric_hash_function,
                   key_list, ittls.repeat(n))

    ret = list(range(n))
    for i in iter(data):
        index = next(hash_gen)

        if type(ret[index]) == list:
            ret[index].append(i)
        else:
            ret[index] = [i]

    return ret


def get_data(table, key_index, key):

    n = len(table)

    if type(key) == str:
        index = alphanumeric_hash_function(key, n)
    else:
        index = numeric_hash_function(key, n)

    return list(filter(
        lambda x: list(x.keys())[key_index] == key,
        table[index]
    ))


def insert_data(table, key_index, value):

    destruct_list = [x for x in table if type(x) == list]
    final_list = [y for x in destruct_list for y in x]
    values = op.add(final_list, value)
    return hash_table(values, key_index)


def update_data(table, key_index, key, value):

    n = len(table)

    if type(key) == str:
        index = alphanumeric_hash_function(key, n)
    else:
        index = numeric_hash_function(key, n)

    table[index] = list(map(
        lambda x: value if list(x.keys())[key_index] == key else x,
        table[index]
    ))

    return table


def del_data(table, key_index, key):

    n = len(table)

    if type(key) == str:
        index = alphanumeric_hash_function(key, n)
    else:
        index = numeric_hash_function(key, n)

    table[index] = list(filter(
        lambda x: list(x.keys())[key_index] != key,
        table[index]
    ))

    destruct_list = [x for x in table if type(x) == list]
    final_list = [y for x in destruct_list for y in x]

    return hash_table(final_list, key_index)
