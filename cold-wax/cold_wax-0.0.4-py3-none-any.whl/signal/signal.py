import numpy as np
import soundfile as sf
from scipy import signal as scipy_signal



def read_signal(audio_file):
    signal, samplerate = sf.read(audio_file)
    return signal, samplerate

def normalise(signal):
    return signal / np.abs(np.max(signal))


def stereo_to_mono(signal):
	return normalise(signal[:, 0] + signal[:, 1])


def convolve_ir_to_signal(signal, ir, samplerate):
    if not any([isinstance(signal, np.array), isinstance(signal, str)]):
        raise TypeError('Signal must be either an np.array or a path to an \
                        audio file')
    if not any([isinstance(ir, np.array), isinstance(ir, str)]):
        raise TypeError('Ir must be either an np.array or a path to an \
                        audio file')
    
