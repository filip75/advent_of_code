from collections import defaultdict
from itertools import product

from aoc import *


def get_data() -> tuple:
    data = read_file(17).strip("target area: ").split(",")
    x_input = tuple(map(int, data[0].strip()[2:].split("..")))
    y_input = tuple(map(int, data[1].strip()[2:].split("..")))

    return x_input, y_input


def first() -> int:
    _, y_bound = get_data()

    v = -y_bound[0] - 1

    return ((v + 1) * v) // 2


def second() -> int:
    x_bound, y_bound = get_data()

    time = 0
    x_times = defaultdict(list)
    x_stop_times = defaultdict(list)
    for v_x in range(1, x_bound[1] + 1):
        v_x_copy = v_x
        stop_time = 0
        time = 0
        while stop_time < x_bound[1] and v_x_copy != 0:
            stop_time += v_x_copy
            v_x_copy = max(0, v_x_copy - 1)
            time += 1
            if x_bound[0] <= stop_time <= x_bound[1]:
                if v_x_copy == 0:
                    x_stop_times[time].append(v_x)
                else:
                    x_times[time].append(v_x)

    y_times = defaultdict(list)
    for v_y in range(y_bound[0], -y_bound[0] + 1):
        y = 0
        time = 0
        v_y_copy = v_y
        while y >= y_bound[0]:
            if y <= y_bound[1]:
                y_times[time].append(v_y)
            y += v_y_copy
            v_y_copy -= 1
            time += 1

    pairs = set()

    for time, speeds in y_times.items():
        if time in x_times:
            pairs |= set(product(speeds, x_times[time]))
        for stop_time, stop_speeds in x_stop_times.items():
            if time >= stop_time:
                pairs |= set(product(speeds, stop_speeds))

    return len(list(pairs))
