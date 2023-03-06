'''Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''

from math import sqrt

def is_abundant(n: int) -> int:
    '''checks if sum of proper divisors of n is greater than itself'''
    if n < 12:
        return False
    div_sum = 1
    root = sqrt(n)
    for div in range(2, int(root)+1):
        if not n % div:
            div_sum += div + n//div if div != root else div
        if div_sum > n:
            return True
    return False

abundant_nums = [n for n in range(28123) if is_abundant(n)]
abundant_sum = sum(set(n1 + n2 for i, n1 in enumerate(abundant_nums) for n2 in abundant_nums[i:] if n1 + n2 < 28123))
non_abundant_sum = sum(range(28123)) - abundant_sum
print(non_abundant_sum)