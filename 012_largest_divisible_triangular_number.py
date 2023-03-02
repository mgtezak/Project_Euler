'''What is the value of the first triangle number to have over five hundred divisors?'''

import math

def generate_triangle_nums():
    num = 0
    add = 0
    while True:
        add += 1
        num += add
        yield num

def count_divisors(num):
    '''function works for all values from 5 upwards'''
    divisor_count = 2   # 1 and self already accounted for
    sqrt = math.sqrt(num)
    for n in range(2, int(sqrt)+1):
        if not num % n:
            divisor_count += 2
    if sqrt == int(sqrt):
        divisor_count -= 1
    return divisor_count

for num in generate_triangle_nums():
    if count_divisors(num) > 500:
        break

print(num)