"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """Find ID-code from given text."""
    # "0123456789" = 48 - 57 ASCII
    new_text: str = ""
    counter = 0
    for element in text:
        new_element = ord(element)  # Gives an integer meaning from ASCII
        if 47 < new_element:  # Controls if new_element is from 0 to 9
            if new_element < 58:
                new_text += element  # If element suits to program than it gives element's meaning to the new variable
                counter += 1
    if counter > 11:
        return "Too many numbers!"
    elif counter < 11:
        return "Not enough numbers!"
    else:
        return new_text


# Sledujushuju funktsiju mozno b6lob6 cokratit', isspolzovav pervuju
def the_first_control_number_algorithm(text: str) -> str:
    """Check if given value is correct for control number in ID code only with the first algorithm."""
    new_text: str = ""
    counter, sum_of_nine, sum_of_ten_numbers = 0, 0, 0
    for element in text:
        new_element = ord(element)
        if 47 < new_element < 58:
            new_text += element
            counter += 1
    if counter == 11:
        for i in range(9):
            sum_of_nine += int(new_text[i]) * (i + 1)  # multiplies with its corresponding digit (until 9 digits)
            if i == 8:
                sum_of_ten_numbers = sum_of_nine + int(new_text[9])  # multiplies with its 10th digit

        remainder = sum_of_ten_numbers % 11
        if remainder < 10:
            if remainder == int(new_text[10]):
                return new_text
            else:
                return "Incorrect ID code!"
        else:
            return "Needs the second algorithm!"
    else:
        return "Incorrect ID code!"


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
    if is_valid_birth_number(birth_number):
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


# --------------------------------------------------------------------------------------


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    sum_of_seven2, sum_of_ten_numbers2, sum_of_three2 = 0, 0, 0
    if the_first_control_number_algorithm(id_code) == "Incorrect ID code!":
        return False
    elif the_first_control_number_algorithm(id_code) == "Needs the second algorithm!":
        for i in range(7):
            sum_of_seven2 += int(id_code[i + 3]) * (i + 3)  # multiplies with its corresponding digit (until 7 digits)
            if i == 9:
                for iteration in range(7, 10):
                    sum_of_three2 += int(id_code[iteration - 6]) * (iteration - 6)  # multiplies last 3 digits
        sum_of_ten_numbers2 = sum_of_seven2 + sum_of_three2
        control_number = sum_of_ten_numbers2 % 11
        if control_number >= 10:
            control_number = 0
        if control_number == int(id_code[10]):
            return True
        else:
            return False
    else:
        return True


# Mb gde to zdes' oshibka
def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    if is_valid_gender_number(gender_number) and is_valid_year_number(year_number) and is_valid_month_number(month_number):
        # Previous line checks if all the numbers are correct.
        days_in_month_31 = [1, 3, 5, 7, 8, 10, 12]
        days_in_month_30 = [4, 6, 9, 11]
        for element in range(len(days_in_month_31)):
            if month_number == days_in_month_31[element] and 0 < day_number < 32:
                return True
        for element in range(len(days_in_month_30)):
            if month_number == days_in_month_30[element] and 0 < day_number < 31:
                return True
        year_in_4_numbers = get_full_year(gender_number, year_number)
        if is_leap_year(year_in_4_numbers) and 0 < day_number < 30:
            return True
        else:
            if 0 < day_number < 29:
                return True
            return False
    else:
        return False


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    if is_valid_control_number(id_code):
        year_number, month_number, day_number, gender_number = "", "", "", 0
        for index in range(len(id_code)):
            if index == 0:
                gender_number = int(id_code[index])
            if index == 1 or index == 2:
                year_number += id_code[index]
            if index == 3 or index == 4:
                month_number += id_code[index]
            if index == 5 or index == 6:
                day_number += id_code[index]
        year_number = int(year_number)
        month_number = int(month_number)
        day_number = int(day_number)
        if is_valid_day_number(gender_number, year_number, month_number, day_number):
            return True
        else:
            return False
    else:
        return False


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    if is_id_valid(id_code):
        year_number, month_number, day_number, birth_number, gender_number, gender, location = "", "", "", "", 0, "", ""
        for index in range(len(id_code)):
            if index == 0:
                gender_number = int(id_code[index])
            if index == 1 or index == 2:
                year_number += id_code[index]
            if index == 3 or index == 4:
                month_number += id_code[index]
            if index == 5 or index == 6:
                day_number += id_code[index]
            if index == 7 or index == 8 or index == 9:
                birth_number += id_code[index]

        gender = get_gender(gender_number)
        year_number = int(year_number)
        ful_year = str(get_full_year(gender_number, year_number))
        birth_number = int(birth_number)

        if is_valid_birth_number(birth_number):
            location = get_birth_place(birth_number)

        return f"This is a {gender} born on {day_number}.{month_number}.{ful_year} in {location}"
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6
    print(is_valid_control_number("50205160274"))  # -> "Needs
    # the second algorithm!"(Ne proverjaet ljuboi string tk vernut'
    # pervaja f moshet libo needs... libo otvet, libo oshibku)

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
    print(get_data_from_id("50204073724"))

    print("\nTest now your own ID code:")
    personal_id = input()  # type your own id in command prompt
    print(is_id_valid(personal_id))  # -> True
