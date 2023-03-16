'''Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.'''

from math import sqrt

def generate_primes():
    yield 2
    n = 3
    while True:
        for div in range(3, int(sqrt(n)) + 1):
            if not n % div:
                break
        else:
            yield n
        n += 2

current = 1
for p in generate_primes():
    if current * p > 1_000_000:
        break
    current *= p

print(current)
