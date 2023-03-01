'''Find the sum of all the multiples of 3 or 5 below 1000.'''

print(sum(n for n in range(3, 1000) if not n % 3 or not n % 5))