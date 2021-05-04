'''
Created on 24 févr. 2021

@author: fv
'''

from .base import DBoard
from dboard.base import DBoardPreferedDapiMode

class Board30(DBoard):
    '''Class for MB-30 Dassym's board.'''
    
    number = '30'

    def __init__(self, dapi, dmode=DBoardPreferedDapiMode.REGISTER):
        '''Constructor'''
        super().__init__(dapi, dmode)
        self.speed_range.set(1000,40000) 
        