from math import gcd, asin, pi, sqrt
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


def assign_angle(p: Point):
    if p[0]:
        v = p[0] / sqrt(p[0] ** 2 + p[1] ** 2)
    else:
        v = 1
    if p[0] >= 0 and p[1] < 0:
        return asin(v)
    elif p[0] >= 0 and p[1] >= 0:
        return asin(v) + pi / 2
    elif p[0] < 0 and p[1] >= 0:
        return asin(v) + pi
    elif p[0] < 0 and p[1] < 0:
        return asin(v) + pi * 3 / 2


with open("input.txt") as file:
    asteroids = []
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    m = 0
    station = None
    for a in asteroids:
        c = len(eliminate_covered(a, asteroids)) - 1
        if c > m:
            m = c
            station = a
    print(m)

    # this only works because more than 200 asteroids are visible at the beginning, otherwise after each rotation
    # new visible asteroids should be determined
    visible = eliminate_covered(station, asteroids)
    asteroids_with_angles = [(a, assign_angle((a[0] - station[0], a[1] - station[1]))) for a in visible]
    asteroids_with_angles = sorted(asteroids_with_angles, key=lambda x: x[1])
    print(asteroids_with_angles[200][0][0] * 100 + asteroids_with_angles[200][0][1])
