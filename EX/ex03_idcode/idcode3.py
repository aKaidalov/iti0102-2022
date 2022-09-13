"""EX03 ID code."""


def is_leap_year(year_number: int):
    """Define the leap year."""
    if year_number % 400 == 0:
        return True
    if year_number % 4 == 0 and not year_number % 100 == 0:
        return True
    if year_number % 100 == 0 and year_number % 400 != 0:
        return False
    return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    if gender_number == 1 or gender_number == 2:
        return 1800 + year_number
    if gender_number == 3 or gender_number == 4:
        return 1900 + year_number
    if gender_number == 5 or gender_number == 6:
        return 2000 + year_number



def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if is_valid_birth_number(birth_number) is True:
        if 1 <= birth_number <= 10:
            return "Kuressaare"
        if 11 <= birth_number <= 20:
            return "Tartu"
        if 21 <= birth_number <= 220:
            return "Tallinn"
        if 221 <= birth_number <= 270:
            return "Kohtla-Jarve"
        if 271 <= birth_number <= 370:
            return "Tartu"
        if 371 <= birth_number <= 420:
            return "Narva"
        if 421 <= birth_number <= 470:
            return "Parnu"
        if 471 <= birth_number <= 710:
            return "Tallinn"
        if 711 <= birth_number <= 999:
            return "undefined"
    else:
        return "Wrong input!"


if __name__ == '__main__':
    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"