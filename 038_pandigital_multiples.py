'''What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?'''

def generate_multiples(n):
    for i in range(1, 10):
        yield i * n
    
def concat_multiples(n):
    concat = ''
    for mul in generate_multiples(n):
        concat += str(mul)
        if len(concat) >= 9:
            return concat

def is_pandigital(concat):
    if len(concat) > 9 or len(set(concat)) < 9 or '0' in concat:
        return False
    return True

pandigital_multiples = []

for n in range(1_000_000):
    concat = concat_multiples(n)
    if is_pandigital(concat):
        pandigital_multiples.append(int(concat))

print(max(pandigital_multiples))