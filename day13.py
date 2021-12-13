def to_point(line):
    return tuple(map(int, line.split(",")))

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    whilePoints = True
    folds = []
    points = []
    for l in lines:
        if whilePoints:
            if l:
                points.append(to_point(l))
            else:
                whilePoints = False
        else:
            folds.append(tuple(l.split("fold along ")[1].split('=')))
    return (points, folds)
            
def display(points):
    xmin = xmax = points[0][0]
    ymin = ymax = points[0][1]
    for (x,y) in points:
        xmin = min(xmin, x)
        ymin = min(ymin, y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)
    w = xmax - xmin + 1
    h = ymax - ymin + 1
    a = [['.'] * w for i in range(h)]
    for (x,y) in points:
        a[y][x] = '#'
    for i in range(h):
        print("".join(a[i]))

def foldy(points, fold_y):
    r = set()
    for (x,y) in points:
        if (y < fold_y):
            r.add((x,y))
        elif (y > fold_y):
            r.add((x, 2 * fold_y - y))
    return list(r)

def foldx(points, fold_x):
    r = set()
    for (x,y) in points:
        if (x < fold_x):
            r.add((x,y))
        elif (x > fold_x):
            r.add((2 * fold_x - x, y))
    return list(r)

if __name__ == '__main__':
    (p_all, folds)= parse_input("day13_input.txt")
    part1 = len(foldx(p_all, 655))
    print("part1=", part1)

    for (cmd, value) in folds:
        if cmd == "x":
            p_all = foldx(p_all, int(value))
        elif cmd == "y":
            p_all = foldy(p_all, int(value))

    display(p_all)