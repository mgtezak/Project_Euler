'''Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?'''

print(max(sum(int(n) for n in str(a**b)) for a in range(100) for b in range(100)))