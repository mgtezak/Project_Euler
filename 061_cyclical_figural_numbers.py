from math import sqrt

def is_triangular(x):
    n = (sqrt(1 + 8 * x) - 1) / 2
    return n == int(n), n

def is_square(x):
    n = sqrt(x)
    return n == int(n), n

def is_pentagonal(x):
    n = (1 + sqrt(1 + 24 * x)) / 6
    return n == int(n), n 

def is_hexagonal(x):
    n = (1 + sqrt(1 + 8 * x)) / 4
    return n == int(n), n

def is_heptagonal(x):
    n = (3 + sqrt(9 + 40 * x)) / 10
    return n == int(n), n

def is_octagonal(x):
    n = (2 + sqrt(4 + 12 * x)) / 6
    return n == int(n), n

funcs = set((is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal))
solution = []
def dfs(nums, current, funcs=funcs, indices=[]):
    if len(nums) == 6:
        if current == int(str(nums[0])[:2]):
            solution.append(nums)
        return
    for f in funcs:
        for n in range(current*100, (current+1)*100):
            if n % 100 < 10:
                continue
            is_polygonal, idx =  f(n)
            if is_polygonal and idx not in indices:
                dfs(nums+[n], n%100, funcs-{f}, indices+[idx])

for n in range(1_000, 10_000):
    valid, idx = is_triangular(n)
    if valid and n % 100 >= 10:
        dfs([n], n%100, funcs, [idx])

print(sum(solution.pop()))