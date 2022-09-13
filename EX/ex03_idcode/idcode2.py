"""EX03 ID code."""


def is_valid_gender_number(gender_number: int):
    """Check if given value is correct for gender number in ID code."""
    if gender_number < 1 or gender_number > 6:
        return False
    else:
        return True


def get_gender(gender_number: int):
    """Determines if gender is male or female."""
    modulo = gender_number % 2
    if modulo != 0:
        return "male"
    else:
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if -1 < year_number < 100:
        return True
    return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    if 0 < month_number < 13:
        return True
    return False


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if 0 < birth_number < 1000:
        return True
    return False


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
