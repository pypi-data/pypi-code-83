'''
Created on 24 févr. 2021

@author: fv
'''
from .base import BaseDBoard
from dboard.base import DBoardPreferedDapiMode

class GenericBoard(BaseDBoard):
    '''
    classdocs
    '''
    number = '00'

    def __init__(self, dapi, dmode=DBoardPreferedDapiMode.REGISTER):
        '''Constructor'''
        super().__init__(dapi, dmode)
        self.speed_range.set(0,40000)         