from typing import List, Optional

POSITION_MODE = '0'
IMMEDIATE_MODE = '1'
RELATIVE_MODE = '2'


class IntCode:
    def __init__(self, memory: List[int]):
        self.start_memory = memory[:] + [0] * 10000
        self.memory = self.start_memory[:]
        self.pointer = 0
        self.relative_base = 0

    def reset(self):
        self.memory = self.start_memory[:]
        self.pointer = 0
        self.relative_base = 0

    def get_mode(self, position: int) -> str:
        return str(self.memory[self.pointer])[:-2][-1 - position:-2 - position:-1]

    def get_value(self, position: int) -> int:
        return self.memory[self.get_address(position)]

    def get_address(self, position: int):
        mode = self.get_mode(position)
        if mode == IMMEDIATE_MODE:
            return self.pointer + 1 + position
        elif mode == RELATIVE_MODE:
            return self.relative_base + self.memory[self.pointer + 1 + position]
        else:
            return self.memory[self.pointer + 1 + position]

    def run(self, inp: List[int]) -> Optional[int]:
        while True:
            op_code = str(self.memory[self.pointer])
            instruction = int(op_code[-2:])
            if instruction == 1:
                self.memory[self.get_address(2)] = self.get_value(0) + self.get_value(1)
                self.pointer += 4
            elif instruction == 2:
                self.memory[self.get_address(2)] = self.get_value(0) * self.get_value(1)
                self.pointer += 4
            elif instruction == 3:
                if inp:
                    self.memory[self.get_address(0)] = inp.pop(0)
                    self.pointer += 2
                else:
                    return
            elif instruction == 4:
                v = self.get_value(0)
                self.pointer += 2
                return v
            elif instruction == 5:
                if self.get_value(0) != 0:
                    self.pointer = self.get_value(1)
                else:
                    self.pointer += 3
            elif instruction == 6:
                if self.get_value(0) == 0:
                    self.pointer = self.get_value(1)
                else:
                    self.pointer += 3
            elif instruction == 7:
                if self.get_value(0) < self.get_value(1):
                    self.memory[self.get_address(2)] = 1
                else:
                    self.memory[self.get_address(2)] = 0
                self.pointer += 4
            elif instruction == 8:
                if self.get_value(0) == self.get_value(1):
                    self.memory[self.get_address(2)] = 1
                else:
                    self.memory[self.get_address(2)] = 0
                self.pointer += 4
            elif instruction == 9:
                self.relative_base += self.get_value(0)
                self.pointer += 2
            elif instruction == 99:
                self.pointer += 1
                return None


if __name__ == '__main__':
    with open("input.txt") as file:
        code = [int(x) for x in file.readline().split(',')]

    ic = IntCode(code)
    print(ic.run([5]))
