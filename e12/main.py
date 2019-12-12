import re
from collections import defaultdict
from itertools import combinations, permutations
from math import ceil, sqrt, floor
from typing import List

with open('input.txt') as file:
    moons = []
    for line in file:
        x = int(re.findall(r'x=([\-0-9]+)', line)[0])
        y = int(re.findall(r'y=([\-0-9]+)', line)[0])
        z = int(re.findall(r'z=([\-0-9]+)', line)[0])
        moons.append([[x, 0], [y, 0], [z, 0]])

    for _ in range(1000):
        gravity = [[0, 0, 0] for _ in range(len(moons))]

        for m1, m2 in combinations(moons, 2):
            for p1, p2 in zip(m1, m2):
                if p1[0] < p2[0]:
                    p1[1] += 1
                    p2[1] -= 1
                elif p1[0] > p2[0]:
                    p1[1] -= 1
                    p2[1] += 1

        energy = 0
        for moon in moons:
            for p in moon:
                p[0] += p[1]
            ep = sum((abs(p[0]) for p in moon))
            ek = sum((abs(p[1]) for p in moon))
            energy += ep * ek

    print(energy)
