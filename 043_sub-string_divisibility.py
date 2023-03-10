'''Find the sum of all 0 to 9 pandigital numbers with sub-string divisibility.'''

from itertools import permutations

divisors = (2, 3, 5, 7, 11, 13, 17)

def is_substring_divisible(num):
    num = ''.join(str(d) for d in num)
    for i in range(7):
        if int(num[i+1: i+4]) % divisors[i]:
            return False
    return True

print(sum(int(''.join(str(d) for d in n)) for n in permutations(range(10)) if is_substring_divisible(n)))