"""Exam 0."""
import math

def find_capital_letters(string1: str):
    """Find all capital letters."""
    result = ""
    for letter in string1:
        if letter.isupper():
            result += letter
    return result


def close_far(a: int, b: int, c: int):
    """Return true if one number is near and other is far."""
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 or abs(b - c) >= 2:
            return True
    elif abs(a - c) <= 1:
        if abs(a - b) >= 2 or abs(c - b) >= 2:
            return True


if __name__ == '__main__':
    print(find_capital_letters("SasSHa"))
