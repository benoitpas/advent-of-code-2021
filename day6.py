file = open("day6_input.txt")
day6_input = file.read()

def new_map():
    day_map = {}
    for day in range(9):
        day_map[day] = 0
    return day_map

def next_day(day_map):
    r = new_map()
    r[2] = day_map[3]
    r[1] = day_map[2]
    r[0] = day_map[1]
    r[6] = day_map[0] + day_map[7]
    r[8] = day_map[0]
    r[7] = day_map[8]
    r[3] = day_map[4]
    r[4] = day_map[5]
    r[5] = day_map[6]
    return r

def part12(input):
    days = list(map(int, input[0:-1].split(",")))
    day_map = new_map()

    for day in days:
        day_map[day] = day_map[day] + 1

    def sum_days(dm):
        return sum(list(dm.values()))

    part1 = 0
    for i in range(256):
        if i == 80:
            part1 = sum_days(day_map)
        day_map = next_day(day_map)
    part2 = sum_days(day_map)

    return (part1, part2)

if __name__ == '__main__':
    (part1, part2) = part12(day6_input)
    print("part1=", part1)
    print("part2=", part2)
