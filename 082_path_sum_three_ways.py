'''Find the minimal path sum from the top left to the bottom right by only moving right and down'''

# # test data:
# matrix = [[131, 673, 234, 103,  18], 
#           [201,  96, 342, 965, 150], 
#           [630, 803, 746, 422, 111], 
#           [537, 699, 497, 121, 956], 
#           [805, 732, 524,  37, 331]]

path = 'Project_Euler/puzzle_input/081-082.txt'
with open(path) as file:
    matrix = [[int(n) for n in line.split(',')] for line in file.read().split('\n')]

m = len(matrix)
sum_path = {(row, 0): matrix[row][0] for row in range(m)}

def get_min_neighbor(row, col):
    up   = sum_path.get((row - 1, col), float('inf'))
    down = sum_path.get((row + 1, col), float('inf'))
    left = sum_path[(row, col - 1)]
    return min(up, down, left)

for col in range(1, m):
    # fill in column: top to bottom
    for row in range(m):
        sum_path[(row, col)] = matrix[row][col] + get_min_neighbor(row, col)
    # fill in column: bottom to top
    for row in range(m-1, -1, -1):
        sum_path[(row, col)] = matrix[row][col] + get_min_neighbor(row, col)

print(min(sum_path[(row, m - 1)] for row in range(m)))