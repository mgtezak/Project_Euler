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

sum_path = {(0, 0): matrix[0][0]}
def get_sum_path(i, j):
    if i < 0 or j < 0:
        return float('inf')
    
    if (i, j) in sum_path:
        return sum_path[(i, j)]
    
    up = get_sum_path(i-1, j)
    left = get_sum_path(i, j-1)
    min_sum_path = matrix[i][j] + min(up, left)
    sum_path[(i, j)] = min_sum_path
    return min_sum_path

print(get_sum_path(m-1, m-1))