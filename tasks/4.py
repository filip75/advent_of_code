from input_utils import *
from itertools import product

EMPTY = "x"


def get_data() -> tuple[list, list]:
    data = read_list(4)
    calls = (int(d) for d in data[0].split(","))
    boards = []
    for idx, line in enumerate(data[1:]):
        if idx % 6 == 0:
            boards.append([])
            continue
        boards[-1].append([int(d) for d in line.split()])

    return calls, boards


def is_board_complete(board: list[list[int]]) -> bool:
    for row in board:
        if all(element == EMPTY for element in row):
            return True

    for column in range(5):
        if all(
            element == EMPTY for element in (board[row][column] for row in range(5))
        ):
            return True

    return False


def board_sum(board: list[list[int]]) -> int:
    return sum(sum(element for element in row if element != EMPTY) for row in board)


def first() -> int:
    calls, boards = get_data()

    for call in calls:
        for i, j in product(range(5), range(5)):
            for board in boards:
                if board[i][j] == call:
                    board[i][j] = EMPTY

                if is_board_complete(board):
                    return board_sum(board) * call


def second() -> int:
    calls, boards = get_data()
    for call in calls:

        not_complete = []

        for grid in boards:
            for i, j in product(range(5), range(5)):
                if grid[i][j] == call:
                    grid[i][j] = EMPTY

            if not is_board_complete(grid):
                not_complete.append(grid)

        if len(not_complete) == 0:
            return board_sum(boards[0]) * call
        boards = not_complete
