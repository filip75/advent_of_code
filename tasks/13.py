from aoc import *


def get_data() -> tuple[set[tuple[int, int]], list[tuple[int, int]]]:
    data = read_file(13)
    dots_input, folds_input = data.split("\n\n")
    dots = set()
    folds = []

    for dot in dots_input.split("\n"):
        dots.add(tuple(map(int, dot.split(","))))
    for fold in folds_input.split("\n"):
        axis, value = fold.split(" ")[2].split("=")
        folds.append((axis, int(value)))

    return dots, folds


def first() -> int:
    dots, folds = get_data()

    fold = folds[0]
    fold_axis = 1 if fold[0] == "y" else 0
    to_add = set()
    to_remove = set()

    for dot in dots:
        if dot[fold_axis] > fold[1]:
            to_remove.add(dot)
            if fold[0] == "y":
                to_add.add((dot[0], fold[1] - (dot[1] - fold[1])))
            else:
                to_add.add((fold[1] - (dot[0] - fold[1]), dot[1]))

    dots = dots - to_remove | to_add

    return len(dots)


def print_paper(dots: set[tuple[int, int]]) -> None:
    width, height = max(x[0] for x in dots), max(x[1] for x in dots)
    result = [[" "] * (width + 1) for _ in range(height + 1)]
    for dot in dots:
        result[dot[1]][dot[0]] = "x"
    print("\n".join([str(x) for x in result]))


def second() -> int:
    dots, folds = get_data()

    for fold in folds:
        fold_axis = 1 if fold[0] == "y" else 0
        to_add = set()
        to_remove = set()

        for dot in dots:
            if dot[fold_axis] > fold[1]:
                to_remove.add(dot)
                if fold[0] == "y":
                    to_add.add((dot[0], fold[1] - (dot[1] - fold[1])))
                else:
                    to_add.add((fold[1] - (dot[0] - fold[1]), dot[1]))

        dots = dots - to_remove | to_add

    print_paper(dots)

    return len(dots)
