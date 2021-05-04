"""
TODO: Add power spectrum plotting for pandas as well as numpy, separate out the two.
"""
import numpy as np
import pandas as pd
from scipy.signal.windows import hann
from sciparse import sampling_period, title_to_quantity, to_standard_quantity, quantity_to_title, column_from_unit, frequency_bin_size
import re
from spectralpy import ureg
from scipy.optimize import curve_fit
import pint

@np.vectorize
def sinc(x):
    if abs(x) < 1e-8:
        return 1
    else:
        return np.sin(x) / x

@np.vectorize
def dirichlet(W, n):
    """
    :param W: Discrete-time angular frequency
    :param n: Number of sample points in time domain (NOT frequency domain)
    """
    if abs(W) < 1e-8:
        return 1
    else:
        return 1/n * np.sin(n*W/2) / np.sin(W/2) * np.exp(-1j*W/2*(n-1))

@np.vectorize
def hann_dtft(W, n):
    return 0.5 * (dirichlet(W, n) - 0.5 * \
            (dirichlet(W - 2*np.pi/(n-1), n) + dirichlet(W + 2*np.pi/(n-1), n)))

def hann_norm(n_samples):
    hann_normalized = hann(n_samples) / np.sqrt(np.mean(np.square(hann(n_samples))))
    return hann_normalized

def generate_window(n_samples, window='hann'):
    if window == 'box' or window == 'boxcar':
        window_data = np.ones(n_samples)
    elif window == 'hann':
        window_data = hann_norm(n_samples)
    else:
        raise ValueError(
            f'Window type {window} not supported. Supported types are \
            box and hann')
    return window_data

def power_spectrum(data, window='hann', siding='single', amplitude=False):
    """
    Computes the single-or double-sided power spectrum with different types
    of filetring (hann, boxcar)

    :param data: data to be transformed
    :param window: window type - hann or box
    :param amplitude: Whether to return the power spectrum or the amplitude spectrum
    :param siding: 'single' or 'double' sided spectrum.

    """
    n_samples = len(data)
    window_data = generate_window(n_samples, window=window)

    if isinstance(data, np.ndarray):
        power_spectrum = power_spectrumNumpy(
            data, window_data, siding=siding, amplitude=amplitude)
    elif isinstance(data, pd.DataFrame):
        power_spectrum = power_spectrum_pandas(
            data, window_data=window_data, siding=siding, amplitude=amplitude)
    else:
        raise ValueError(f"Function not implemented for type {type(data)},"+
                         "only np.ndarray, pd.DataFrame.")

    return power_spectrum

def power_spectrum_pandas(data, window_data=1, siding='single',
        amplitude=False):
    """
    Implementation of powerSpectrum for a pandas DataFrame.

    :param window_data: Raw window data to multiply the time-domain data by
    :param amplitude: Whether to return the power spectrum or the amplitude spectrum
    :param siding: single or double (sinusoidal or exponential)
    """
    n_samples = len(data)
    half_data_length = int(n_samples/2+1)
    Ts = sampling_period(data)
    fs = (1 / Ts).to(ureg.Hz)
    fs_Hz = fs.to(ureg.Hz).magnitude

    power_quantity = title_to_quantity(data.columns.values[1])

    frequencies = np.linspace(0,
            fs_Hz* (n_samples - 1) / (n_samples),
            n_samples)

    if amplitude == False:
        power_quantity = power_quantity ** 2

    power_quantity = to_standard_quantity(power_quantity)
    power_title = quantity_to_title(power_quantity)
    frequency_title = quantity_to_title(fs)

    if siding == 'single':
        frequencies = double_to_single(frequencies, freq=True)
    elif siding == 'double':
        pass
    else: raise ValueError(f'No such siding {siding}. Available sidings are "single" and "double"')


    fft_data = power_quantity.magnitude * power_spectrumNumpy(
        data.iloc[:,1].values,
        window_data=window_data, siding=siding, amplitude=amplitude)
    overall_data = pd.DataFrame(
        {frequency_title: frequencies, power_title: fft_data})
    return overall_data

def power_spectrumNumpy(data, window_data=1, siding='single',
        amplitude=False):
    """
    Implementation of powerSpectrum for numpy arrays.

    :param data: Input data (numpy array)
    :param window_data: Raw window data to multiply the data by
    :param siding: single or double (sinusoidal or complex)
    :param amplitude: Whether to return the power spectrum or the amplitude spectrum
    :returns power_spectrum: Power spectrum as a numpy array

    """
    spectrum = np.fft.fft(data * window_data / len(data))
    if amplitude == False:
        spectrum = np.square(np.abs(spectrum))
        if siding == 'single':
            spectrum = double_to_single(spectrum)
    return spectrum

def double_to_single(spectrum, freq=False):
    """
    Converts a single-sided spectrum into a double-sided spectrum

    :param spectrum: Spectrum to convert from double sided to single-sided.
    :param freq: If the data is stand-alone frequency data that should not be power-corrected
    """
    if isinstance(spectrum, np.ndarray):
        n_samples = len(spectrum)
        half_data_length = int(n_samples/2+1)
        new_spectrum = spectrum[0:half_data_length]
        if freq == False:
            # DC component does not need to be corrected.
            new_spectrum *= 2
            new_spectrum[0] /= 2
            if n_samples % 2 == 0:
                new_spectrum[-1] /= 2
    else:
        raise ValueError(f'double_to_single not implemented for type {type(spectrum)}')
    return new_spectrum

def psd_weights(data, frequency, window='hann', siding='single', amplitude=False):
    """
    Computes the PSD weights for an ideal sinewave of a given frequency

    :param frequency: Desired frequency to extract
    :param data: Time-domain data we want the frequency-domain weights of
    :param window: Window type. Options are "hann" or "boxcar"
    :param power: Whether to give magnitude squared (if true) or amplitude (if false)
    """
    n_samples = len(data)
    ts = sampling_period(data)
    W0 = 2*np.pi * frequency * ts
    if isinstance(W0, pint.Quantity):
        W0 = W0.to(ureg.rad).m
    W_max = 2*np.pi * (n_samples - 1) / n_samples
    W_min = 0
    W = np.linspace(W_min, W_max, n_samples)

    if window == 'box' or window == 'boxcar':
        weights = 0.5*dirichlet(W - W0, n_samples) + 0.5*dirichlet(W + W0, n_samples)
    elif window == 'hann' or window == 'hanning':
        weights = 0.5 * hann_dtft(W - W0, n_samples) + 0.5*hann_dtft(W + W0, n_samples)

    if amplitude == False:
        weights = abs(weights) ** 2
        weights /= np.sum(weights)
        if siding == 'single': # properly treat DC component
            weights = double_to_single(weights)
            # for the pathalogical case that the frequency is exactly pi:
    else:
        weights /= np.sqrt(np.sum(np.square(np.abs(weights))))

    return weights

def extract_power(data, frequency, window='hann', siding='double'):
    """
    Extracts the power of a desired frequency from a power spectral density, accounting for spectral leakage and frequency bin size
    TODO: NEEDS TO FIT OR KNOW THE PHASE OF THE SINEWAVE OF INTEREST. RIGHT NOW IT FAILS WHEN THE SIGNAL IS NOT A PERFECT COSINE.

    :param data: Time-domain data
    :param frequency: Desired frequency power to extract
    :param window: Window type. Options are "hann" or "boxcar"
    :param siding: Whether the input spectrum is single-sided or double-sided
    """
    ts = sampling_period(data)
    n_samples = len(data)
    spectrum = power_spectrum(data, window=window, siding=siding, amplitude=True)
    power_quantity = title_to_quantity(spectrum.columns.values[1]) ** 2
    known_spectrum = psd_weights(data, frequency, window=window, siding=siding, amplitude=True)
    if isinstance(spectrum, pd.DataFrame):
        spectrum_product = np.abs(spectrum.iloc[:,1].values) * np.abs(known_spectrum)
    elif isinstance(spectrum, np.ndarray):
        spectrum_product = np.abs(spectrum) * np.abs(known_spectrum)
     # Take only the real part. Not sure how kosher this is.
    spectrum_integral = np.square(np.real(np.sum(spectrum_product)))

    return spectrum_integral * power_quantity
