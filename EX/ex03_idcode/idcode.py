"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """Find ID-code from given text."""
    # "0123456789" = 48 - 57 ASCII
    new_text: str = ""
    counter = 0
    for element in text:
        new_element = ord(element)  # Gives an integer meaning from ASCII
        if 47 < new_element:        # Controls if new_element is from 0 to 9
            if new_element < 58:
                new_text += element  # If element suits to program than it gives element's meaning to the new variable
                counter += 1
    if counter > 11:
        return "Too many numbers!"
    elif counter < 11:
        return "Not enough numbers!"
    else:
        return new_text


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    new_text: str = ""
    counter, sum_of_nine, sum_of_ten_numbers = 0, 0, 0
    for element in text:
        new_element = ord(element)
        if 47 < new_element:
            if new_element < 58:
                new_text += element
                counter += 1
    if counter > 11:
        return "Incorrect ID code!"
    elif counter < 11:
        return "Incorrect ID code!"
    else:
        for i in range(9):
            sum_of_nine += int(new_text[i]) * (i + 1)       # multiplies with its corresponding digit (until 9 digits)
            if i == 8:
                sum_of_ten_numbers = sum_of_nine + int(new_text[9])     # multiplies with its 10th digit

        remainder = sum_of_ten_numbers % 11
        if remainder < 10:
            if remainder == int(new_text[10]):
                return new_text
            else:
                return "Incorrect ID code!"
        else:
            return "Needs the second algorithm!"


# --------------------------------------------------------------------------------------


def is_valid_gender_number(gender_number: int):
    """Check if given value is correct for gender number in ID code."""
    if gender_number < 1 or gender_number > 6:
        return False
    else:
        return True


def get_gender(gender_number: int):
    """Determine if gender is male or female."""
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


# --------------------------------------------------------------------------------------


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
