'''By starting at the top of the triangle and moving to adjacent numbers on the row below,
find the maximum sum from top to bottom'''

from collections import defaultdict

path = 'Project_Euler/puzzle_input/067.txt'
with open(path) as file:
    triangle = [[int(n) for n in line.split()] for line in file.read().split('\n')]

memo = defaultdict(int)
def solve_bottom_up(idx, line):
    max_sum = max(memo[(line+1, idx)], memo[(line+1, idx+1)]) + triangle[line][idx]
    memo[(line, idx)] = max(max_sum, memo[(line, idx)])

for line in range(99, -1, -1):
    for idx in range(line + 1):
        solve_bottom_up(idx, line)

print(memo[(0, 0)])