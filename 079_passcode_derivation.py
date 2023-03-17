'''A common security method used for online banking is to ask the user for three random 
characters from a passcode. For example, if the passcode was 531278, they may ask for the 
2nd, 3rd, and 5th characters; the expected reply would be: 317. The text file contains fifty 
successful login attempts. Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret passcode of unknown length.'''

path = 'Project_Euler/puzzle_input/079.txt'

with open(path) as file:
    sequences = file.read().split('\n')

# check if duplicate digits in any of the sequences
all_digits = set()
for s in sequences:
    if len(set(s)) != len(s):
        print(s)
    all_digits |= set(s)

# no duplicates at all, so finding the correct order is easy:
order = {d: set() for d in all_digits}
for s in sequences:
    for i, d in enumerate(s):
        order[d] |= set(s[:i])

pw = ''
while order:
    for d in order:
        if order[d] == set():
            pw += d
            break
    del order[d]
    for n in order:
        if d in order[n]:
            order[n].remove(d)

print(pw)