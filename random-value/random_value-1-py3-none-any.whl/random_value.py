import string import random 

def random_string(length, string):

    if type(length) == 'float':
        raise TypeError('The "length" argument must be an integer.')

    elif string == 1:
        _LENGTH = length

        string_pool = string.ascii_lowercase
        result = "" 
        for i in range(_LENGTH): 
            result += random.choice(string_pool) 
        
        return result

    elif string == 2:
        _LENGTH = length

        string_pool = string.ascii_uppercase
        result = "" 
        for i in range(_LENGTH): 
            result += random.choice(string_pool) 
        
        return result
    
    elif string == 3:
        _LENGTH = length

        string_pool = string.ascii_letters
        result = "" 
        for i in range(_LENGTH): 
            result += random.choice(string_pool) 
        
        return result
    
    else:
        raise WrongValue('The "string" argument must be one of 1, 2, ​3.')

def random_number(length):
    if type(length) == 'float':
        raise TypeError('The "length" argument must be an integer.')
    
    else:
        _LENGTH = int(length)
        string_pool = string.digits
        result = "" 
        for i in range(_LENGTH):
            result += random.choice(string_pool)
