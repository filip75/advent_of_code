from typing import List


def is_immediate(modes: str, position: int) -> bool:
    return modes[-1 - position:-2 - position:-1] == '1'


def get_value(memory: List[int], pointer: int, position: int) -> int:
    modes = str(memory[pointer])[:-2]
    if is_immediate(modes, position):
        return memory[pointer + 1 + position]
    else:
        return memory[memory[pointer + 1 + position]]


def find(memory: List[int], inp: int) -> None:
    pointer = 0
    while True:
        op_code = str(memory[pointer])
        instruction = int(op_code[-2:])
        if instruction == 1:
            memory[memory[pointer + 3]] = \
                get_value(memory, pointer, 0) + get_value(memory, pointer, 1)
            pointer += 4
        elif instruction == 2:
            memory[memory[pointer + 3]] = \
                get_value(memory, pointer, 0) * get_value(memory, pointer, 1)
            pointer += 4
        elif instruction == 3:
            memory[memory[pointer + 1]] = inp
            pointer += 2
        elif instruction == 4:
            print(get_value(memory, pointer, 0))
            pointer += 2
        elif instruction == 5:
            if get_value(memory, pointer, 0) != 0:
                pointer = get_value(memory, pointer, 1)
            else:
                pointer += 3
        elif instruction == 6:
            if get_value(memory, pointer, 0) == 0:
                pointer = get_value(memory, pointer, 1)
            else:
                pointer += 3
        elif instruction == 7:
            if get_value(memory, pointer, 0) < get_value(memory, pointer, 1):
                memory[memory[pointer + 3]] = 1
            else:
                memory[memory[pointer + 3]] = 0
            pointer += 4
        elif instruction == 8:
            if get_value(memory, pointer, 0) == get_value(memory, pointer, 1):
                memory[memory[pointer + 3]] = 1
            else:
                memory[memory[pointer + 3]] = 0
            pointer += 4
        elif instruction == 99:
            break


with open("input.txt") as file:
    code = [int(x) for x in file.readline().split(',')]

find(code, 5)
