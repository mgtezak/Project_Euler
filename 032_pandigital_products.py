'''Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.'''

from itertools import permutations
from math import sqrt

def get_factor_pair(num):
    for div in range(2,int(sqrt(num))+1):
        if num % div == 0 and div != sqrt(num):
            yield div, num // div

digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
candidates = permutations(digits, 4)
pandigital_products = []
for product in candidates:
    product_digits = ''.join(product)
    product = int(product_digits)
    for f1, f2 in get_factor_pair(product):
        digits_used = product_digits + str(f1) + str(f2)
        if len(digits_used) != 9 or len(set(digits_used)) != 9 or '0' in digits_used:
            continue
        pandigital_products.append(product)
        break

print(sum(pandigital_products))