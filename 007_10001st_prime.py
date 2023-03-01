'''What is the 10001st prime number?'''

from math import sqrt

def get_nth_prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        for p in primes:
            if not num % p:
                break
            if p > sqrt(num):
                primes.append(num)
                break
        num += 2
    return primes.pop()

print(get_nth_prime(10001))