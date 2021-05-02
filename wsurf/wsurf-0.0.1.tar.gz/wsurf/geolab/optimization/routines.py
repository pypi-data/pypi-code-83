

from scipy import sparse


def spdot(A, B):
    return sparse.spmatrix.dot(A, B)


def hdot(A):
    return sparse.spmatrix.dot(A, A.transpose())


def hdot_mkl(A):
    from geolab.optimization.sparse_mkl.sparse_dot import gram_matrix_mkl
    B = gram_matrix_mkl(A)
    B = B + sparse.triu(B, 1).transpose()
    return B
