from aoc import *


def get_data() -> list:
    data = read_list(6, separtor=",", cast_function=int)

    return data


def first() -> int:
    data = get_data()
    n = []
    for _ in range(80):
        for i in range(len(data)):
            data[i] -= 1
            if data[i] == -1:
                data[i] = 6
                n.append(8)
        data.extend(n)
        n = []

    return len(data)


def second() -> int:
    data = get_data()

    fish = [0] * 9
    for d in data:
        fish[d] += 1

    for _ in range(256):
        to_add = fish[0]
        fish[0] = 0
        for idx, c in enumerate(fish[0:]):
            fish[idx - 1] = c
        fish[6] += to_add
        fish[8] = to_add

    return sum(fish)
