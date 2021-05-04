import numpy as np
import scipy as sp

def convert_pure(sparse, single_sidelength, len_x):
    """
    Info:
    Args:
    Returns:
    """
    with_log = False

    sidelength = single_sidelength*len_x
    data = list()

    for i in range(len(sparse)):
        var = sparse[i]
        val1 = int(var)%sidelength
        val2 = int(int(var)/sidelength)
        val = (val1, val2)
        if with_log: 
            print("\n val: ", val)
        if val1 != val2 and val1 > val2: # TODO: Originally it was val1 < val2, why did 
                                         #    we now have to turn it around?
            #data[i][0] = val1
            #data[i][1] = val2
            data.append([val1, val2])
        else:
            pass
            #print("\n data i: ", i, "; equal val1: ", val1, "; val2: ", val2)
        if with_log: 
            print("\n data: ", data)

    data_dense = dense_matrix(data, sidelength)
    return data_dense

# TODO: Actually this function is copy-pasted from our other script - 
#     organize, that we don't write the same function twice
def dense_matrix(data, len_xy):
    """
    Info: 
    Args:
    Returns: 
    """
    
    with_log = False
    if with_log: 
        print("\n data_in: ", data)
    rows = [el[0] for el in data]
    cols = [el[1] for el in data]
    vals = [1 for el in data]

    dense_matrix = sp.sparse.coo_matrix((vals, (rows, cols)), shape=(len_xy, len_xy)).toarray()
    return dense_matrix

