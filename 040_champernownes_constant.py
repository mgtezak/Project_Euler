'''An irrational decimal fraction is created by concatenating the positive integers. If dn 
represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000'''

f = ''
for n in range(200_000):
    f += str(n)

print(int(f[1]) * int(f[10]) * int(f[100]) * int(f[1000]) * int(f[10_000]) * int(f[100_000]) * int(f[1_000_000]))