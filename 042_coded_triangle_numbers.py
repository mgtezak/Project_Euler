'''How many words in the puzzle input are triangle words?'''

import string

path = 'Project_Euler/puzzle_input/042.txt'
with open(path) as file:
    words =  [word.strip('"') for word in file.read().split(',')]

alphabet = '_' + string.ascii_uppercase
def get_word_value(word):
    val = 0
    for char in word:
        val += alphabet.index(char)
    return val

triangle_nums = [int((n/2)*(n+1)) for n in range(500)]
print(sum(1 for word in words if get_word_value(word) in triangle_nums))