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
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("123456789123456789"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(the_first_control_number_algorithm("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm!"

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
