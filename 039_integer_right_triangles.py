'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?'''

max_n_solutions = 0
winner = 0
for p in range(1001):
    n_solutions = 0
    for a in range(1, p//2):
        for b in range(a, p//2):
            if (p - a - b)**2 == a**2 + b**2:
                n_solutions += 1
    if n_solutions > max_n_solutions:
        max_n_solutions = n_solutions
        winner = p

print(winner)