'''How many Lychrel numbers are there below ten-thousand?'''

def is_lychrel(num):
    reverse = int(str(num)[::-1])
    for _ in range(50):
        num += reverse
        if num == (reverse := int(str(num)[::-1])):
            return False
    return True

print(sum(1 for num in range(10_000) if is_lychrel(num)))