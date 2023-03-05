'''Find the sum of the digits in the number 100!'''

from math import factorial

print(sum(int(d) for d in str(factorial(100))))