'''A module to finds all kinds of primes.'''
from time import time
from math import log

NUMPY_ENABLED = True
try:
    from numpy import ones, nonzero, __version__
    print(f'Detected numpy version {__version__}')
except ImportError:
    NUMPY_ENABLED = False

__version__ = 1.0

def _check_num(n):
    if not isinstance(n, int):
        raise TypeError(f'Type of argument n should be int, got {type(n).__name__}')

    if n < 0:
        raise ValueError(f'The number of argument n should be greater than 0, got {n}')

def is_prime(n):
    '''
    If n is prime, return True.
    '''
    _check_num(n)
    if n in [2, 3, 5, 7]:
        return True

    if not (n % 10 % 2) or n % 10 not in [1, 3, 7, 9] or n == 1 or not isinstance(n, int):
        return False

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True

def all_primes(n, output = 'array'):
    '''
    Return a prime list below n.

    Arguments:
    output ----- 'array' or 'list' ----- The output type of the function.
    '''
    _check_num(n)
    if NUMPY_ENABLED:
        sieve = ones(n + 1, dtype = bool)
    else:
        sieve = [True] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    if NUMPY_ENABLED:
        s = nonzero(sieve)[0]
        if output == 'list':
            return s.tolist()[2:]

        return s[2:]

    else:
        return [x for x in range(2, n + 1) if sieve[x]]

def find_twins(n):
    '''
    Return a dict that has all twin primes below n.
    '''
    _check_num(n)
    primes = all_primes(n)
    twin_primes = {}
    for ix, xp in enumerate(primes):
        if ix == len(primes) - 1:
            break

        if primes[ix + 1] - xp == 2:
            twin_primes[xp] = primes[ix + 1]

    return twin_primes

def find_palindromes(n):
    '''
    Return a list that has all palindromes primes below n.
    '''
    _check_num(n)
    primes = all_primes(n)
    palin_primes = []
    for ix, xp in enumerate(primes):
        palin_num = int(str(xp)[::-1])
        if is_prime(palin_num) and palin_num == xp and xp > 10:
            palin_primes.append(palin_num)

    return palin_primes

def find_reverse(n):
    '''
    Return a dict that has all reverse primes below n.
    '''
    _check_num(n)
    primes = all_primes(n)
    reverse_primes = {}
    for ix, xp in enumerate(primes):
        reverse_num = int(str(xp)[::-1])
        if is_prime(reverse_num) and xp > 10:
            reverse_primes[xp] = reverse_num

    palin_primes = find_palindromes(n)
    for x in palin_primes:
        if reverse_primes.get(x):
            reverse_primes.pop(x)

    return reverse_primes

def find_square_palindromes(n):
    '''
    Return a dict that has all square palindrome primes below n.
    '''
    _check_num(n)
    palin_primes = find_palindromes(n)
    square_palin_prime = {}
    for x in palin_primes:
        if str(x ** 2)[::-1] == str(x ** 2):
            square_palin_prime[x] = x ** 2

    return square_palin_prime

def find_arithmetic_prime_progressions(n):
    '''
    Return a list that has all arithmetic prime progression below n.
    '''
    _check_num(n)
    primes = all_primes(n)
    time = 0
    arithmetic_prime_list = []
    for i, xp in enumerate(primes):
        for j in range(i + 1, len(primes)):
            a0, a1 = primes[i], primes[j]
            an = a1 + a1 - a0
            k = []
            while an < n and an in primes:
                k.append(an)
                an += a1 - a0

            if len([a0, a1] + k) >= 3:
                if k and not time:
                    arithmetic_prime_list = [[a0, a1] + k]

                if time:
                    arithmetic_prime_list += [[a0, a1] + k]
                time += 1

    return arithmetic_prime_list

def find_mersenne_primes(n):
    '''
    Return a list that has all mersenne primes below n.
    '''
    _check_num(n)
    primes = set(all_primes(n))
    result = []
    for i in range(2, int(log(n + 1, 2)) + 1):
        result.append(2 ** i - 1)

    mersenne_primes = primes.intersection(result)
    return sorted(mersenne_primes)

def find_fermat_pseudoprime(n):
    '''
    Return a list that has all fermat pseudoprimes below n.
    '''
    _check_num(n)
    primes = all_primes(n)
    a = 2
    fermat_pseudoprimes = []
    composites = [x for x in range(3, n + 1, a) if x not in primes]
    for x in composites:
        if (a ** (x - 1) - 1) % x == 0:
            fermat_pseudoprimes.append(x)

    return fermat_pseudoprimes

def main():
    '''A test of this module.'''
    start_tm = time()
    print(f'Twin primes: {find_twins(4750)}\n')
    print(f'Palindome primes: {find_palindromes(20000)}\n')
    print(f'Reverse primes: {find_reverse(3000)}\n')
    print(f'Square palindome primes: {find_square_palindromes(500)}\n')
    print(f'Arithmetic prime progressions: {find_arithmetic_prime_progressions(125)}\n')
    print(f'Mersenne Primes: {find_mersenne_primes(525000)}\n')
    print(f'Fermat Pseudoprime: {find_fermat_pseudoprime(1000)}')
    end_tm = time()
    print(f'Time: {round(end_tm - start_tm, 12)} seconds.')

if __name__ == '__main__':
    main()
