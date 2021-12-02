def get_row(seat: str) -> int:
    binary = seat[:7].replace("F", "0").replace("B", "1")
    return int(binary, base=2)


def get_column(seat: str) -> int:
    binary = seat[-3:].replace("L", "0").replace("R", "1")
    return int(binary, base=2)


with open("5.input") as file:
    seats = [l.strip() for l in file.readlines()]

max_ = 0
for seat in seats:
    if (m := get_row(seat) * 8 + get_column(seat)) > max_:
        max_ = m
print(max_)

ids = set()
for seat in seats:
    ids.add(get_row(seat) * 8 + get_column(seat))
for i in range(min(ids) + 1, max(ids)):
    if i not in ids and i - 1 in ids and i + 1 in ids:
        print(i)
