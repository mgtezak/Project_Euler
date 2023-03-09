'''What is the largest n-digit pandigital prime that exists?'''

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

def is_pandigital(n):
    n = str(n)
    return all(str(d) in n for d in range(1, len(n)+1))


primes = [n for n in range(2_143, 10_000_000, 2) if is_prime(n)]

while primes:
    p = primes.pop()
    if is_pandigital(p):
        break

print(p)