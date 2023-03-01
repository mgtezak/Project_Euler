'''By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.'''

def even_fibonacci_num_generator(limit):
    prev_val = 0
    curr_val = 1
    while (next_val := prev_val + curr_val) <= limit:
        if not next_val % 2:
            yield next_val
        prev_val = curr_val
        curr_val = next_val

print(sum(n for n in even_fibonacci_num_generator(limit=4_000_000)))