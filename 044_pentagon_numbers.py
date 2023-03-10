'''Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference 
are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?'''

'''
formula for pentas:
x = n * (3 * n - 1) / 2     
if n is not a positive integer then x is not a penta.

solve for n:
2x = 3n^2 - n
0 = 3n^2 - n - 2x
0 = n^2 - n / 3 - 2x / 3 

p,q-formula:
n = - p/2 + sqrt((p/2)^2 - q)      

insert values p = -1/3 and q = -2/3:
n = 1 / 6 + sqrt(1 / 36 + 2x / 3)
n = 1 / 6 + sqrt(1 / 36 + 24x / 36)
n = 1 / 6 + sqrt((1 + 24x) / 36)
n = 1 / 6 + sqrt(1 + 24x) / 6
n = (1 + sqrt(1 + 24x)) / 6
'''
from math import sqrt

def check_if_pentagonal(num):
    n = (1 + sqrt(1 + 24 * num)) / 6
    return n == int(n)

penta_nums = [int(n * (3 * n - 1) / 2) for n in range(1, 5_000)]

def get_lowest_diff():
    for x in penta_nums:
        for y in penta_nums:
            if check_if_pentagonal(x+y) and check_if_pentagonal(x+2*y):
                return x

print(get_lowest_diff())