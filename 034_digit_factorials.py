'''Find the sum of all numbers which are equal to the sum of the factorial of their digits.'''

from math import factorial

print(sum(n for n in range(3, 100_000) if n == sum(factorial(int(d)) for d in str(n))))