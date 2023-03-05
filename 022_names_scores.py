'''What is the total of all the name scores in the file?'''

from string import ascii_uppercase

path = 'Project_Euler/puzzle_input/022.txt'
with open(path) as file:
    names = sorted(name.strip('"') for name in file.read().split(','))

alphabet = '_' + ascii_uppercase

def score_name(name, idx):
    return sum(alphabet.index(char) for char in name) * idx

def get_total_score(names):
    return sum(score_name(name, idx) for idx, name in enumerate(names, start=1))

print(get_total_score(names))