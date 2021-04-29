import finesse
from finesse.cmatrix import KLUMatrix
import numpy as np
import pytest

def test_fill_za_zmvc():
    M = KLUMatrix('M')
    M.add_diagonal_elements(3, 0, 'a')
    M.add_diagonal_elements(3, 1, 'b')
    M.add_diagonal_elements(1, 2, 'c')

    Vac = M.get_sub_matrix_view(0, 2, 'a->c', False)
    Vbc = M.get_sub_matrix_view(1, 2, 'b->c', True)

    Vca = M.get_sub_matrix_view(2, 0, 'c->a', False)
    Vcb = M.get_sub_matrix_view(2, 1, 'c->b', True)

    M.construct()

    I = np.array([
        [1,2j,3],
        [4,5,6j],
        [7,8j,9]], dtype=np.complex128)
    V = np.array([1,2j,3], dtype=np.complex128)

    Vac.do_fill_za_zmvc(3j, I, V)
    assert((abs(Vac.view - 3j*(I@V)) < 1e-15).all())

    Vbc.do_fill_za_zmvc(3j, I, V)
    assert((abs(Vbc.view - (3j*I@V).conj()) < 1e-15).all())

    Vca.do_fill_za_zmvc(3j, I, V)
    assert((abs(Vca.view.T - 3j*I@V) < 1e-15).all())

    Vcb.do_fill_za_zmvc(3j, I, V)
    assert((abs(Vcb.view.T - (3j*I@V).conj()) < 1e-15).all())
