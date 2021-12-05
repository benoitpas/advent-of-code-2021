from functools import reduce
import itertools

def toPoint(str):
    return list(map(int, str.split(",")))

def toLine(str):
    (p1,p2) = list(map(toPoint, str.split(" -> ")))
    return (p1,p2)

def expand(line):
    r = []
    if line[0][0] == line[1][0]:
        # vertical line
        r = [(line[0][0], y) for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1)]
    if line[0][1] == line[1][1]:
        # horizontal line
        r = [(x, line[0][1]) for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1)]
    return r

def part1(filename):
    file = open(filename, "r")
    lines = file.read().splitlines()
    points = [toLine(l) for l in lines]
    all_points = [p for points in map(expand, points) for p in points]
    freq = {}
    for p in all_points:
        freq[p] = 1 + (freq[p] if p in freq else 0)
    c = 0
    for k in freq.keys():
        if freq[k]>1:
            c = c + 1
    return c

filename = "day5_input.txt"
print("part1=", part1(filename))