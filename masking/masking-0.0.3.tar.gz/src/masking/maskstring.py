import sys
class indexError(Exception):
    '''
    This class is used to raise custom exception when user supplies index values that are not available for the string. 
    '''
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)

class maskError(Exception):
    '''
    This class is used to raise custom exception when main string is equal to substring used for masking.
    '''
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)
def maskstring(strng,substr,*args):
    '''
    This function is used to mask a given input string based on the index positions passed as arguments.
    This function will replace other characters from the main string with a substring where index positions in the main string is not present in the list of arguments(index position) supplied to the function.
    :param strng: This is the main string that you want to mask
    :param substr: This is the substring that you want mask with in the main string
    :param args: Array of index positions where you don't want masking to happen. Viewer will be able to view the masked string with only those characters that are available in these index positions.
    :return: return the masked string e.g.******3.9.2 where string 'Python' has been masked with '*'
    '''
    try:
        if strng == substr:
            raise maskError('Masking cannot be done with the same string in the main string')
        for indx in args:
            if indx > (len(strng) - 1):
                raise indexError(f'Index {indx} supplied in the argument is not available in the main string.\nSolution:Kindly, supply arguments(index positions) available for the string.')
    except indexError as ex:
        print(f'''  File "{sys.argv[0]}"''')
        print(f'indexError:{ex}')
    except maskError as ex:
        print(f'''  File "{sys.argv[0]}"''')
        print(f'maskError:{ex}')
    else:
        mskstr = ''
        for tup in enumerate(strng):
            idx, ch = tup
            if idx in args:  # Checking if the index position is available in the list of arguments(index positions) that were supplied. If it is available it will not mask.
                mskstr += ch
            else:  # If the index position is not available in the list of arguments(index positions) that were supplied it will mask.
                mskstr += substr
        return mskstr
