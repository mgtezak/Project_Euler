'''in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 
28433 × 2^7830457 + 1. Find the last ten digits of this prime number.'''

num = 2
for _ in range(1, 7_830_457):
    num = (num * 2) % 10_000_000_000
num = 28_433 * num + 1
print(num % 10_000_000_000)