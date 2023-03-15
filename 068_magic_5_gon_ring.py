'''Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?'''

'''
idx 0 to 4 are the nodes of the outside ring, starting at the top-left going clockwise
idx 5 to 9 are the nodes of the inside ring, starting at the top going clockwise
therefore the 5 lines have the following indices:
1:  0, 5, 6
2:  1, 6, 7
3:  2, 7, 8
4:  3, 8, 9
5:  4, 9, 5
'''

from itertools import permutations

solutions = []
def fill_lines(nums, idx, line_sum, candidates):
    if idx == 4:
        remaining = candidates.pop()
        if remaining < nums[0] or sum((remaining, nums[9], nums[5])) != line_sum:
            return
        nums[4] = remaining
        solutions.append(nums)
        return
    for a, b in permutations(candidates, 2):
        if (idx and a < nums[0]) or b == 10:
            continue
        if idx == 0:
            line_sum = sum((a, b, nums[idx+5]))
        elif sum((a, b, nums[idx+5])) != line_sum:
            continue
        nums[idx] = a
        nums[idx+6] = b
        fill_lines(nums[:], idx+1, line_sum, candidates-{a, b})

candidates = set(n for n in range(1, 11))
for n in range(1, 10):
    fill_lines([0, 0, 0, 0, 0, n, 0, 0, 0, 0], 0, None, candidates-{n})

def format_solutions(s):
    return int(''.join((str(s[i]) for i in (0, 5, 6, 1, 6, 7, 2, 7, 8, 3, 8, 9, 4, 9, 5))))

print(max(format_solutions(s) for s in solutions))