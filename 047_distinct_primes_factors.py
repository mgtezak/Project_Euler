'''Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?'''

from math import sqrt

def get_primes_in_range(upper):

    def is_prime(n):
        '''Doesnt check divisibility by 2, only works with the list comprehension underneath.'''
        for div in range(3, int(sqrt(n)) + 1, 2):
            if not n % div:
                return False
        return True

    return [2] + [num for num in range(3, upper, 2) if is_prime(num)]

primes = get_primes_in_range(1000)

def get_prime_factors(num):
    prime_factors = set()
    for p in primes:
        if num <= 1:
            return len(prime_factors)
        while not num % p:
            num //= p
            prime_factors.add(p)

def get_first_of_consecutive_nums():
    streak = 0
    for i in range(1_000_000):
        if get_prime_factors(i) != 4:
            streak = 0
            continue
        streak += 1
        if streak == 4:
            return i - 3

print(get_first_of_consecutive_nums())