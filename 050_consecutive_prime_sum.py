'''Which prime, below one-million, can be written as the sum of the most consecutive primes?'''

from math import sqrt

def is_prime(n): # this function only works in combination with the list comprehension underneath because it doesnt check divisibility by 2
    for div in range(3, int(sqrt(n)) + 1, 2):
        if not n % div:
            return False
    return True

primes = [2] + [num for num in range(3, 1_000_000, 2) if is_prime(num)]

def get_longest_prime_sum(limit=1_000_000):
    window = 1 
    for i in range(len(primes)):
        current_sum = sum(primes[i:i+window])

        for j in range(i+window, len(primes)):
            current_sum += primes[j]
            if current_sum > limit:
                if j-i == window:
                    return prime_sum
                break

            if current_sum in primes and j - i > window:
                window = j - i 
                prime_sum = current_sum

print(get_longest_prime_sum())