from aoc import *

OPENINGS = ["(", "[", "{", "<"]
CLOSINGS = [")", "]", "}", ">"]
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORES2 = {")": 1, "]": 2, "}": 3, ">": 4}


def get_data() -> list:
    data = read_list(10)

    return data


def first() -> int:
    data = get_data()

    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in OPENINGS:
                stack.append(c)
            elif c in CLOSINGS:
                if c == CLOSINGS[OPENINGS.index(stack[-1])]:
                    stack.pop(-1)
                else:
                    score += SCORES[c]
                    break

    return score


def second() -> int:
    data = get_data()

    scores = []
    for line in data:
        corrupted = False
        stack = []
        for c in line:
            if c in OPENINGS:
                stack.append(c)
            elif c in CLOSINGS:
                if c == CLOSINGS[OPENINGS.index(stack[-1])]:
                    stack.pop(-1)
                else:
                    corrupted = True
                    break

        if not corrupted:
            scores.append(0)

            for c in reversed(stack):
                scores[-1] *= 5
                scores[-1] += SCORES2[CLOSINGS[OPENINGS.index(c)]]

    return sorted(scores)[len(scores) // 2]
