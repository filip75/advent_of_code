from dataclasses import dataclass
from itertools import product
from os.path import join
from typing import Callable, Iterator, Optional


def get_file_path(day: int) -> str:
    return join("tasks", "data", str(day))


def read_list(
    day: int, cast_function: Optional[Callable] = None, separtor: str = "\n"
) -> list:
    cast = cast_function or (lambda x: x)
    with open(get_file_path(day)) as file:
        return [cast(line) for line in file.read().strip().split(separtor)]


def cast_list(values: list, function: Callable) -> list:
    return [function(element) for element in values]


@dataclass
class Point:
    x: int
    y: int


class Map:
    DIFS = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    DIAGONAL_DIFS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def __init__(self, data: list[list[any]]) -> None:
        self.data = data
        self.width = len(data[0])
        self.height = len(data)

    def get_adjacent(self, point: Point, include_diagonal: bool = True) -> list[Point]:
        points = []
        for dif in self.DIFS + (self.DIAGONAL_DIFS if include_diagonal else []):
            if (
                0 <= point.x + dif[0] < self.height
                and 0 <= point.y + dif[1] < self.width
            ):
                points.append(Point(point.x + dif[0], point.y + dif[1]))
        return points

    def __iter__(self) -> Iterator[Point]:
        return (Point(x, y) for x, y in product(range(self.height), range(self.width)))

    def __getitem__(self, key: Point) -> any:
        return self.data[key.x][key.y]

    def __setitem__(self, key: Point, value: any) -> None:
        self.data[key.x][key.y] = value

    def __str__(self) -> str:
        return str("\n".join(([str(line) for line in self.data])))
