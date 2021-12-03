import functools

file = open("day3_input.txt", "r")
lines = list(file.readlines())

numbers = list(map(lambda l:  list(map(lambda d:int(d),l[0:-1])), lines))

numbersTest = list(map(lambda l: list(map(lambda d:int(d),l)),[
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
    nbNumbers = len(numbers)
    nbDigits = len(numbers[0])

    r1 = 0
    for i in range(0, nbDigits):
        c = 0
        for j in range(0, nbNumbers):
            c += numbers[j][i]
        r1 *= 2
        if c > nbNumbers/2:
            r1 += 1
    r2 = (pow(2,nbDigits)-1-r1)
    return r1 * r2

def mostCommon(numbers, index):
    if len(numbers) == 1:
        r = numbers[0] 
    else:
        sum_digits = sum(map(lambda l:l[index], numbers))
        most_common_digit = 1 if sum_digits>=len(numbers)/2 else 0
        next_numbers = list(filter(lambda l: l[index] == most_common_digit, numbers))
        r = mostCommon(next_numbers, index+1)
    return r

def lessCommon(numbers, index):
    if len(numbers) == 1:
        r = numbers[0] 
    else:
        sum_digits = sum(map(lambda l:l[index], numbers))
        less_common_digit = 1 if sum_digits<len(numbers)/2 else 0
        next_numbers = list(filter(lambda l: l[index] == less_common_digit, numbers))
        r = lessCommon(next_numbers, index+1)
    return r

def toDecimal(digits):
    return functools.reduce(lambda a,b: a*2+b, digits)

def part2(numbers):
    oxygen = toDecimal(mostCommon(numbers, 0))
    co2 = toDecimal(lessCommon(numbers, 0))
    return oxygen*co2

if __name__ == '__main__':
    print("part1=", part1(numbers))
    print("part2=", part2(numbers))