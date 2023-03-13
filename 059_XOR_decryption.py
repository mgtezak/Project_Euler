'''Using the knowledge that the plain text must contain common English words, decrypt 
the message and find the sum of the ASCII values in the original text. The encryption 
key consists of three lower case characters'''

from itertools import cycle

path = 'Project_Euler/puzzle_input/059.txt'
with open(path) as file:
    nums = [int(n) for n in file.read().split(',')]

alphabet_lowercase = range(97, 123)

def decrypt():
    for a in alphabet_lowercase:
        for b in alphabet_lowercase:
            for c in alphabet_lowercase:
                key = iter(cycle((a, b, c)))
                decrypted = ''.join(chr(n ^ next(key)) for n in nums)
                if 'the' in decrypted and 'and' in decrypted and 'for' in decrypted:
                    key = iter(cycle((a, b, c)))
                    return decrypted + '\n', sum(n ^ next(key) for n in nums)

decypted_message, decrypted_ascii_sum = decrypt()
print(decypted_message)
print(decrypted_ascii_sum)