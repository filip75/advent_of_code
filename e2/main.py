from typing import List


def find(memory: List[int], noun: int, verb: int) -> int:
    memory[1] = noun
    memory[2] = verb

    pointer = 0
    while True:
        op_code = memory[pointer]
        if op_code == 1:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
        elif op_code == 2:
            memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
        elif op_code == 99:
            break
        pointer += 4

    return memory[0]


with open("input.txt") as file:
    code = [int(x) for x in file.read().split(',')]

for n in range(100):
    for v in range(100):
        if find(code[:], n, v) == 19690720:
            print(100 * n + v)
