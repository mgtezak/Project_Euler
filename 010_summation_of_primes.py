'''Find the sum of all the primes below two million.'''

from math import sqrt

def get_sum_of_primes_in_range(r):
    primes = [2]
    for num in range(3, r, 2):
        for p in primes:
            if not num % p:
                break
            if p > sqrt(num):
                primes.append(num)
                break
    return sum(primes)

print(get_sum_of_primes_in_range(2_000_000))