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
        if 11 <= birth_number <= 20 or 271 <= birth_number <= 370:
            return "Tartu"
        if 21 <= birth_number <= 220 or 471 <= birth_number <= 710:
            return "Tallinn"
        if 221 <= birth_number <= 270:
            return "Kohtla-Järve"
        if 371 <= birth_number <= 420:
            return "Narva"
        if 421 <= birth_number <= 470:
            return "Pärnu"
        if 711 <= birth_number <= 999:
            return "undefined"
    else:
        return "Wrong input!"


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    sum_of_seven2, sum_of_ten_numbers2, sum_of_three2 = 0, 0, 0
    if the_first_control_number_algorithm(id_code) == "Incorrect ID code!":
        return False
    elif the_first_control_number_algorithm(id_code) == "Needs the second algorithm!":
        for i in range(3, 10):
            sum_of_seven2 += int(id_code[i]) * i       # multiplies with its corresponding digit (until 7 digits)
            if i == 9:
                for iteration in range(1, 4):
                    sum_of_three2 += int(id_code[iteration])     # multiplies last 3 digits
        sum_of_ten_numbers2 = sum_of_seven2 + sum_of_three2
        remainder2 = sum_of_ten_numbers2 % 11
        if remainder2 < 10 and remainder2 == int(id_code[10]):
            return True
        else:
            return False
    else:
        return True


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    # Write your code here


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    # Write your code here


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    # Write your code here


if __name__ == '__main__':
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6
    print(is_valid_control_number("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm!"50205160274

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
