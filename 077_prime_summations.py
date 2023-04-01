'''What is the first value which can be written as the sum of primes in over five thousand different ways?'''

def get_primes_in_range_(r):
    primes = [3]
    for i in range(5, r + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    return [2] + primes


def count_n_ways_to_sum_primes(target):
    n_combinations = [1] + [0] * target
    for p in primes:
        for i in range(len(n_combinations) - p):
            n_combinations[i + p] += n_combinations[i]
    return n_combinations[-1]


upper = 100
primes = get_primes_in_range_(upper)
for i in range(upper):
    if count_n_ways_to_sum_primes(i) > 5000:
        break

print(i)