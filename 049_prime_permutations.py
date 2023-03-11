'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in 
two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of 
one another. There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this 
property, but there is one other 4-digit increasing sequence. What 12-digit number do you form by 
concatenating the three terms in this sequence?'''

from math import sqrt

def is_prime(n):
    if not n % 2:
        return False
    for div in range(3, int(sqrt(n)) + 1, 2):
        if not n % div:
            return False
    return True

for n in range(1_000, 10_000):
    if not is_prime(n):
        continue
    if sorted(str(n)) != sorted(str(n+3330)) or not is_prime(n+3330):
        continue
    if sorted(str(n)) != sorted(str(n+6660)) or not is_prime(n+6660):
        continue
    print(str(n) + str(n+3330) + str(n+6660))