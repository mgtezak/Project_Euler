'''Find the smallest cube for which exactly five permutations of its digits are cube.'''

from collections import defaultdict

cube_perms = defaultdict(list)
for cube in (i**3 for i in range(10000)):
    sorted_digits = ''.join(sorted(str(cube)))
    cube_perms[sorted_digits].append(cube)
    if len(cube_perms[sorted_digits]) == 5:
        break

print(min(cube_perms[sorted_digits]))