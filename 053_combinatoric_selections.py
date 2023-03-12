'''How many, not necessarily distinct, values of "n choose r" for 1 <= n <= 100 are greater than one-million?'''

from math import factorial as f

def count_results_above_(threshold):
    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            if f(n) / (f(r) * (f(n-r))) > threshold:
                count += 1
    return count

print(count_results_above_(1_000_000))

### ONE LINER:

print(sum(1 for n in range(1, 101) for r in range(1, n+1) if f(n) / (f(r) * f(n-r)) > 1000000))