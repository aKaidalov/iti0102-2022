"""Exam 0."""
from typing import Optional


def find_capital_letters(string1: str):
    """Find all capital letters."""
    result = ""
    for letter in string1:
        if letter.isupper():
            result += letter
    return result


def close_far(a: int, b: int, c: int):
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    elif abs(a - c) <= 1 and abs(a - b) >= 2 and abs(c - b) >= 2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(find_capital_letters("SasSHa"))
    print(close_far(1, 2, 3))
