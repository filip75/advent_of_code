from itertools import combinations

with open("1.input") as file:
    numbers = [int(n) for n in file.readlines()]


def find(numbers, count):
    for combination in combinations(numbers, count):
        if sum(combination) == 2020:
            r = 1
            for n in combination:
                r *= n
            return r


print(find(numbers, 2))
print(find(numbers, 3))
