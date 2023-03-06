'''Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''

def measure_recurring_cycle(a, b):
    result = ''
    while len(result) < 10000:
        result += str(a // b)
        a = a % b * 10

    segment = result[100:110]
    return result[110:].index(segment)

print(max([(measure_recurring_cycle(1, b), b) for b in range(1, 1000)])[1])