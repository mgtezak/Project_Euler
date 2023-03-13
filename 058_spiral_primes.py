'''what is the side length of the square spiral for which the ratio of primes along both 
diagonals first falls below 10%?'''

from math import sqrt

def is_prime(n):
    if not n % 2 or n == 1:
        return False
    for div in range(3, int(sqrt(n)) + 1, 2):
        if not n % div:
            return False
    return True

diag = []
edge_side = 1
current_val = 1
n_edges = 0
while True:
    current_val += edge_side
    diag.append(is_prime(current_val)) if n_edges % 4 else diag.append(is_prime(current_val-1))
    n_edges += 1
    if sum(diag)/len(diag) < 0.1 and current_val > 2:
        break
    if not n_edges % 2:
        edge_side += 1

print(edge_side)