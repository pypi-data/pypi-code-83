# Python lib
from random import choice

NUMBERS = ''.join([chr(i) for i in range(48, 58)])
UPPERCASE_LETTERS = ''.join([chr(i) for i in range(65, 91)])
LOWERCASE_LETTERS = ''.join([chr(i) for i in range(97, 123)])
MISC_LETTERS = '!#$%&^*?'
PASS_LIST = [NUMBERS, UPPERCASE_LETTERS, LOWERCASE_LETTERS, MISC_LETTERS]

def generate(length = 12) -> str:
    '''Generates random password'''
    valid = False

    while not valid:
        password = ''
        while len(password) <= length:
            choiced_letters = choice(PASS_LIST)
            password += choice(choiced_letters)
        valid = _validate_password(password)
    
    return password

def _validate_password(password) -> bool:
    '''
    Validate password have at least one number, uppercase letter,
    lowercase letter, misc letter
    '''
    number = False
    uppercase_letter = False
    lowercase_letter = False
    misc_letter = False

    for letter in password:
        if letter in NUMBERS:
            number = True
            continue
        if letter in UPPERCASE_LETTERS:
            uppercase_letter = True
            continue
        if letter in LOWERCASE_LETTERS:
            lowercase_letter = True
            continue
        if letter in MISC_LETTERS:
            misc_letter = True
            continue
    
    if number and uppercase_letter and lowercase_letter and misc_letter:
        return True
    return False