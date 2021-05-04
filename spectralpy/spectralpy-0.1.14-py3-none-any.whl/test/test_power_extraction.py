import pytest
import os
import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_allclose
from sciparse import assert_allclose_qt, assert_equal_qt
from pandas.testing import assert_frame_equal
from spectralpy import power_spectrum, hann_norm, generate_window, psd_weights, ureg, dirichlet, extract_power, hann_dtft

dir_path = os.path.dirname(os.path.realpath(__file__))

@pytest.fixture
def real_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = pd.read_csv(dir_path + '/data/NL_test_data_10k.csv')
    real_equation = 'sin(x) * 1e-3 * cos(2x) + 1e-6 * sin(3x)'
    yield data

def test_hann_norm():
    n_samples = 5
    hann_data = hann_norm(n_samples)
    desired_data = np.array([0, 0.5, 1, 0.5, 0]) / 0.5477225575051661
    actual_data = hann_norm(n_samples)
    assert_equal(actual_data, desired_data)

def test_generate_window_hann():
    n_samples = 5
    hann_data = hann_norm(n_samples)
    desired_data = np.array([0, 0.5, 1, 0.5, 0]) / 0.5477225575051661
    actual_data = generate_window(n_samples, window='hann')
    assert_equal(actual_data, desired_data)

def test_generate_window_boxcar():
    n_samples = 5
    desired_data = np.ones(n_samples)
    actual_data = generate_window(n_samples, window='boxcar')
    assert_equal(actual_data, desired_data)

def test_generate_psd_weights_no_leak_double():
    """
    Checks the PSD coefficients are correct when we have an integer number of periods
    """
    data = pd.DataFrame({
            'time (s)': [0, 1, 2, 3],
            'data': [-1, 1, -1, 1]})
    desired_weights = np.array([0, 0, 1, 0])
    actual_weights = psd_weights(data , 0.5*ureg.Hz, window='box', siding='double', amplitude=False)
    assert_allclose(actual_weights, desired_weights, atol=1e-10)

def test_generate_psd_weights_no_leak_single():
    """
    Checks the PSD coefficients are correct when we have an integer number of periods
    """
    data = pd.DataFrame({
            'time (s)': [0, 1, 2, 3],
            'data': [-1, 1, -1, 1]})
    desired_weights = np.array([0, 0, 1])
    actual_weights = psd_weights(data , 0.5*ureg.Hz, window='box', siding='single', amplitude=False)
    assert_allclose(actual_weights, desired_weights, atol=1e-10)

def test_generate_psd_weights_leak_double():
    """
    Checks the PSD coefficients are correct when we have a simple sinewave at maximum frequency with a half-integer number of periods.
    """
    frequencies = np.array([0, 1, 2, 3])*1/7
    desired_weights = np.array([0.04000000000000001, 0.061114561800016814, 0.4188854381999833,0.4188854381999833, 0.061114561800016814])
    data = pd.DataFrame({
            'time (s)': [0, 1, 2, 3, 4],
            'Value': [1, -1, 1, -1, 1]})
    signal_frequency = 0.5*ureg.Hz
    actual_weights = psd_weights(data, signal_frequency, window='box', siding='double', amplitude=False)
    assert_allclose(actual_weights, desired_weights)

def test_generate_psd_weights_noleak_single():
    """
    Checks the PSD coefficients are correct when we have a simple sinewave at maximum frequency with a half-integer number of periods.
    """
    frequencies = np.array([0, 1, 2, 3])*1/7
    desired_weights = np.array([0.04000000000000001, 0.061114561800016814, 0.4188854381999833,0.4188854381999833, 0.061114561800016814])
    data = pd.DataFrame({
            'time (s)': [0, 1, 2, 3, 4],
            'Value': [1, -1, 1, -1, 1]})
    signal_frequency = 0.5*ureg.Hz
    actual_weights = psd_weights(data, signal_frequency, window='box', siding='double', amplitude=False)
    assert_allclose(actual_weights, desired_weights)

def test_generate_psd_weights_hann():
    desired_weights = np.array([
            0.,
            0.06366100187501754,
            0.43633899812498245,
            0.43633899812498245,
            0.06366100187501754])
    data = pd.DataFrame({
            'time (s)': [0, 1, 2, 3, 4],
            'Value': [1, -1, 1, -1, 1]})
    signal_frequency = 0.5*ureg.Hz
    actual_weights = psd_weights(data, signal_frequency, window='hann', siding='double', amplitude=False)
    assert_allclose(actual_weights, desired_weights, atol=1e-10)

def test_dirichlet_non_vectorized():
    n_samples = 5
    W = 3 * np.pi / 5
    desired_val = 0.19999999999999996 - 1j*0.1453085056010722
    actual_val = dirichlet(W, n_samples)
    assert_allclose(actual_val, desired_val)

def test_dirichlet_vectorized():
    n_samples = 5
    W = 3 * np.pi / 5
    desired_val = 0.19999999999999996 - 1j*0.1453085056010722
    desired_vals = np.array([desired_val, desired_val])
    actual_vals = dirichlet(np.array([W, W]), n_samples)
    assert_allclose(actual_vals, desired_vals)

def test_hann_dtft_single():
    n_samples = 5
    window = np.array([0, 0.5, 1, 0.5, 0])
    W = 2*np.pi/5
    desired_value = -0.21180339887498945 - 0.15388417685876268j
    actual_value = hann_dtft(W, n_samples)
    assert_allclose(actual_value, desired_value)

def test_hann_dtft_vector():
    n_samples = 5
    window = np.array([0, 0.5, 1, 0.5, 0])
    W = 2*np.pi * np.array([0, 1/5, 2/5, 3/5, 4/5])
    desired_values = np.array([
            0.4,
            -0.21180339887498945 - 0.15388417685876268j,
            0.011803398874989502 + 0.03632712640026803j,
            0.011803398874989502 - 0.03632712640026803j,
            -0.21180339887498945 + 0.15388417685876268j])
    actual_values = hann_dtft(W, n_samples)
    assert_allclose(actual_values, desired_values)

def test_extract_power_double_sided_no_leak():
    """
    """
    data = pd.DataFrame({
            'Time (s)': [0, 1, 2, 3],
            'Value (A)': [1, -1, 1, -1]})
    desired_power = 1*ureg.A ** 2
    frequency = 0.5 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)

def test_extract_power_double_sided_sinewave():
    """
    """
    data = pd.DataFrame({
            'Time (s)': [0, 1, 2, 3],
            'Value (A)': [0, 1, 0, -1]})
    desired_power = 0.5*ureg.A ** 2
    frequency = 0.25 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)


def test_extract_power_double_sided_no_leak_doubled():
    """
    """
    data = pd.DataFrame({
            'Time (s)': [0, 1, 2, 3],
            'Value (A)': [2, -2, 2, -2]})
    desired_power = 4*ureg.A ** 2
    frequency = 0.5 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)

def test_extract_power_double_sided_no_leak():
    """
    """
    data = pd.DataFrame({
            'Time (s)': [0, 1, 2, 3],
            'Value (A)': [1, -1, 1, -1]})
    desired_power = 1*ureg.A ** 2
    frequency = 0.5 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)

    frequency = 0.5 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)

def test_extract_power_double_sided_no_leak_diff_units():
    """
    """
    data = pd.DataFrame({
            'Time (ms)': [0, 1, 2, 3],
            'Value (A)': [1, -1, 1, -1]})
    desired_power = 1*ureg.A ** 2
    frequency = 0.5 * ureg.kHz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)

def test_extract_power_double_sided_with_leak():
    """
    """
    data = pd.DataFrame({
            'Time (s)': [0, 1, 2, 3, 4],
            'Value (A)': [1, -1, 1, -1, 1]})
    desired_power = 1*ureg.A ** 2
    frequency = 0.5 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='boxcar')
    assert_allclose_qt(actual_power, desired_power)

def test_extract_power_double_sided_with_leak_hann():
    """
    """
    data = pd.DataFrame({
            'Time (s)': [0, 1, 2, 3, 4],
            'Value (A)': [1, -1, 1, -1, 1]})
    desired_power = 1*ureg.A ** 2
    frequency = 0.5 * ureg.Hz
    actual_power = extract_power(data, frequency, siding='double', window='hann')
    assert_allclose_qt(actual_power, desired_power)

def test_extract_power_noiseless_data_first_harmonic(real_data):
    """
    """
    desired_power = 5e-19 * (ureg.A ** 2)
    frequency = 100 * ureg.Hz
    actual_power = extract_power(real_data, frequency, siding='double', window='hann')
    assert_allclose_qt(actual_power, desired_power, atol=1e-30, rtol=1e-5)

def test_extract_power_noiseless_data_second_harmonic(real_data):
    """
    """
    desired_power = 5e-19 * 1e-6 * (ureg.A ** 2)
    frequency = 2 * 100 * ureg.Hz
    actual_power = extract_power(real_data, frequency, siding='double', window='hann')
    assert_allclose_qt(actual_power, desired_power, atol=1e-28, rtol=1e-4)

def test_extract_power_noiseless_data_third_harmonic(real_data):
    """
    """
    desired_power = 5e-19 * 1e-12 * (ureg.A ** 2)
    frequency = 3 * 100 * ureg.Hz
    actual_power = extract_power(real_data, frequency, siding='double', window='hann')
    assert_allclose_qt(actual_power, desired_power, atol=1e-32, rtol=1e-3)
