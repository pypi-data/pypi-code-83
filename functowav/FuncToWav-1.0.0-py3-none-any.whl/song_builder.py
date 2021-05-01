import numpy
from extended_int import int_inf
from functools import reduce
from FuncToWav import constants as c
from math import sin, pi
from FuncToWav.helper import heaviside, combineFuncs
from typing import Callable

class SongBuilder:
    length: int
    notes: []

    def __init__(self):
        self.length = 0
        self.notes = []
    
    def numToFreq(self, x: int):
        return round((2**((x-49)/12)*440),3)

    def _keyToNum(self, scale: str, octave: str) -> int:
        if scale.lower() not in c.KEY_TO_NUM:
            raise ValueError("The letter code is not one of the scale")
        
        num = int(octave)*12+c.KEY_TO_NUM[scale.lower()]-8

        if num < 1 or num > 88:
            raise ValueError("Unsupported tone")

        return num

    def keyToNum(self, key: str) -> int:
        if len(key) == 3:
            scale = key[:2]
            octave = key[2]
        elif len(key) == 2:
            scale = key[0]
            octave = key[1]
        elif len(key) == 1:
            scale = key
            octave = 4
        else:
            raise ValueError("It's not possible to convert the input to key number")

        return self._keyToNum(scale, octave)

    def appendToSong(self, key: str, startTime: int, duration: int = None, endTime: int = int_inf):
        if (duration == None) and (endTime == int_inf):
            endTime = self.length
        elif (duration == None) and (endTime != int_inf):
            endTime = endTime
        elif (duration != None) and (endTime == int_inf):
            endTime = startTime+duration
        else:
            raise ValueError("Either duration is specified or endTime is specified. Not Both.")

        self.length = self.length if self.length >= endTime else endTime
        part = {
            c.FREQUENCY: self.numToFreq(self.keyToNum(key)),
            c.START_TIME: startTime,
            c.END_TIME: endTime
        }

        self.notes.append(part)

    def freqToFunc(self, part: dict) -> Callable[[float], float]:
        freq = part[c.FREQUENCY]
        sTime = part[c.START_TIME]
        eTime = part[c.END_TIME]
        return lambda x: sin(2*pi*freq * x) * heaviside(x, sTime=sTime, eTime=eTime)

    def buildSong(self) -> Callable[[float], float]:
        funcs = list(map(self.freqToFunc, self.notes))
        return reduce(combineFuncs, funcs)
