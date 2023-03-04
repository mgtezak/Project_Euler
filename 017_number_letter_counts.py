'''If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?'''

letters = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4, '10': 3, 
        '11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8,
        '20': 6, '30': 6, '40': 5, '50': 5, '60': 5, '70': 7, '80': 6, '90': 6}

def get_length_of_num_name(n):
    if n == 1000:
        return 11
    w = str(n)
    if w in letters:
        return letters[w]
    if n < 100:
        return letters[f'{w[0]}0'] + letters[w[1]]
    if w[1:] == '00':
        return letters[w[0]] + 7
    return letters[w[0]] + 10 + get_length_of_num_name(int(w[1:]))

print(sum(get_length_of_num_name(n) for n in range(1, 1001)))