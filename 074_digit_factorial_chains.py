'''How many chains of factorial sums, with a starting number below one million, contain exactly sixty non-repeating terms?'''

from math import factorial
from collections import Counter

chain_lengths = {169: 3, 363601: 3, 1454: 3, 169: 3, 871: 2, 45361: 2, 871: 2, 872: 2, 45362: 2, 872: 2, 145: 1}
factorials = {n: factorial(n) for n in range(10)}


def get_chain_length(n):
    if n in chain_lengths:
        return chain_lengths[n]
    
    factorial_sum = 0
    digits = n
    while digits:
        factorial_sum += factorials[digits % 10]
        digits //= 10

    if factorial_sum == n:
        chain_length = 1
    else:
        chain_length = 1 + get_chain_length(factorial_sum)

    chain_lengths[n] = chain_length
    return chain_length

for n in range(1, 1_000_000):
    get_chain_length(n)

print(Counter(chain_lengths.values())[60])