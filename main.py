from argparse import ArgumentParser
from importlib import import_module
from os.path import join


def main(day: str, only_first: bool) -> None:
    module = import_module(f"tasks.{day}")
    first = getattr(module, "first")
    second = getattr(module, "second")

    print(first())
    if not only_first:
        print(second())


def parse_arguments() -> dict:
    parser = ArgumentParser()
    parser.add_argument("--day", type=str, required=True)
    parser.add_argument("-f", dest="only_first", action="store_true")
    args = parser.parse_args()
    return args.__dict__


if __name__ == "__main__":
    parameters = parse_arguments()
    main(**parameters)
