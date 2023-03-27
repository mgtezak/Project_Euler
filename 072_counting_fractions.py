'''How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?'''

limit = 1_000_001
phis = list(range(2, limit))
l = len(phis)
for i, n in enumerate(phis):
    if i + 2 == n:
        for j in range(i, l, n):
            phis[j] *= (1 - 1/n)
            
print(int(sum(phis)))