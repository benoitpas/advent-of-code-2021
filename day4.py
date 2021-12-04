import functools

def str2list(str,sep):
    l = (s for s in str[0:-1].split(sep) if s)
    r = list(int(e) for e in l)
    return r


def scoreWinner(grid, draw):
    remaining_numbers = {e for r in grid for e in r} - set(draw)
    r = sum(remaining_numbers) * draw[-1]
    return r

def iswinner(grid, draw):
    cols = [[row[i] for row in grid] for i in range(len(grid))]
    sdraw = set(draw)
    for line in cols + grid:
        if set(line).issubset(sdraw):
            return True
    return False

def part12(filename):
    file = open(filename, "r")
    draw = str2list(file.readline(),",")
    rows = map(lambda l: str2list(l," "), file.readlines())
    grids = functools.reduce(lambda a,l: a + [[]] if not l else a[0:-1]+[a[-1]+[l]], rows,[])

    first = None
    last = None
    for i in range(1,len(draw)+1):
        sub_draw = draw[0:i]
        winners = [grid for grid in grids if iswinner(grid, sub_draw)]
        if winners:
            if not first:
                first = scoreWinner(winners[0], sub_draw)
            for winner in winners:
                grids.remove(winner)
            if not grids:
                last = scoreWinner(winners[0], sub_draw)
                break
    
    file.close()
    return (first, last)


if __name__ == '__main__':
    (first,last) = part12("day4_input.txt")
    print("part1=", first)
    print("part2=", last)

