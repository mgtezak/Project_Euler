'''Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.'''

from math import sqrt

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
    return [2] + primes

primes = get_primes_in_range(int(1.3 * sqrt(10_000_000)))
min_ratio = 2
solution = None

for i, p1 in enumerate(primes):
    for p2 in primes[:i]:
        n = p1 * p2
        phi = int(n * (1 - (1 / p1)) * (1 - (1 / p2)))
        totient_ratio = n / phi
        if n > 10_000_000 or totient_ratio >= min_ratio:
            continue
        if sorted(str(n)) == sorted(str(phi)):
            min_ratio = totient_ratio
            solution = n

print(solution)