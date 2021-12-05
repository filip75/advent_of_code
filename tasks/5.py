from collections import defaultdict

from aoc import *


def get_data() -> list[tuple[Point, Point]]:
    data = read_list(5)
    lines = []
    for entry in data:
        start, end = entry.split("->")
        lines.append(
            (
                Point(*cast_list(start.split(","), int)),
                Point(*cast_list(end.split(","), int)),
            )
        )

    return lines


def first() -> int:
    data = get_data()
    d = defaultdict(lambda: 0)

    for entry in data:
        start, end = entry
        if start.x == end.x:
            for i in range(min(start.y, end.y), max(start.y, end.y) + 1):
                d[start.x, i] += 1
        if start.y == end.y:
            for i in range(min(start.x, end.x), max(start.x, end.x) + 1):
                d[i, start.y] += 1

    return sum(a >= 2 for a in d.values())


def second() -> int:
    data = get_data()
    d = defaultdict(lambda: 0)

    for entry in data:
        start, end = entry
        if start.x == end.x:
            for i in range(min(start.y, end.y), max(start.y, end.y) + 1):
                d[start.x, i] += 1
        elif start.y == end.y:
            for i in range(min(start.x, end.x), max(start.x, end.x) + 1):
                d[i, start.y] += 1
        elif abs(start.x - end.x) == abs(start.y - end.y) and start != end:
            step_x = 1 if start.x < end.x else -1
            step_y = 1 if start.y < end.y else -1
            for x, y in zip(
                range(start.x, end.x + step_x, step_x),
                range(start.y, end.y + step_y, step_y),
            ):
                d[x, y] += 1

    return sum(a >= 2 for a in d.values())
