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
                return c
    return None

def part1(filename):
    lines = parse_input(filename)
    r = dict(zip(op.values(), [0] * len(op.values())))
    for l in lines:
        c = fig(l)
        if c:
            r[c] = 1 + r[c]

    part1 = 3 * r[')'] + 57 * r[']'] + 1197 * r['}'] + 25137 * r['>']
    return part1

if __name__ == '__main__':
    print("part1=", part1("day10_input.txt"))
    