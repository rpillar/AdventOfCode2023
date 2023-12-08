"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Use Data file - ./Data/data_file_1.txt

read file
get the numbers in each string - n = [x for x in s if x.isdigit()]
create a number from the first and last digits - o = int( n[0] + n[-1] )
add this number to a 'total' (the accumulator)
print total at end.
"""
with open('Data/avc_day1.txt') as reader:
    total = 0
    line = reader.readline()
    while line != '':
        n_array = [x for x in line if x.isdigit()]
        number = int( n_array[0] + n_array[-1] )
        total = total + number
        print(f"line : {line} / number : {number} / total : {total}")
        line = reader.readline()

    print(f"The total is : {total}")

