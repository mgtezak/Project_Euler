'''determine which line number has the greatest numerical value'''


from math import log

path = 'Project_Euler/puzzle_input/099.txt'
with open(path) as file:
    lines = file.read().split('\n')

max_val = 0
max_idx = 0
for i, line in enumerate(lines, start=1):
    base, exponent = map(int, line.split(','))
    val = exponent * log(base)
    if val > max_val:
        max_val = val
        max_idx = i

print(max_idx)