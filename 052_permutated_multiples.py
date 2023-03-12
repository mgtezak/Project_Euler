'''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different 
order. Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''

for n in range(1, 1_000_000):
    if (digits := sorted(str(n))) != sorted(str(n*2)):
        continue
    if digits != sorted(str(n*3)):
        continue
    if digits != sorted(str(n*4)):
        continue
    if digits != sorted(str(n*5)):
        continue
    if digits != sorted(str(n*6)):
        continue
    break

print(n)