import math

def to_point(string):
    return list(map(int, string.split(",")))

def to_line(string):
    (p1, p2) = list(map(to_point, string.split(" -> ")))
    return (p1, p2)

def expand(line, mode):
    r = []
    if line[0][0] == line[1][0]:
        # vertical line
        r = [(line[0][0], y) for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1)]
    elif line[0][1] == line[1][1]:
        # horizontal line
        r = [(x, line[0][1]) for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1)]
    elif mode:
        # diagonal
        dx = line[1][0] - line[0][0]
        dy = line[1][1] - line[0][1]
        r = [(line[0][0] + math.copysign(i, dx), line[0][1] + math.copysign(i, dy)) for i in range(0, abs(dx) + 1)]
    return r

def part12(filename, expand):
    file = open(filename, "r")
    lines = file.read().splitlines()
    points = [to_line(l) for l in lines]
    all_points = [p for points in map(expand, points) for p in points]
    freq = {}
    for p in all_points:
        freq[p] = 1 + (freq[p] if p in freq else 0)
    c = 0
    for k in freq:
        if freq[k] > 1:
            c = c + 1
    file.close()
    return c

def part1(filename):
    return part12(filename, lambda l: expand(l, False))

def part2(filename):
    return part12(filename, lambda l: expand(l, True))

if __name__ == '__main__':
    FILENAME = "day5_input.txt"
    print("part1=", part1(FILENAME))
    print("part2=", part2(FILENAME))