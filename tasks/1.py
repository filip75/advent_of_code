from input_utils import read_list


def prepare_input() -> list[int]:
    return read_list(1, int)


def first() -> int:
    values = prepare_input()
    return sum(1 for i in range(len(values) - 1) if values[i] < values[i + 1])


def second() -> int:
    values = prepare_input()
    windows = [sum(values[i : i + 3]) for i in range(len(values) - 2)]
    return sum(1 for i in range(len(windows) - 1) if windows[i] < windows[i + 1])
