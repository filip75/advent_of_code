from itertools import cycle
from typing import List, Generator


def compute_element(s: List[int], p: Generator[int, None, None]) -> int:
    c = cycle(p)
    next(c)
    return abs(sum([a * b for a, b in zip(s, c)])) % 10


def alter_pattern(s: List[int], step: int) -> Generator[int, None, None]:
    return (e for element in s for e in [element] * step)


def compute_phase(s: List[int], p: List[int]) -> List[int]:
    return [compute_element(s, alter_pattern(p, i)) for i in range(1, len(s) + 1)]


with open("input.txt") as file:
    signal = [int(x) for x in file.read()]
    pattern = [0, 1, 0, -1]
    for _ in range(100):
        signal = [
            compute_element(signal, alter_pattern(pattern, i))
            for i in range(1, len(signal) + 1)
        ]

    print("".join(str(d) for d in signal)[:8])
