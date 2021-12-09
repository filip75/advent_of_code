from itertools import *
from math import prod

from aoc import *

DIFS = [
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 0),
]
VISITED = "X"


def get_data() -> list:
    data = read_list(9)
    return [[int(x) for x in line] for line in data]


def first() -> int:
    data = get_data()

    width, height = len(data[0]), len(data)

    s = 0
    for x, y in product(range(height), range(width)):
        adjecent = [
            data[x - a][y - b]
            for a, b in DIFS
            if 0 <= x - a < height and 0 <= y - b < width
        ]
        if all(a > data[x][y] for a in adjecent):
            s += data[x][y] + 1

    return s


def get_neighbours(coordinate: tuple, width: int, height: int):
    r = []
    for d in DIFS:
        n = (coordinate[0] + d[0], coordinate[1] + d[1])
        if 0 <= n[0] < height and 0 <= n[1] < width:
            r.append(n)
    return r


def second() -> int:
    data = get_data()

    width, height = len(data[0]), len(data)

    lps = []
    for x, y in product(range(height), range(width)):
        adjecent = [
            data[x - a][y - b]
            for a, b in DIFS
            if 0 <= x - a < height and 0 <= y - b < width
        ]
        if all(a > data[x][y] for a in adjecent):
            lps.append((x, y))

    basins = []
    for lp in lps:
        basins.append(0)
        to_visit = [lp]

        while to_visit:
            c = to_visit.pop()
            value = data[c[0]][c[1]]
            if value not in (VISITED, 9):
                basins[-1] += 1
                data[c[0]][c[1]] = VISITED
                to_visit.extend([f for f in get_neighbours(c, width, height)])

    return prod(sorted(basins, reverse=True)[:3])
