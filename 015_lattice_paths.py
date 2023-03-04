'''How many routes are there from the top left to the bottom right corner of a 20×20 grid?'''

memo = {}
def count_routes(a, b):
    if not a:
        return 1
    if (a, b) in memo:
        return memo[(a, b)] 

    tup_1 = tuple(sorted([a-1, b]))
    tup_2 = tuple(sorted([a, b-1]))
    memo[tup_1] = count_routes(*tup_1)
    memo[tup_2] = count_routes(*tup_2)
    return memo[tup_1] + memo[tup_2]

print(count_routes(20, 20))