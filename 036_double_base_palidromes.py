'''Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.'''

def is_palidromic(num):
    bin_ = bin(num)[2:]
    num = str(num)
    if num == num[::-1] and bin_ == bin_[::-1]:
        return True
    return False

print(sum(n for n in range(1_000_000) if is_palidromic(n)))