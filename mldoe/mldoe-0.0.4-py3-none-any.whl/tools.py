import numpy
from math import factorial
from numba import njit
from typing import List


@njit(cache=True)
def weight_dist(d_mat: numpy.array):
    """
    Compute the weight distribution of a design matrix.
    The weight distribution B is a vector such that :math:`B_i = j` when there are j rows with i non-zero entries in the
    design matrix.

    :param d_mat: design matrix
    :type d_mat: numpy.array (2D)
    :return: weight distribution vector
    :rtype: numpy.array (1D)
    """
    row_sum = d_mat.sum(1)
    b_vec = numpy.zeros(d_mat.shape[1] + 1)
    for i in range(len(row_sum)):
        b_vec[row_sum[i]] += 1
    return b_vec


def krawtchouck(n: int):
    """
    Builds a :math:`n` by :math:`n` matrix of all the Krawtchouck polynomial values for :math:`j = 1,\ldots,n` and
    :math:`x = 1,\ldots,n`, with a given value for :math:`n`. All values are computed using the recursive formula from
    Xu [2009]_:

    * if :math:`j = 0` then :math:`P_j(x,n)=1`
    * if :math:`j = 0` then :math:`P_j(x,n)={n \choose j}`
    * in other cases :math:`P_j(x,n)= P_j(x-1,n) - P_{j-1}(x,n) - P_{j-1}(x-1,n)`

    :param n: number of factors in the design
    :type n: int
    :return: :math:`n` by :math:`n` matrix of all the Krawtchouck polynomial values :math:`P_j(x,n)`
    :rtype: numpy.array
    """
    const = factorial(n)
    mat = numpy.zeros((n+1, n+1))
    mat[0, :] = 1
    for j in range(1, n+1):
        mat[j, 0] = const / (factorial(j) * factorial(n - j))
        for x in range(1, n+1):
            mat[j, x] = mat[j, x - 1] - mat[j - 1, x] - mat[j - 1, x - 1]
    return mat


def wlp_vec(d_mat: numpy.array, r_min: int = 3):
    run_size, n_fac = d_mat.shape
    w_vec = numpy.zeros(n_fac + 1)
    weight_dist_vec = weight_dist(d_mat)
    krawtchouck_mat = krawtchouck(n_fac+1)
    for j in range(r_min, n_fac+1):
        sum_j = 0
        for i in range(n_fac+1):
            sum_j += (krawtchouck_mat[j, i] * weight_dist_vec[i])
        w_vec[j] = (1 / run_size) * sum_j
    return w_vec


@njit(cache=True)
def del_col(arr: numpy.array, num: int):
    """Delete-one-factor projection (DOP) of an array. Numba implementation of the numpy.delete function.
    Deletes the column, referred in num, of the array

    :param arr: 2-D array
    :type arr: numpy.array
    :param num: column to delete
    :type num: int
    :return: DOP of the input 2-D array
    :rtype: numpy.array
    """
    n_runs, n_cols = arr.shape
    arr_flat = arr.T.flatten()
    mask = numpy.zeros(n_runs * n_cols, dtype=numpy.int64) == 0
    mask[n_runs * num:n_runs * (num + 1)] = False
    new_arr = arr_flat[mask]
    return numpy.reshape(new_arr, (n_cols - 1, n_runs)).T


@njit(cache=True)
def kt_value(mat: numpy.array, q: int = 1, t: int = 10):
    """Moment projection pattern.
    Frequency vector of the t-th power Kt moment values.
    Values are computed on the projections of the input matrix into n-1, ..., n-q factors.
    For q=1 the MPP is a n-by-1 vector.
    For q=2 the MPP is a n-by-(n-1) matrix.

    :param mat: 2-D binary array
    :type mat: numpy.array
    :param q: level of projection, defaults to 1, maximum is 2
    :type q: int, optional
    :param t: power of the Kt moment, defaults to 10
    :type t: int, optional
    :return: tuple of the frequency vector for q=1 and the frequency matrix for q=2
    :rtype: tuple
    """
    n_cols = mat.shape[1]
    vec_q1 = numpy.zeros(n_cols)
    vec_q2 = numpy.zeros((n_cols, n_cols - 1))
    for i in range(n_cols):
        mat_dop = del_col(mat, i)
        mat_dop_dd = weight_dist(mat_dop)
        kt_val = 0.0
        for idx, val in enumerate(mat_dop_dd):
            kt_val += (n_cols - 1 - idx) ** t * val[0]
        vec_q1[i] = kt_val

        if q == 2:
            for j in range(n_cols - 1):
                mat_dop2 = del_col(mat_dop, j)
                mat_dop2_dd = weight_dist(mat_dop2)
                kt_val2 = 0.0
                for idx2, val2 in enumerate(mat_dop2_dd):
                    kt_val2 += (n_cols - 2 - idx2) ** t * val2[0]
                vec_q2[i, j] = kt_val2
    return vec_q1, vec_q2

    
    
