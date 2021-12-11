from aoc import *

FLASHED = "X"


def get_data() -> list:
    data = read_list(11)
    return [[int(c) for c in line] for line in data]


def first() -> int:
    data = get_data()
    map = Map(data)
    flashes = 0

    for _ in range(100):
        for point in map:
            map[point] += 1

        for point in map:
            if map[point] != FLASHED and map[point] > 9:
                to_visit = [point]
                while to_visit:
                    c = to_visit.pop()
                    if map[c] != FLASHED and map[c] > 9:
                        map[c] = FLASHED
                        neighbours = map.get_adjacent(c)
                        for n in neighbours:
                            if map[n] != FLASHED:
                                map[n] += 1
                        to_visit.extend(neighbours)

        for point in map:
            if map[point] == FLASHED:
                map[point] = 0
                flashes += 1

    return flashes


def second() -> int:
    data = get_data()
    map = Map(data)
    day = 0
    
    while True:
        for point in map:
            map[point] += 1

        for point in map:
            if map[point] != FLASHED and map[point] > 9:
                to_visit = [point]
                while to_visit:
                    c = to_visit.pop()
                    if map[c] != FLASHED and map[c] > 9:
                        map[c] = FLASHED
                        neighbours = map.get_adjacent(c)
                        for n in neighbours:
                            if map[n] != FLASHED:
                                map[n] += 1
                        to_visit.extend(neighbours)
        day += 1

        if all(map[p] == FLASHED for p in map):
            break

        for point in map:
            if map[point] == FLASHED:
                map[point] = 0

    return day
