'''
PROBLEM: 
Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly 
one integer sided right angle triangle be formed?

APPROACH:
Conditions for integer-sided right triangle:
a < b < c
a^2 + b^2 = c^2
L = a + b + c
From Euclid's formular we derive that if m, n are two coprime numbers and of them is even, 
then a primitve Pythagorean triple can be generated as follows:
a = m^2 - n^2
b = 2 * m * n
c = m^2 + n^2
m > n > 0
In order to find non-primitive triples, we simply multiply every side with a factor k.
'''

from math import sqrt, gcd
from collections import defaultdict, Counter

wire_lengths = defaultdict(int)
limit = 1_500_000 
for m in range(2, int(sqrt(limit + 1))):
    for n in range(1, m):
        if gcd(m, n) > 1 or (m % 2 and n % 2):
            continue
        m_sq, n_sq = m**2, n**2
        a = m_sq - n_sq
        b = 2 * m * n
        c = m_sq + n_sq
        L = a + b + c
        if L > limit:
            break
        for k in range(1, limit // L + 1):
            wire_lengths[k * L] += 1

print(Counter(wire_lengths.values())[1])