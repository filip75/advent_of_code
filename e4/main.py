from typing import List


def get_digit(n: int, digit: int) -> int:
    return int((n % 10 ** (digit + 1)) / (10 ** digit))


def check(n: int) -> bool:
    if n < 0 or n > 999999:
        return False
    digits = [get_digit(n, d) for d in range(6)]
    double_digits = False

    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            return False
        if digits[i] == digits[i + 1]:
            if not (i + 2 < len(digits) and digits[i + 2] == digits[i]):
                if not (i - 1 >= 0 and digits[i - 1] == digits[i]):
                    double_digits = True

    return double_digits


def find_possible(low: int, high: int) -> List[int]:
    return [i for i in range(low, high + 1) if check(i)]


print(len(find_possible(172851, 675869)))
