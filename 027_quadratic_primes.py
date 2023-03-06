'''Find the product of the coefficients a and b for the quadratic expression that produces 
the maximum number of primes for consecutive values of n starting with n = 0.'''

from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or not n % 2:
        return False
    for div in range(3, int(sqrt(n)) + 1, 2):
        if not n % div:
            return False
    return True

primes = [n for n in range(10_000) if is_prime(n)]

def count_primes(a, b, n=0):
    '''counts the number of primes produced by the quadratic formula when using the coefficients a and b'''
    while True:
        if (result := n**2 + a*n + b) < 2 or result not in primes:
            return n - 1
        n += 1
    
max_result = 0
product = 0
for a in range(-1000, 1000):
    for b in range(1001):
        n_primes = count_primes(a, b)
        if n_primes <= max_result:
            continue
        max_result = n_primes
        product = a * b

print(product)