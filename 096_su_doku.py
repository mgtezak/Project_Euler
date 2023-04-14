from collections import defaultdict as dict

with open('Project_Euler/puzzle_input/096.txt') as input:
    lines = input.read().split('\n')
    sudokus = [[[int(i) for i in lines[row]] for row in range(grid, grid + 9)] for grid in range(1, 500, 10)]

def solve_sudoku(grid):
    rows, cols, sqrs, empty = dict(set), dict(set), dict(set), []
    for r, row in enumerate(grid):
        for c, num in enumerate(row):
            s = r//3 * 3 + c//3
            if num == 0:
                empty.append((r, c, s))
            else:
                rows[r].add(num)
                cols[c].add(num)
                sqrs[s].add(num)

    def dfs(i):
        if i == n:
            return True
        r, c, s = empty[i]
        for num in set(range(1, 10)).difference(rows[r] | cols[c] | sqrs[s]):
            rows[r].add(num)
            cols[c].add(num)
            sqrs[s].add(num)
            if dfs(i+1):
                grid[r][c] = num
                return True
            rows[r].remove(num)
            cols[c].remove(num)
            sqrs[s].remove(num)
    
    n = len(empty)
    dfs(0)
    return 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]

print(sum(solve_sudoku(s) for s in sudokus))