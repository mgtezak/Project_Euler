'''What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''

from math import sqrt

def is_composite(num):
    for div in range(3, int(sqrt(num)) + 1, 2):
        if not num % div:
            return True
    return False

def is_prime(num):
    for div in range(3, int(sqrt(num)) + 1, 2):
        if not num % div:
            return False
    return True

def check_conjecture(num):
    for prime in primes:
        if prime > num:
            return False
        for n in range(1000):
            result = prime + 2 * n**2
            if num == result:
                return True
            if result > num:
                break
    return False


composite_nums = [n for n in range(9, 10_000, 2) if is_composite(n)]
primes = [2] + [n for n in range(3, 10_000, 2) if is_prime(n)]

for num in composite_nums:
    if not check_conjecture(num):
        break

print(num)