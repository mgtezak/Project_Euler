'''What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?'''

path = 'Project_Euler/puzzle_input/011.txt'

with open(path) as file:
    grid = [[int(n) for n in line.split()] for line in file.read().split('\n')]

largest_product = 0

# check rows:
for line in grid:
    for i in range(17):
        prod = line[i] * line[i+1] * line[i+2] * line[i+3]
        largest_product = max(largest_product, prod)

# check columns:
for i in range(17):
    for j in range(20):
        prod = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
        largest_product = max(largest_product, prod)

# check descending diagonals:
for i in range(17):
    for j in range(17):
        prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        largest_product = max(largest_product, prod)

# check ascending diagonals:
for i in range(17):
    for j in range(3, 20):
        prod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
        largest_product = max(largest_product, prod)

print(largest_product)