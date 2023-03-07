'''How many different ways can £2 be made using any number of coins?'''

coins = [1, 2, 5, 10, 20, 50, 100, 200][::-1] # way more efficient when reversed
target = 200

def solve_recursively():

    def dfs(i=0, total=0):
        if total > target or i > 7:
            return
        if total == target:
            solutions.append(1)
            return
        dfs(i, total+coins[i])
        dfs(i+1, total)

    solutions = []
    dfs()
    return len(solutions)


def solve_iteratively():
    solutions = []
    queue = [(0, 0)]

    while queue:
        i, total = queue.pop()
        if total > target or i > 7:
            continue
        if total == target:
            solutions.append(1)
            continue
        queue.append((i, total+coins[i]))
        queue.append((i+1, total))

    return len(solutions)

print(solve_recursively())
print(solve_iteratively())