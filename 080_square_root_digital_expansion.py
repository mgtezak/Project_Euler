'''For the first one hundred natural numbers, find the total of the digital sums 
of the first one hundred decimal digits for all the irrational square roots.'''

from decimal import Decimal, getcontext

getcontext().prec = 102

total = 0
for x in range(2, 100):
    if (root := Decimal(x).sqrt()) % 1:
        decimals = str(root).replace('.', '')
        total += sum(int(d)for d in decimals[:100])

print(total)