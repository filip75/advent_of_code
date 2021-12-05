from aoc import read_list


def first() -> int:
    values = prepare_input()
    depth, position = 0, 0
    for op, arg in values:
        if op == "forward":
            position += arg
        elif op == "up":
            depth -= arg
        elif op == "down":
            depth += arg

    return depth * position


def second() -> int:
    values = prepare_input()
    depth, position, aim = 0, 0, 0
    for op, arg in values:
        if op == "forward":
            position += arg
            depth += arg * aim
        elif op == "up":
            aim -= arg
        elif op == "down":
            aim += arg

    return depth * position


def prepare_input() -> list[tuple[str, int]]:
    values = read_list(2)
    result = []
    for line in values:
        args = line.split()
        result.append((args[0], int(args[1])))
    return result
