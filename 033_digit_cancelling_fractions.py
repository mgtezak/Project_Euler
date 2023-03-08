'''If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.'''

import math

numerand = 1
denominator = 1
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if c == a:
                continue
            if int(str(a) + str(c)) / int(str(c) + str(b)) == a / b:
                numerand *= a
                denominator *= b

gcd = math.gcd(numerand, denominator)
print(denominator // gcd)