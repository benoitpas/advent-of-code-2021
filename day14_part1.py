
def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    polymer = lines[0]
    m = {}
    for i in range(2, len(lines)):
        p = lines[i].split(" -> ")
        m[p[0]] = p[1]
    
    return (polymer, m)

m = {
    "CH" : "B",
    "HH" : "N",
    "CB" : "H",
    "NH" : "C",
    "HB" : "C",
    "HC" : "B",
    "HN" : "C",
    "NN" : "C",
    "BH" : "H",
    "NC" : "B",
    "NB" : "B",
    "BN" : "B",
    "BB" : "N",
    "BC" : "B",
    "CC" : "N",
    "CN" : "C"}

def updateMap(m):
    for k in m:
        m[k] = k[0] + m[k]

def next(s):
    pairs = []
    for i in range(len(s)-1):
        pairs.append(s[i:i+2])
    pairs.append(s[-1])
    return "".join(map(lambda p: m[p] if p in m else p, pairs))

def toFreq(s):
    fm = {}
    for e in s:
        fm[e] = 1 + fm[e] if e in fm else 1
    p = sorted(fm.items(), key = lambda p : p[1])
    return p

#(polymer,m) = parse_input("day14_input.txt")
updateMap(m)
polymer ="NNCB"
for i in range(40):
    polymer = next(polymer)
    print(i,len(polymer))

fpolymer = toFreq(polymer)
min = fpolymer[0][1]
max = fpolymer[-1][1]
print(max-min)