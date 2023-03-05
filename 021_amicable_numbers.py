'''Evaluate the sum of all the amicable numbers under 10000.'''

from math import sqrt

def get_div_sum(n):
    '''produces numbers less than n which divide evenly into n'''
    if n < 2:
        return 0
    div_sum = 1
    root = sqrt(n)
    for d in range(2, int(root)+1):
        if not n % d:
            div_sum += d + n//d if root != int(root) else d
    return div_sum

amicable = set()
for num in range(10_000):
    if num in amicable:
        continue
    div_sum = get_div_sum(num)
    if div_sum != num and get_div_sum(div_sum) == num:
        amicable.add(num)
        amicable.add(div_sum)

print(sum(amicable))    