import functools

def to_state(l):
    return list(map(lambda s: list(map(int,s.strip())),l))

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return to_state(lines)

def neighbours(mx, my, n):
    xmin = max(0, mx - 1)
    xmax = min(n, mx + 2)
    ymin = max(0, my - 1)
    ymax = min(n, my + 2)
    r = [(x,y) for x in range(xmin, xmax) for y in range(ymin, ymax) if x != mx or y != my]
    return r

def next(state):
    n = len(state)

    # increase enery levels
    for y in range(n):
        for x in range(n):
            state[y][x] = state[y][x] + 1

    # check for flashes
    oneflash = True
    flash =[[False] * n for i in range(n)]
    while oneflash:
        oneflash = False
        for y in range(n):
            for x in range(n):
                if not flash[y][x] and state[y][x] > 9:
                    flash[y][x] = oneflash = True
                    for (x,y) in neighbours(x, y, n):
                        state[y][x] = state[y][x] + 1

    # Reset energy levels
    for y in range(n):
         for x in range(n):
             if state[y][x] > 9:
                  state[y][x] = 0

    nb_flashes = sum((1 if flash[y][x] else 0 for x in range(n) for y in range(n)))
    return nb_flashes

def part12(filename):
    state = parse_input(filename)
    all = len(state) * len(state)
    part1 = 0
    part2 = 100
    nb_flash = 0
    for i in range(part2):
        nb_flash = next(state)
        part1 = part1 + nb_flash
    
    while nb_flash < all:
        part2 = part2 + 1
        nb_flash = next(state)

    return (part1,part2)

if __name__ == '__main__':
    (part1, part2) = part12("day11_input.txt")
    print("part1=", part1)
    print("part2=", part2)

