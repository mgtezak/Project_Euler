'''Find the largest palindrome made from the product of two 3-digit numbers.'''

largest_product = 0
for a in range(999, 99, -1):
    if a**2 < largest_product:
        break
    for b in range(a, 99, -1):
        if (prod := a*b) < largest_product:
            break
        if str(prod) == str(prod)[::-1]:
            largest_product = prod
            break

print(largest_product)