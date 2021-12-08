import itertools
from os import replace

def sort_letters(s):
    return  "".join(sorted(s))

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
        r = [[sort_letters(w) for w in l.replace(" |", "").split(" ")] for l in lines]
    return r

def perm_value(output, combination):
    m = dict(zip(combination,range(len(combination))))
    r = 0
    for v in output:
        r = r * 10 + m[v]
    return r

def to_digits(perm):
    zero = perm[0:3] + perm[4:]
    one = perm[2] + perm[5]
    two = perm[0] + perm[2:5] + perm[6]
    three = perm[0] + perm[2:4] + perm[5:]
    four = perm[1:4] + perm[5]
    five = perm[0:2] + perm[3] + perm[5:]
    six = perm[0:2] + perm[3:]
    seven = perm[0] + perm[2] + perm[5]
    eigth = perm
    nine = perm[0:4] + perm[5:]
    return list(map(sort_letters,[zero, one, two, three, four, five, six, seven, eigth, nine]))


def part2(filename):
    outputs = parse_input("day8_input.txt")
    perms = map(lambda l: "".join(l), itertools.permutations("abcdefg"))
    perm_map = {p: to_digits(p) for p in perms}

    ret = 0
    for output in outputs:
        for perm in perm_map:
            if set(output).issubset(set(perm_map[perm])):
                ret = ret + perm_value(output[-4:], perm_map[perm])
                break
    return ret

if __name__ == '__main__':
    print("part2=", part2("day8_input.txt"))
