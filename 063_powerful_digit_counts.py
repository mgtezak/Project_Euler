'''How many n-digit positive integers exist which are also an nth power?'''

count = 0
for x in range(1, 10):
    for n in range(1, 1000):
        n_digits = len(str(x**n))
        if n_digits == n:
            count += 1
        if n_digits > n:
            break

print(count)