'''Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.'''

print(str(sum(x**x for x in range(1, 1001)))[-10:])