from e5.main import IntCode

if __name__ == "__main__":
    with open("input.txt") as file:
        code = [int(x) for x in file.readline().split(",")]

    ic = IntCode(code)
    print(ic.run([1]))
    ic.reset()
    print(ic.run([2]))
