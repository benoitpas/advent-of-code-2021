
from typing import _ProtocolMeta

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    polymer = lines[0]
    m = {}
    for i in range(2, len(lines)):
        p = lines[i].split(" -> ")
        m[p[0]] = p[1]
    
    return (polymer, m)

def toFreq(s):
    fm = {}
    for e in s:
        fm[e] = 1 + fm[e] if e in fm else 1
    p = sorted(fm.items(), key = lambda p : p[1])
    return p

def part12(polymer, mapping):

    def updateMap(m):
        for k in m:
            m[k] = [k[0] + m[k], m[k]+ k[1]]

    def toPairFreq(s):
        r = {}
        for i in range(len(s) - 1):
            p = s[i:i+2]
            r[p] = 1 + r[p] if p in r else 1
        return r

    def next(pairMap):
        r = {}
        for pair in pairMap:
            p1 =  mapping[pair][0]
            p2 =  mapping[pair][1]
            r[p1] = pairMap[pair] + (r[p1] if p1 in r else 0)
            r[p2] = pairMap[pair] + (r[p2] if p2 in r else 0)
        return r

    def toPairMapFreq(pairMap):
        r = {}
        for pair in pairMap:
            e = pair[0]
            r[e] = pairMap[pair] + (r[e] if e in r else 0)
        lastletter = polymer[-1]
        r[lastletter] = 1 + (r[lastletter] if lastletter in r else 0)
        return r

    def result(pairMap):
        freq = toPairMapFreq(pairMap)
        s_freq = sorted(freq.items(), key=lambda p:p[1])
        return s_freq[-1][1]-s_freq[0][1]


    updateMap(mapping)
    np = toPairFreq(polymer)
    for i in range(40):
        np = next(np)
        part2 = result(np)
        if i == 9:
            part1 = part2
    return (part1, part2)

if __name__ == '__main__':
    (polymer,mapping) = parse_input("day14_input.txt")
    (part1, part2) = part12(polymer, mapping)
    print("part1=", part1)
    print("part2=", part2)