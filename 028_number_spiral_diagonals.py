'''What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed by 
starting with the number 1 and moving to the right in a clockwise direction?'''

from itertools import cycle

def get_diagonals(size=1001):
    current_val = 1
    edge_len = 1
    n_edges = 0
    diagonals = []
    while True:
        current_val += edge_len
        diagonals.append(current_val) if n_edges % 4 else diagonals.append(current_val-1)
        if edge_len == size:
            return sum(diagonals)
        edge_len = edge_len + 1 if n_edges % 2 else edge_len
        n_edges += 1

print(get_diagonals())