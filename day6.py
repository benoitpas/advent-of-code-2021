file = open("day6_input.txt")
day6_input = file.read()

def next_day(day_map):
    r = day_map[1:] + day_map[:1]
    r[6] = r[6] + day_map[0]
    return r

def part12(input):
    days = list(map(int, input[0:-1].split(",")))
    day_map = [0] * 9

    for day in days:
        day_map[day] = day_map[day] + 1

    part1 = 0
    for i in range(256):
        if i == 80:
            part1 = sum(day_map)
        day_map = next_day(day_map)
    part2 = sum(day_map)

    return (part1, part2)

if __name__ == '__main__':
    (part1, part2) = part12(day6_input)
    print("part1=", part1)
    print("part2=", part2)
