'''Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''

def calc_power_sum(num, power=5):
    return sum(int(d)**power for d in str(num))

print(sum(n for n in range(2, 1_000_000) if n == calc_power_sum(n)))