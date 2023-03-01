'''What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

from collections import defaultdict

all_prime_factors = defaultdict(int)

for n in range(4, 21):
    prime_factors = defaultdict(int)
    i = 2
    while i <= n:
        if n % i == 0:
            prime_factors[i] += 1
            n //= i
        else:
            i += 1
    for i, count in prime_factors.items():
        all_prime_factors[i] = max(count, all_prime_factors[i])

solution = 1
for i, count in all_prime_factors.items():
    solution *= i ** count

print(solution)