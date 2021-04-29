import numpy as np
# from wizzi_utils import misc_tools as mt
# import sklearn
from sklearn import cluster


def find_centers(A: np.array, k: int = 1) -> np.array:
    """
    :requires: sklearn
    :param A: nx(d+1) data array. A=X|y
    :param k: how many centers
    :return: centers kxd
    see find_centers_test()
    """
    k_means_obj = cluster.KMeans(n_clusters=k)
    k_means_obj.fit(A)
    centers = k_means_obj.cluster_centers_
    return centers
