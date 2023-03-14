'''Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.'''

from math import sqrt
from collections import defaultdict

def get_primes_in_range(r):
    primes = [3]
    for n in range(5, r+1, 2):
        sqrt_n = sqrt(n)
        for p in primes:
            if not n % p:
                break
            if p > sqrt_n:
                primes.append(n)
                break
    return primes

def is_prime(n):
    '''only works for nums >= 3'''
    for div in range(3, int(sqrt(n)) + 1, 2):
        if not n % div:
            return False
    return True

def dfs(current_primes, current_sum, remaining_candidates):
    if len(current_primes) == 5:
        sums.append(current_sum)
        return
    if not remaining_candidates:
        return
    for c in remaining_candidates:
        dfs(current_primes + [c], current_sum + c, remaining_candidates & d[c])

primes = get_primes_in_range(10_000)
d = defaultdict(set)
for i, p1 in enumerate(primes):
    for p2 in primes[i+1:]:
        if is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1))):
            d[p1].add(p2)

sums = []
for p in primes:
    dfs([p], p, d[p])

print(min(sums))