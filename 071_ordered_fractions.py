'''By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.'''

limit = 3/7
closest_val = 0
numerator = 0
for d in range(999_000, 1_000_000):
    left = d // 3
    right = d // 2
    while left <= right:
        n = (left + right) // 2
        if n / d >= limit:
            right = n - 1
        else:
            left = n + 1
    if right / d > closest_val:
        closest_val = right / d
        numerator = right

print(numerator)