'''How many circular primes are there below one million?'''

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

def generate_rotations(num):
    num = str(num)
    for _ in range(len(num)-1):
        num = num[1:]+num[0]
        yield int(num)

primes = [n for n in range(1_000_000) if is_prime(n)]
circular_primes = [p for p in primes if all(r in primes for r in generate_rotations(p))]

print(len(circular_primes))