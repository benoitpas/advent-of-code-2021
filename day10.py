import functools

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines

op = {'(' : ')', '<' : '>', '{' : '}', '[' : ']' }
cp = dict(zip(op.values(), op.keys()))

# returns the first illegal character (or None)
def fig(line):
    stack = []
    for c in line:
        if c in op:
            stack.append(op[c])
        elif c in set(op.values()):
            if stack.pop() != c:
                return (c,None)
    return (None, stack)

def score(stack):
    points = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }
    stack.reverse()
    return functools.reduce(lambda a, c: a * 5 + points[c], stack, 0)

def part12(filename):
    lines = parse_input(filename)
    r = dict(zip(op.values(), [0] * len(op.values())))
    scores = []
    for l in lines:
        (ic, stack) = fig(l)
        if ic:
            r[ic] = 1 + r[ic]
        if stack:
            scores.append(score(stack))

    part1 = 3 * r[')'] + 57 * r[']'] + 1197 * r['}'] + 25137 * r['>']
    scores.sort()
    part2 = scores[int(len(scores)/2)]
    return part1, part2

if __name__ == '__main__':
    r = part12("day10_input.txt")
    print("part1=", r[0])
    print("part2=", r[1])
