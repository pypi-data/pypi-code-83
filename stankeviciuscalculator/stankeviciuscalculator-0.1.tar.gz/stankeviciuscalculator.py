'''
Calculator module. 

This module provides several math operations on float numbers.

Classes:

Calculator
'''

__version__ = '0.1'

from math import fsum

class Calculator():
    '''
    A clas to represent Calculator

    Methods
    -------
    add:
        Adds numbers.
    subtract:
        Subtracts numbers
    multiply:
        Multiple numbers
    division:
        Divides numbers
    n_root:
        Takes n root of number
    reset_memory:
        Resets calculator memory to 0
    '''
    
    def __init__(self, number: float=None) -> None:
        '''
        Constructs all the necessary attributes for the Calculator object.
        
        Parameters
        ----------
            number: float, optional. Default is None.        
        '''
        
        if number == None:
            self.memory = 0
        else:
            self.memory = number
        
    def add(self, number: float) -> float:
        '''
        Ads numbers, starting from 0 or from the one provided by the user
        while initiliazing Calculator ogject.

        Returns
        -------
        Result of addition in float
        '''
        
        self.memory = fsum((self.memory,number))
        return self.memory
    
    def subtract(self, number: float) -> float:
        '''
        Substracts numbers, starting from 0 or from the one provided by the user
        while initiliazing Calculator ogject.

        Returns
        -------
        Result of substraction in float
        '''
        
        self.memory -= number
        return self.memory
    
    def multiply(self, number: float) -> float:
        '''
        Multiple numbers, starting from 0 or from the one provided by the user
        while initiliazing Calculator ogject.

        Returns
        -------
        Result of multiplication in float
        '''
        
        self.memory *= number
        return self.memory
    
    def division(self, number: float) -> float:
        '''
        Divides numbers, starting from 0 or from the one provided by the user
        while initiliazing Calculator ogject.
       
        Raises
        ------
        ZeroDivisionError
            If 0 is passed is as parameter.

        Returns
        -------
        Result of division in float
        '''
        
        try:
            self.memory /= number
            return self.memory
        except ZeroDivisionError as e:
            raise e

    def n_root(self, number: float) -> float:
        '''
        Takes n root of numbers, starting from 0 or from the one provided by the user
        while initiliazing Calculator ogject.
       
        Raises
        ------
        ZeroDivisionError
            If 0 is passed is as parameter.

        Returns
        -------
        Result of n root in float
        '''
        
        try:
            self.memory = self.memory**(1./(number))
            return self.memory
        except ZeroDivisionError as e:
            raise e
    
    def reset_memory(self):
        '''
        Resets calculator memory to zero.

        Returns
        -------
        None.
        '''
        self.memory = 0