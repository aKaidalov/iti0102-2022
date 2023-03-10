"""TK1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = minutes // 60
    new_minutes = minutes % 60
    if minutes < 60:
        return f'{minutes}min'
    elif hours != 0 and new_minutes == 0:
        return f'{hours}h'
    else:
        return f'{hours}h {new_minutes}min'


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if is_birthday:
        if speed < 66:
            result = 0
        elif 65 < speed < 86:
            result = 1
        else:
            result = 2
    else:
        if speed < 61:
            result = 0
        elif 60 < speed < 81:
            result = 1
        else:
            result = 2
    return result


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    len_of_first_half = len(text) // 2
    return text[:len_of_first_half]


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    first_element = nums[0]
    last_element = nums[-1]
    if first_element <= last_element:
        if first_element >= len(nums):
            return first_element
        else:
            return nums[first_element]
    else:
        if last_element >= len(nums):
            return last_element
        else:
            return nums[last_element]


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    quantity = text.count(to_remove)
    new_list = []
    if to_remove != "":
        if quantity > 2:
            list = text.split(to_remove)
            list.insert(1, to_remove)
            list.insert(-1, to_remove)
            for element in list:
                if element != '':
                    new_list.append(element)
            new_text = "".join(new_list)
        else:
            return text
    else:
        return text
    return new_text
