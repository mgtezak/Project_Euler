'''How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?'''

from math import gcd

total = 0

for d in range(4, 12001):
    left = d // 3 + 1
    right = d // 2 + 1 if d % 2 else d // 2
    for n in range(left, right):
        if gcd(n, d) == 1:
            total += 1

print(total)