'''Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.'''

sqr_of_sum = sum(range(101))**2
sum_of_sqr = sum(n**2 for n in range(101))
solution = sqr_of_sum - sum_of_sqr
print(solution)