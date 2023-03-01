'''What is the largest prime factor of the number 600851475143 ?'''

num = 600_851_475_143

n = 3
while num > n:
    if num % n == 0:
        num //= n
    else:
        n += 2

print(n)