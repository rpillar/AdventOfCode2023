"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

n_strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
n_digits = [0,1,2,3,4,5,6,7,8,9]

def parse_for_string(s):
    number_collection = []
    for idx, number in enumerate(n_strings):
        pos = s.find(number)
        if ( pos > -1 ):
            number_collection.append( (pos, idx) )
    return number_collection

# note - only gets the 'first' of a number when there might be more ...
def parse_for_number(s):
    digit_collection = []
    for idx, number in enumerate(n_digits):
        pos = s.find(str(number))
        if ( pos != -1 ):
            digit_collection.append( (pos, number) )
    return digit_collection

with open('Data/avc_day1.txt') as reader:
    total = 0
    line = reader.readline()
    while line != '':
        string_t = parse_for_string(line)
        number_t = parse_for_number(line)

        joined_list = string_t + number_t
        sorted_list = sorted(joined_list)
        print(f"line : {line}")
        number = str(sorted_list[0][1]) + str(sorted_list[-1][1])
        print(f"number : {number}")
        total = total + int(number)
        print(f"total : {total}")
        print("=====")
        line = reader.readline()

    print(f"The total is : {total}")

