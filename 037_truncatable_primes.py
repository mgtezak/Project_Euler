'''Find the sum of the only eleven primes that are both truncatable from left to right and right to left.'''

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


def truncate(num):
    left = right = str(num)
    while len(left) > 1:
        left = left[1:]
        yield int(left)
    while len(right) > 1:
        right = right[:-1]
        yield int(right)

primes = [n for n in range(11, 1_000_000, 2) if is_prime(n)]
truncatable = [p for p in primes if all(is_prime(t) for t in truncate(p))]

print(sum(truncatable))