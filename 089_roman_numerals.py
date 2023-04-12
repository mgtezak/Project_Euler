with open('Project_Euler/puzzle_input/089.txt') as f:
    nums = f.read().split('\n')

conversion_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
conversion_2 = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}

def roman_to_number(roman):
    total = 0
    prev = None
    for char in roman:
        num = conversion_1[char]
        if prev is None:
            prev = num
        elif prev == num:
            total += num
        elif prev > num:
            total += prev
            prev = num
        else:
            total += num - prev
            prev = None
    if prev:
        total += prev
    return total


def number_to_roman(number):
    roman = ''
    ones = number % 10
    tens = number % 100 - ones
    hundreds = number % 1000 - tens
    thousands = number // 1000

    roman += thousands * 'M'

    hundreds //= 100
    if hundreds <= 3:
        roman += hundreds * 'C'
    elif hundreds == 4:
        roman += 'CD'
    elif hundreds <= 8:
        roman += 'D' + (hundreds-5) * 'C' 
    else:
        roman += 'CM' 

    tens //= 10
    if tens <= 3:
        roman += tens * 'X'
    elif tens == 4:
        roman += 'XL'
    elif tens <= 8:
        roman += 'L' + (tens-5) * 'X' 
    else:
        roman += 'XC'  

    if ones <= 3:
        roman += ones * 'I'
    elif ones == 4:
        roman += 'IV'
    elif ones <= 8:
        roman += 'V' + (ones-5) * 'I' 
    else:
        roman += 'IX'

    return roman

print(sum(len(num) - len(number_to_roman(roman_to_number(num))) for num in nums))