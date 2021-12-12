def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines

def cnx2map(cnxs):
    paths = [c.split('-') for c in cnxs]
    r = dict()
    for p in paths:
        if not p[0] in r:
            r[p[0]] = []
        r[p[0]].append(p[1])
        if not p[1] in r:
            r[p[1]] = []
        r[p[1]].append(p[0])
    return r

def is_upper_case(s):
    return s == s.upper()

def findPaths(start, cm, visited, twice_visited):
    r = []
    if start == 'end':
        r = [[start]]
    elif start in cm:
        nexts = cm[start]
        n_visited = visited.union({start} if not is_upper_case(start) else {})
        r = [[start] + path
            for next_node in nexts if is_upper_case(next_node) or not next_node  in visited or not twice_visited and next_node != "start"
            for path in findPaths(next_node, cm, n_visited, 
                twice_visited or (not is_upper_case(next_node) and next_node in visited and next_node != "start")) ]
    return r

def countPaths(cm, twice_visited):
    return len (findPaths("start", cm, set(), twice_visited))

if __name__ == '__main__':
    lines = parse_input("day12_input.txt")
    cm = cnx2map(lines)
    print("part1=", countPaths(cm, True))
    print("part2=", countPaths(cm, False))

#cm = cnx2map(cnx1)
#print(len(findPaths("start",cm, set(), True)))
#lines = parse_input("day12_input.txt")
#cm = cnx2map(lines)
#print(len(findPaths("start",cm2, set(), True)))

#p = findPaths("start",cm, set(), False)
#print(len(p))
#print(len(findPaths("start",cm2, set(),False)))