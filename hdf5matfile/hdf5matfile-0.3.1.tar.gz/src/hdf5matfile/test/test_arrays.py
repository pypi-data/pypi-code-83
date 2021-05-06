import numpy as np

from . import assert_array_equal, get_var_loader

load_var = get_var_loader('test_arrays.mat')


def test_scalar():
    a0 = load_var('a0')
    assert_array_equal(a0, np.array([[1.]]))


def test_1d():
    a1 = load_var('a1')
    assert_array_equal(a1, np.array([[1., 2., 3.]]))


def test_2d():
    a2 = load_var('a2')
    assert_array_equal(a2, np.array([[1., 2., 3.], [4., 5., 6.]]))


def test_3d():
    a3 = load_var('a3')
    assert_array_equal(a3, np.ones((2, 3, 4)))
