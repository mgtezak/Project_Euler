'''A number chain is created by continuously adding the square of the digits in a number 
to form a new number until it has been seen before.'''

memo = {1: False, 89: True}
def arrives_at_89(num):
    if num in memo:
        return memo[num]
    new_num = sum(int(d)**2 for d in str(num))
    solution = arrives_at_89(new_num)
    memo[num] = solution
    return solution

print(sum(1 for n in range(1, 10_000_000) if arrives_at_89(n)))