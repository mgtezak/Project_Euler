'''There exists exactly one Pythagorean triplet with a < b < c 
for which a + b + c = 1000. Find the product abc.'''

def find_product_of_triplet():
    for a in range(1, 400):
        for b in range(a+1, 400):
            c = 1000 - a - b
            if c <= b:
                break
            if a**2 + b**2 > c**2:
                break
            if a**2 + b**2 == c**2:
                return a * b * c
                
print(find_product_of_triplet())