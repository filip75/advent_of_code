from aoc import *


def prepare_input() -> list:
    return read_list(3)


def first() -> int:
    values = prepare_input()

    gamma = [
        "1" if sum(int(bit) for bit in bits) > len(values) // 2 else "0"
        for bits in zip(*values)
    ]
    espilon = [
        "0" if sum(int(bit) for bit in bits) > len(values) // 2 else "1"
        for bits in zip(*values)
    ]

    return int("".join(gamma), base=2) * int("".join(espilon), base=2)


def most(values, bit):
    s = sum(int(value[bit]) for value in values)
    s = 1 if s >= len(values) // 2 else 0

    oxygen_values = [v for v in values if int(v[bit]) == s]
    return oxygen_values


def least(values, bit):
    s = sum(int(value[bit]) for value in values)
    s = 0 if s >= len(values) // 2 else 1

    oxygen_values = [v for v in values if int(v[bit]) == s]
    return oxygen_values


def second() -> int:
    values = prepare_input()

    oxygen_values = values[:]
    for i in range(len(oxygen_values[0])):
        if len(oxygen_values) == 1:
            break
        oxygen_values = most(oxygen_values, i)

    co2_values = values[:]
    for i in range(len(co2_values[0])):
        if len(co2_values) == 1:
            break
        co2_values = least(co2_values, i)

    return int(oxygen_values[0], base=2) * int(co2_values[0], base=2)
