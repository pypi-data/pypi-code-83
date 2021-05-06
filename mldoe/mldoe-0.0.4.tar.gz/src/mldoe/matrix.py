import numpy as np


def bmat(r: int, alt_coding: bool = False) -> np.array:
    """
    Create the full-interaction matrix (B) for :math:`r` basic factors.

    The B matrix is a :math:`2^r` by  :math:`2^r-1` matrix with the :math:`2^r-1` interactions of the columns
    representing the :math:`r` basic factors.

    :param r: number of basic factors
    :type r: int
    :param alt_coding: use (-1,+1) coding instead of (0,1) coding. Default to False (0,1).
    :type alt_coding: bool
    :return: full-interaction matrix
    :rtype: numpy.array
    """
    vec = np.array(range(int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    if alt_coding:
        return (np.array((mat[::-1].T @ mat[:, 1:]) % 2, dtype=int) * 2) - 1
    return np.array((mat[::-1].T @ mat[:, 1:]) % 2, dtype=int)


def rmat(r: int, alt_coding: bool = False) -> np.array:
    """
    Create the basic factor matrix (R) for :math:`r` basic factors.

    The R matrix is a :math:`2^r` by  :math:`r` matrix where each column represents a basic factor and each row
    represents a run. The columns are ordered such that ith columns is a repetition of :math:`2^{(r-i)}` zeros and
    :math:`2^{(r-i)}` ones.

    :param r: number of basic factors
    :type r: int
    :param alt_coding: use (-1,+1) coding instead of (0,1) coding. Default to False (0,1).
    :type alt_coding: bool
    :return: basic factor matrix
    :rtype: numpy.array
    """
    vec = np.array(range(int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    if alt_coding:
        return (np.array(mat[::-1].T, dtype=int) * 2) - 1
    return np.array(mat[::-1].T, dtype=int)


def gmat(r: int, alt_coding: bool = False) -> np.array:
    """
    Create the reduced interaction (G) matrix for :math:`r` basic factors.

    The G matrix is a :math:`r` by  :math:`2^r-1` matrix where each column represents an interaction and each row
    represents a basic factor. An entry of 1 means that the :math:`i`-th basic factor is used in the :math:`j`-th
    interaction.

    :param r: number of basic factors
    :type r: int
    :param alt_coding: use (-1,+1) coding instead of (0,1) coding. Default to False (0,1).
    :type alt_coding: bool
    :return: reduced interaction matrix
    :rtype: numpy.array
    """
    vec = np.array(range(1, int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    if alt_coding:
        return (np.array(mat, dtype=int) * 2) - 1
    return np.array(mat, dtype=int)
