from math import gcd
from typing import Tuple, List

Point = Tuple[int, int]


def compute_step(s: Point, e: Point) -> Point:
    dx = e[0] - s[0]
    dy = e[1] - s[1]
    m = gcd(dx, dy)
    if m != 0:
        return dx // m, dy // m
    return 0, 0


def is_covered(s: Point, e: Point, step: Point) -> bool:
    dx = e[0] - s[0]
    dy = e[1] - s[1]

    if dx == 0 and dy != 0 and step[0] == 0 and step[1] != 0:
        return (dy / step[1]) > 0
    if dy == 0 and dx != 0 and step[1] == 0 and step[0] != 0:
        return (dx / step[0]) > 0
    if dx != 0 and dy != 0:
        if step[0] != 0 and step[1] != 0:
            dxd = dx / step[0]
            dyd = dy / step[1]
            return (dxd == dyd) and (dxd > 0)
        return False
    return False


def eliminate_covered(station: Point, asteroids: List[Point]) -> List[Point]:
    asteroids_copy = asteroids[:]
    ast = asteroids[:]
    ast.remove(station)
    for a in ast:
        for b in ast:
            if is_covered(a, b, compute_step(station, a)):
                try:
                    asteroids_copy.remove(b)
                except ValueError:
                    pass

    return asteroids_copy


with open("input.txt") as file:
    asteroids = []
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    m = 0
    for a in asteroids:
        c = len(eliminate_covered(a, asteroids))
        m = max(m, c)
        print(f'{a} {c}')
    print(m - 1)
