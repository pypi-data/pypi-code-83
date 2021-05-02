import pyfftw
import numpy as np
from numpy.lib.stride_tricks import as_strided
from multiprocessing import cpu_count
from scipy.signal.windows import dpss

__all__ = ['compute_dpss',
           'mtm_spectrum',
           'mtm_spectrogram']

def compute_dpss(N, bandwidth, *, fs=1, n_tapers=None, min_lambda=0.95):
    
    NW = bandwidth * N / fs 
    K = int(np.ceil(2*NW)) - 1
    if K < 1:
        raise ValueError(f"Not enough tapers, with 'NW' of {NW}. Increase the bandwidth or"
                         " use more data points")
        
    tapers, lambdas = dpss(N, NW, Kmax=K, norm=2, return_ratios=True)
    mask = lambdas > min_lambda
    if not np.sum(mask) > 0:
        raise ValueError("None of the tapers satisfied the minimum energy concentration"
                         f" criteria of {min_lambda}")
    tapers = tapers[mask]
    lambdas = lambdas[mask]

    if n_tapers is not None:
        if n_tapers > tapers.shape[0]:
            raise ValueError(f"'n_tapers' of {n_tapers} is greater than the {tapers.shape[0]}"
                            f" that satisfied the minimum energy concentration criteria of {min_lambda}")
        tapers = tapers[:n_tapers]
        lambdas = lambdas[:n_tapers]
    
    return tapers, lambdas

def mtm_spectrum(data, bandwidth, *, n_tapers=None, min_lambda=0.95, fs=1,
                 remove_mean=False, nfft=None, n_fft_threads=cpu_count()):

    N = data.shape[0]
    tapers, lambdas = compute_dpss(N, bandwidth, fs=fs,
                                   n_tapers=n_tapers,
                                   min_lambda=min_lambda)
    n_tapers = tapers.shape[0]
    
    if nfft is None:
        nfft = N
        
    if remove_mean:
        data = data - data.mean()

    if np.isrealobj(data):
        M = nfft // 2 + 1

        xtd = pyfftw.zeros_aligned((n_tapers, nfft), dtype='float64')
        xfd = pyfftw.zeros_aligned((n_tapers, M), dtype='complex128')
        fft_sig = pyfftw.FFTW( xtd, xfd,
                               axes=(1, ),
                               direction='FFTW_FORWARD',
                               flags=['FFTW_ESTIMATE'],
                               threads=n_fft_threads,
                               planning_timelimit=0 )
        
        xtd[:, :N] = tapers * data
        xtd[:, N:] = 0
        fft_sig(normalise_idft=True)
        #assert np.allclose(xfd, np.fft.rfft(tapers * data, n=nfft))
        #xfd = np.fft.rfft(tapers * data, n=nfft)
        
        sdfs = (xfd.real**2 + xfd.imag**2) / fs
        
        if nfft % 2 == 0:
            sdfs[:, 1:-1] *= 2
        else:
            sdfs[:, 1:] *= 2

        freqs = np.fft.rfftfreq(nfft, d=1/fs)
    else:
        # can use an in-place transform here
        x = pyfftw.zeros_aligned((n_tapers, nfft), dtype='complex128')
        fft_sig = pyfftw.FFTW( x, x,
                               axes=(1, ),
                               direction='FFTW_FORWARD',
                               flags=['FFTW_ESTIMATE'],
                               threads=n_fft_threads,
                               planning_timelimit=0 )
        
        x[:, :N] = tapers * data
        x[:, N:] = 0
        fft_sig(normalise_idft=True)
        #assert np.allclose(xfd, np.fft.fft(tapers * data, n=nfft))

        sdfs = (x.real**2 + x.imag**2) / fs        
        freqs = np.fft.fftfreq(nfft, d=1/fs)

    mt_sdf = np.mean(sdfs, axis=0)
        
    #psd = xr.DataArray(psd, dims=['frequency'], coords={'frequency': freqs})

#     if outarray is None:
#         return psd
#     else:
#         return
#         #outarray[:, outind] = psd
        
    return mt_sdf, freqs


def mtm_spectrogram(data, bandwidth, *, fs=1, timestamps=None, nperseg=256, noverlap=0, n_tapers=None,
                    min_lambda=0.95, remove_mean=False, nfft=None,
                    n_fft_threads=cpu_count()):

    tapers, lambdas = compute_dpss(nperseg, bandwidth, fs=fs, n_tapers=n_tapers, min_lambda=min_lambda)
    N = data.shape[0]
    n_tapers = tapers.shape[0]
    
    if timestamps is None:
        timestamps = np.arange(N) / fs
        
    if timestamps.shape[0] != N:
        raise ValueError(f"Expected timestamps to contain {N} elements but got {timestamps.shape[0]}")
        
    estimated_fs = 1.0/np.median(np.diff(timestamps))
    if np.abs((estimated_fs - fs)/fs) > 0.01:
        print("Warning: estimated fs and provided fs differ by more than 1%")
    
    if nfft is None:
        nfft = nperseg
    if nfft < nperseg:
        raise ValueError(f"'nfft' must be at least {nperseg}")
        
    if nperseg > N:
        raise ValueError(f"'nperseg' cannot be larger than the data size {N}")
        
    if not N > noverlap:
        raise ValueError(f"'noverlap' cannot be larger than {N-1}")
        
    if remove_mean:
        data = data - data.mean()

    step = nperseg - noverlap
    shape = data.shape[:-1]+((data.shape[-1]-noverlap)//step, nperseg)
    strides = data.strides[:-1]+(step*data.strides[-1], data.strides[-1])
    data_strided = as_strided(data,
                              shape=shape,
                              strides=strides,
                              writeable=False)
    
    n_segments = data_strided.shape[0]
    out_timestamps = np.mean(as_strided(timestamps,
                                        shape=shape,
                                        strides=strides,
                                        writeable=False),
                                        axis=1)
    
    if np.isrealobj(data):
        M = nfft // 2 + 1

        xtd = pyfftw.zeros_aligned((n_tapers, n_segments, nfft), dtype='float64')
        xfd = pyfftw.zeros_aligned((n_tapers, n_segments, M), dtype='complex128')
        fft_sig = pyfftw.FFTW( xtd, xfd,
                               axes=(2, ),
                               direction='FFTW_FORWARD',
                               flags=['FFTW_ESTIMATE'],
                               threads=n_fft_threads,
                               planning_timelimit=0 )
        
        # (1, n_segments, nperseg) x (n_tapers, 1, nperseg)
        xtd[:, :, :N] = data_strided[None, :, :] * tapers[:, None, :]
        xtd[:, :, N:] = 0
        fft_sig(normalise_idft=True)
        #assert np.allclose(xfd, np.fft.rfft(data_strided[None, :, :] * tapers[:, None, :], n=nfft, axis=-1))
        #xfd = np.fft.rfft(tapers * data, n=nfft)
        
        spectrograms = (xfd.real**2 + xfd.imag**2) / fs
        
        if nfft % 2 == 0:
            spectrograms[:, :, 1:-1] *= 2
        else:
            spectrograms[:, :, 1:] *= 2

        freqs = np.fft.rfftfreq(nfft, d=1/fs)
    else:
        # can use an in-place transform here
        x = pyfftw.zeros_aligned((n_tapers, n_segments, nfft), dtype='complex128')
        fft_sig = pyfftw.FFTW( x, x,
                               axes=(2, ),
                               direction='FFTW_FORWARD',
                               flags=['FFTW_ESTIMATE'],
                               threads=n_fft_threads,
                               planning_timelimit=0 )
        
        # (1, n_segments, nperseg) x (n_tapers, 1, nperseg)
        x[:, :, :N] = data_strided[None, :, :] * tapers[:, None, :]
        x[:, :, N:] = 0
        fft_sig(normalise_idft=True)
        #assert np.allclose(xfd, np.fft.fft(data_strided[None, :, :] * tapers[:, None, :], n=nfft, axis=-1))

        spectrograms = (x.real**2 + x.imag**2) / fs      
        freqs = np.fft.fftfreq(nfft, d=1/fs)
    

    spectrogram = np.sum(lambdas[:, None, None] * spectrograms, axis=0) / np.sum(lambdas)
    assert np.all(np.isfinite(spectrogram))
    
    return spectrogram.T, freqs, out_timestamps