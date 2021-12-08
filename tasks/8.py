from aoc import *


def get_data() -> list:
    data = read_list(8)
    lines = []
    for d in data:
        line = d.split("|")
        lines.append((line[0].strip().split(" "), line[1].strip().split(" ")))

    return lines


def first() -> int:
    lines = get_data()

    return sum(1 for line in lines for o in line[1] if len(o) in (2, 3, 4, 7))


def second() -> int:
    lines = get_data()
    a = 0
    for line in lines:
        inputs, outputs = line

        cf = None
        bd = None

        one = None
        four = None
        seven = None

        for e in inputs:
            if len(e) == 2:
                one = e
            elif len(e) == 4:
                four = e
            elif len(e) == 3:
                seven = e
            if all((one, four, seven)):
                break

        cf = set(seven).intersection(set(one))
        bd = set(four) - set(one)

        result = 0
        base = 1000
        for e in outputs:
            has_cf = all(c in e for c in cf)
            has_bd = all(c in e for c in bd)

            if len(e) == 2:
                result += base
            elif not has_cf and not has_bd and len(e) == 5:
                result += 2 * base
            elif has_cf and not has_bd and len(e) == 5:
                result += 3 * base
            elif len(e) == 4:
                result += 4 * base
            elif not has_cf and has_bd and len(e) == 5:
                result += 5 * base
            elif not has_cf and has_bd and len(e) == 6:
                result += 6 * base
            elif len(e) == 3:
                result += 7 * base
            elif len(e) == 7:
                result += 8 * base
            elif has_cf and has_bd and len(e) == 6:
                result += 9 * base
            base /= 10

        a += int(result)

    return a
