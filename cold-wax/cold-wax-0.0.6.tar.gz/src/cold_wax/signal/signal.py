from os import path
import numpy as np
import soundfile as sf
from scipy import signal as scipy_signal


def read_signal(audio_file):
    signal, samplerate = sf.read(audio_file)
    return signal, samplerate


def write_signal(signal, audio_file_with_extension, samplerate, overwrite=False):
    if path.exists(audio_file_with_extension) and not overwrite:
        return False
    sf.write(audio_file_with_extension, signal, samplerate)
    return True


def normalise(signal):
    return signal / np.abs(np.max(signal))


def stereo_to_mono(signal):
    assert signal.shape[1] == 2
    return normalise(signal[:, 0] + signal[:, 1])


def convolve_ir_to_signal(signal, signal_samplerate, ir, ir_samplerate, out_samplerate):
    if not any([isinstance(signal, np.array), isinstance(signal, str)]):
        raise TypeError('Signal must be either an np.array or a path to an \
                        audio file')
    if not any([isinstance(ir, np.array), isinstance(ir, str)]):
        raise TypeError('Ir must be either an np.array or a path to an \
                        audio file')
    f = signal.copy()
    g = ir.copy()
    if f.shape[1] > 1:
        f = stereo_to_mono(f)
    if g.shape[1] > 1:
        g = stereo_to_mono(g)

    t = np.max(f.shape) / ir_samplerate
    f = scipy_signal.resample(f, int(np.floor(t * out_samplerate)))
    f = normalise(f)
    t = np.max(g.shape) / signal_samplerate
    g = scipy_signal.resample(g, int(np.floor(t * out_samplerate)))
    g = normalise(g)
    y = np.convolve(g, f, 'full')
    y = normalise(y)
    return y

