'''Which starting number, under one million, produces the longest Collatz sequence?'''

memo = {1: 1}

def get_length_of_chain(n):
    count = 0
    while n not in memo:
        count += 1
        if not n % 2:
            n = n // 2
        else:
            n = 3 * n + 1
    return count + memo[n]

for starting_num in range(1, 1_000_000):
    memo[starting_num] = get_length_of_chain(starting_num)

print(max(memo, key=memo.get))