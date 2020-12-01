from itertools import combinations

with open("1.input") as file:
    numbers = [int(n) for n in file.readlines()]

for combination in combinations(numbers, 3):
    if sum(combination) == 2020:
        r = 1
        for n in combination:
            r *= n
        print(r)