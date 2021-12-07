from aoc import *


def get_data() -> list:
    data = read_list(7, cast_function=int, separtor=",")

    return data


def first() -> int:
    data = get_data()

    return min(sum(abs(p - i) for p in data) for i in range(min(data), max(data) + 1))


def eval_fuel(a: int) -> int:
    return int((1 + a) / 2 * a)


def second() -> int:
    data = get_data()

    return min(
        sum(eval_fuel(abs(p - i)) for p in data)
        for i in range(min(data), max(data) + 1)
    )
