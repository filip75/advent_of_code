from collections import defaultdict

from aoc import *


def get_data() -> tuple[list[str], str, str, dict[str, str]]:
    data = read_file(14)
    polymer_input, rules_input = data.split("\n\n")
    pairs = defaultdict(lambda: 0)
    rules = {}
    start, end = polymer_input[0], polymer_input[-1]

    for i in range(len(polymer_input) - 1):
        pairs[polymer_input[i : i + 2]] += 1

    for rule in rules_input.split("\n"):
        a, b = rule.split(" -> ")
        rules[a] = b

    return pairs, start, end, rules


def first() -> int:
    pairs, start, end, rules = get_data()

    for _ in range(10):
        to_add = defaultdict(lambda: 0)

        for pair, insertion in rules.items():
            if pair in pairs:
                to_add[pair] -= pairs[pair]
                to_add[pair[0] + insertion] += pairs[pair]
                to_add[insertion + pair[1]] += pairs[pair]

        for k, v in to_add.items():
            pairs[k] += v

        pairs = defaultdict(lambda: 0, {k: v for k, v in pairs.items() if v != 0})

    letter_count = defaultdict(lambda: 0)
    for k, v in pairs.items():
        letter_count[k[0]] += v
        letter_count[k[1]] += v
    letter_count[start] += 1
    letter_count[end] += 1

    c = sorted(letter_count.values())
    return (c[-1] - c[0]) // 2


def second() -> int:
    pairs, start, end, rules = get_data()

    for _ in range(40):
        to_add = defaultdict(lambda: 0)

        for pair, insertion in rules.items():
            if pair in pairs:
                to_add[pair] -= pairs[pair]
                to_add[pair[0] + insertion] += pairs[pair]
                to_add[insertion + pair[1]] += pairs[pair]

        for k, v in to_add.items():
            pairs[k] += v

        pairs = defaultdict(lambda: 0, {k: v for k, v in pairs.items() if v != 0})

    letter_count = defaultdict(lambda: 0)
    for k, v in pairs.items():
        letter_count[k[0]] += v
        letter_count[k[1]] += v
    letter_count[start] += 1
    letter_count[end] += 1

    c = sorted(letter_count.values())
    return (c[-1] - c[0]) // 2
