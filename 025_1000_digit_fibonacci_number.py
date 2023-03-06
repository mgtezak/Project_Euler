'''What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

target = 10**999
fib_sequence = [1, 1]
while (prev := fib_sequence[-1]) < target:
    fib_sequence.append(prev + fib_sequence[-2])

print(len(fib_sequence))