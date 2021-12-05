"""Day 3 aoc 2021"""

import functools

FILE = open("day3_input.txt", "r")
LINES = list(FILE.readlines())

NUMBERS = list(map(lambda l: list(map(int, l[0:-1])), LINES))

NUMBERSTEST = list(map(lambda l: list(map(int, l)), [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"]))

def part1(numbers):
    nb_numbers = len(numbers)
    nb_digits = len(numbers[0])

    r1 = 0
    for i in range(0, nb_digits):
        c = 0
        for j in range(0, nb_numbers):
            c += numbers[j][i]
        r1 *= 2
        if c > nb_numbers/2:
            r1 += 1
    r2 = (pow(2, nb_digits)-1-r1)
    return r1 * r2

def mostCommon(numbers, index):
    if len(numbers) == 1:
        r = numbers[0]
    else:
        sum_digits = sum(map(lambda l: l[index], numbers))
        most_common_digit = 1 if sum_digits >= len(numbers)/2 else 0
        next_numbers = list(filter(lambda l: l[index] == most_common_digit, numbers))
        r = mostCommon(next_numbers, index+1)
    return r

def lessCommon(numbers, index):
    if len(numbers) == 1:
        r = numbers[0]
    else:
        sum_digits = sum(map(lambda l: l[index], numbers))
        less_common_digit = 1 if sum_digits < len(numbers)/2 else 0
        next_numbers = list(filter(lambda l: l[index] == less_common_digit, numbers))
        r = lessCommon(next_numbers, index+1)
    return r

def to_decimal(digits):
    return functools.reduce(lambda a, b: a*2+b, digits)

def part2(numbers):
    oxygen = to_decimal(mostCommon(numbers, 0))
    co2 = to_decimal(lessCommon(numbers, 0))
    return oxygen*co2

if __name__ == '__main__':
    print("part1=", part1(NUMBERS))
    print("part2=", part2(NUMBERS))
