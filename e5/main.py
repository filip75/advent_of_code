from typing import List, Optional


class IntCode:
    def __init__(self, memory: List[int]):
        self.start_memory = memory[:]
        self.memory = memory[:]
        self.pointer = 0

    def reset(self):
        self.memory = self.start_memory[:]
        self.pointer = 0

    @staticmethod
    def is_immediate(modes: str, position: int) -> bool:
        return modes[-1 - position:-2 - position:-1] == '1'

    def get_value(self, position: int) -> int:
        modes = str(self.memory[self.pointer])[:-2]
        if self.is_immediate(modes, position):
            return self.memory[self.pointer + 1 + position]
        else:
            return self.memory[self.memory[self.pointer + 1 + position]]

    def run(self, inp: int) -> Optional[int]:
        while True:
            op_code = str(self.memory[self.pointer])
            instruction = int(op_code[-2:])
            if instruction == 1:
                self.memory[self.memory[self.pointer + 3]] = self.get_value(0) + self.get_value(1)
                self.pointer += 4
            elif instruction == 2:
                self.memory[self.memory[self.pointer + 3]] = self.get_value(0) * self.get_value(1)
                self.pointer += 4
            elif instruction == 3:
                if inp is not None:
                    self.memory[self.memory[self.pointer + 1]] = inp
                    inp = None
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
                    self.memory[self.memory[self.pointer + 3]] = 1
                else:
                    self.memory[self.memory[self.pointer + 3]] = 0
                self.pointer += 4
            elif instruction == 8:
                if self.get_value(0) == self.get_value(1):
                    self.memory[self.memory[self.pointer + 3]] = 1
                else:
                    self.memory[self.memory[self.pointer + 3]] = 0
                self.pointer += 4
            elif instruction == 99:
                self.pointer += 1
                return None


if __name__ == '__main__':
    with open("input.txt") as file:
        code = [int(x) for x in file.readline().split(',')]

    ic = IntCode(code)
    print(ic.run(5))
