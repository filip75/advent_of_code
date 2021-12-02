map = []
with open("3.input") as file:
    for line in file.readlines():
        map.append(list(line.strip()))


def determine_slope(slope):
    x, y = 0, 0
    trees = 0
    while y < len(map):
        if map[y][x] == "#":
            trees += 1
        x = (x + slope[0]) % len(map[1])
        y = y + slope[1]
    return trees


print(determine_slope((3, 1)))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slope_results = [determine_slope(s) for s in slopes]
m = 1
for r in slope_results:
    m *= r
print(m)
