from typing import List

from e5.main import IntCode

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
ROTATE_RIGHT = 1
ROTATE_LEFT = 0
WHITE = 1
BLACK = 0


class Robot:
    def __init__(self, code: List[int]):
        self.ic = IntCode(code)
        self.position = (0, 0)
        self.orientation = 0
        self.hull = {}

    def reset(self):
        self.position = (0, 0)
        self.orientation = 0
        self.hull = {}
        self.ic.reset()

    def print(self):
        width = max([x[0] for x in self.hull])
        height = max([x[1] for x in self.hull])

        for j in range(-1, height + 2):
            for i in range(width):
                colour = self.hull.get((i, j), BLACK)
                if colour == BLACK:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()

    def rotate(self, direction: int):
        if direction == ROTATE_RIGHT:
            self.orientation = (self.orientation + 1) % 4
        elif direction == ROTATE_LEFT:
            self.orientation = (self.orientation - 1) % 4

    def move_forward(self):
        self.position = (self.position[0] + DIRECTIONS[self.orientation][0],
                         self.position[1] + DIRECTIONS[self.orientation][1])

    def get_colour(self):
        if self.position in self.hull:
            return self.hull[self.position]
        return BLACK

    def make_step(self):
        new_colour = self.ic.run([self.get_colour()])
        if new_colour is None:
            return False
        direction = self.ic.run([])
        if direction is None:
            return False
        self.hull[self.position] = new_colour
        self.rotate(direction)
        self.move_forward()
        return True

    def work(self):
        work_finished = False
        while not work_finished:
            work_finished = not self.make_step()


if __name__ == '__main__':
    with open("input.txt") as file:
        code = [int(x) for x in file.readline().split(',')]

        robot = Robot(code)
        robot.work()
        print(len(robot.hull))

        robot.reset()
        robot.hull[(0, 0)] = WHITE
        robot.work()
        robot.print()
