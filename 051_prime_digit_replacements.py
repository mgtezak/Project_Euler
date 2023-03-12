'''Find the smallest prime which, by replacing part of the number (not necessarily 
adjacent digits) with the same digit, is part of an eight prime value family.'''

from math import sqrt
from itertools import combinations

def get_primes_in_range(r=1_000_000):
    primes = [3]
    for n in range(5, r+1, 2):
        sqrt_n = sqrt(n)
        for p in primes:
            if not n % p:
                break
            if p > sqrt_n:
                primes.append(n)
                break
    return [2] + primes

def is_prime(n):
    left = 0
    right = len(primes) - 1
    while left <= right:
        i = (left + right) // 2
        p = primes[i]
        if n < p:
            right = i - 1
        if n > p:
            left = i + 1
        if n == p:
            return True
    return False

def generate_prime_families(original_n, family_size):
    n = original_n.copy()
    digit_to_switch = 0
    while digit_to_switch <= 10 - family_size:
        digit_indices = [i for i, digit in enumerate(n) if digit == str(digit_to_switch)]
        index_combinations = [c for r in range(1, len(digit_indices)+1) for c in combinations(digit_indices, r)]
        for indices in index_combinations:
            primes = []
            for d in range(10):
                for i in indices:
                    n[i] = str(d)
                result = int(''.join(n))
                if n[0] != '0' and is_prime(result):
                    primes.append(result)
            yield primes
            n = original_n.copy()
        digit_to_switch += 1
    
def get_lowest_prime_for_n_family_size(n):
    for prime in primes:
        digits = list(str(prime))
        for prime_family in generate_prime_families(digits[:], family_size=n):
            if len(prime_family) == n:
                return prime_family[0]

primes = get_primes_in_range()
print(get_lowest_prime_for_n_family_size(8))
