from collections import defaultdict

from aoc import *


def get_data() -> dict[str, list[str]]:
    data = read_list(12)
    caves = defaultdict(list)
    for connection in data:
        s, e = connection.split("-")
        caves[s].append(e)
        caves[e].append(s)

    return caves


def first() -> int:
    caves = get_data()
    paths = [["start"]]

    n = 0
    while paths:
        path = paths.pop()
        adjecents = caves[path[-1]]
        for a in adjecents:
            if a == "end":
                n += 1
            elif a.isupper() or (a.islower() and not a in path):
                paths.append(path + [a])

    return n


def second() -> int:
    caves = get_data()
    paths = [(["start"], False)]

    n = 0
    while paths:
        path, is_twice = paths.pop()
        adjecents = caves[path[-1]]
        for a in adjecents:
            if a == "end":
                n += 1
            elif a.isupper():
                paths.append((path + [a], is_twice))
            elif a != "start" and a.islower():
                if a not in path:
                    paths.append((path + [a], is_twice))
                elif not is_twice and sum(c == a for c in path) == 1:
                    paths.append((path + [a], True))

    return n
