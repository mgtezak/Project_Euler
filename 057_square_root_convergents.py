'''It is possible to show that the square root of two can be expressed as an infinite continued fraction.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?'''

from fractions import Fraction

current = Fraction(1, 2)
count = 0
for _ in range(1000):
    current = Fraction(1, 2 + current)
    if len(str(current.numerator + current.denominator)) > len(str(current.denominator)):
        count += 1

print(count)