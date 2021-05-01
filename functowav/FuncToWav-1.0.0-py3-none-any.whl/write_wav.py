import struct, os
from _io import BufferedWriter
from os.path import isfile
from typing import Callable

class WriteWav:
    duration: int
    fileName: str
    sampleRate: int
    numChannels: int
    bps: int

    def __init__(self, duration: float, fileName: str = 'output', sampleRate: int = 48000, bps: int = 16, numChannels: int = 1):
        self.sampleRate = sampleRate
        self.numChannels = numChannels
        self.bps = bps
        self.fileName = "./" + fileName + ".wav"
        self.duration = duration

    def createFile(self):
        if isfile(self.fileName):
            os.remove(self.fileName)
        
        try:
            with open(self.fileName, 'xb') as file:
                self.writeHeader(file)
        except Exception as e:
            print(e)
            os.remove(self.fileName)
            raise Exception(e)

    def writeHeader(self, file: BufferedWriter):
        file.write(b"RIFF")
        fileSize = (self.sampleRate * self.duration * self.numChannels * self.bps//8) + 36
        file.write(fileSize.to_bytes(4, 'little'))
        file.write(b"WAVE")
        file.write(b"fmt ")
        file.write((16).to_bytes(4, 'little')) # chunk 1 size
        file.write((1).to_bytes(2, 'little')) # audio format
        file.write((1).to_bytes(2, 'little')) # number of channels
        file.write(self.sampleRate.to_bytes(4, 'little')) # sample rate
        byteRate = self.sampleRate * self.numChannels * self.bps // 8
        file.write(byteRate.to_bytes(4, 'little')) # byte rate
        file.write((self.numChannels * self.bps // 8).to_bytes(2, 'little')) # block align
        file.write(self.bps.to_bytes(2, 'little')) # bits per sample

    def appendData(self, song: Callable[[float], float]):
        assert isfile(self.fileName)
        try:
            with open(self.fileName, 'ab+') as file:
                file.write(b"data")
                file.write((self.sampleRate * self.duration * self.numChannels * self.bps//8).to_bytes(4, 'little'))
                t = 0
                step = 1/self.sampleRate
                while t <= self.duration:
                    file.write(struct.pack('<f', song(t)*(2**(self.bps-1))))
                    t += step
        except Exception as e:
            print(e)
            os.remove(self.fileName)
            raise Exception(e)
        
