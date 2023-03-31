'''How many different ways can one hundred be written as a sum of at least two positive integers?'''

target = 100
num_ways_to_sum = [1] + [0] * target 
for i in range(1, target):
    for j in range(i, target + 1):
        num_ways_to_sum[j] += num_ways_to_sum[j - i]

print(num_ways_to_sum[-1])