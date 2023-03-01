'''Find the thirteen adjacent digits in the 1000-digit number that 
have the greatest product. What is the value of this product?'''

path = 'Project_Euler/puzzle_input/008.txt'

with open(path) as file:
    num = [int(n) for line in file.read().split('\n') for n in line]
    
solution = 0
for i in range(988):
    prod = 1
    for j in range(i, i+13):
        prod *= num[j]
    solution = max(prod, solution)

print(solution)