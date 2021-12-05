from typing import Callable, Optional
from dataclasses import dataclass
from os.path import join


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