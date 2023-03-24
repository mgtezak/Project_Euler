'''Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down.'''

from heapq import heappush, heappop

# # test data:
# matrix = [[131, 673, 234, 103,  18], 
#           [201,  96, 342, 965, 150], 
#           [630, 803, 746, 422, 111], 
#           [537, 699, 497, 121, 956], 
#           [805, 732, 524,  37, 331]]

path = 'Project_Euler/puzzle_input/081-083.txt'
with open(path) as file:
    matrix = [[int(n) for n in line.split(',')] for line in file.read().split('\n')]
    m = len(matrix)

visited = set()
priority_queue = [(0, 0, 0)]
while True:
    path_sum, row, col = heappop(priority_queue)
    if row < 0 or col < 0 or row == m or col == m or (row, col) in visited:
        continue

    visited.add((row, col))
    path_sum += matrix[row][col]
    if row == col == m - 1:
        break
    
    for nxt_row, nxt_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
        heappush(priority_queue, (path_sum, nxt_row, nxt_col))

print(path_sum)