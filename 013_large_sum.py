'''Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.'''

path = 'Project_Euler/puzzle_input/013.txt'

with open(path) as file:
    nums = [int(n) for n in file.read().split('\n')]

first_ten_digits = str(sum(nums))[:10]
print(first_ten_digits)