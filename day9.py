def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
        rows = [[int(h) for h in l] for l in lines]

    return rows

def part12(filename):
    heightmap = parse_input(filename)

    def neighbours(x,y):
        up = [(x,y - 1)] if y > 0 else []
        down =[(x, y + 1)] if y < (len(heightmap) - 1) else []
        left = [(x - 1, y)] if x > 0 else []
        right = [(x + 1, y)] if x < (len(heightmap[y]) - 1) else []
        return up + down + left + right

    def low_point(x,y):
        r = True
        h = heightmap[y][x]
        for (nx,ny) in neighbours(x,y):
            r = r and h < heightmap[ny][nx]
        return r

    def basin(x,y, known_points):
        new_known_points = known_points.union({(x,y)})
        nb = set(neighbours(x,y)).difference(known_points)
        for (p_x,p_y) in nb:
            if heightmap[y][x] < heightmap[p_y][p_x] and heightmap[p_y][p_x] < 9:
                new_known_points.update(basin(p_x,p_y, new_known_points))
        return new_known_points

    low_points = [(x,y) for y in range(len(heightmap)) for x in range(len(heightmap[y])) if low_point(x,y)]
    low_heights = [int(heightmap[y][x]) + 1 for (x,y) in low_points]
    part1 = sum(low_heights)
    basins = sorted([len(basin(x,y,set())) for (x,y) in low_points])
    part2 = basins[-1]*basins[-2]*basins[-3]
    return (part1,part2)

if __name__ == '__main__':
    (part1, part2) = part12("day9_input.txt")
    print("part1=", part1)
    print("part2=", part2)
    