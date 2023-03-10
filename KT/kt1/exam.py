"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string.

    The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if s == "":
        return s
    return s[0].capitalize() + s[1:]


def has_seven(nums):
    """
    Whether the list has three 7s and no repeated consecutive elements.

    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if 7 in nums and nums.count(7) == 3:
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                return False
        return True
    return False


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], []]
    """
    if amount > 1:
        big_list = [initial_list] * amount
        if factor > 0 and factor != len(initial_list) and initial_list is not []:
            for count, small_list in enumerate(big_list):
                if count != 0:
                    temp_list = big_list[count - 1].copy()
                    for e in range(len(big_list[count - 1])):
                        if e + 1 + factor > len(big_list[count - 1]):        # [0, 1, 2] => [1, 2, 3]
                            position = ((e + 1 + factor) % len(big_list[count - 1])) - 1
                            del temp_list[position]
                            temp_list.insert(position, big_list[count - 1][e])
                        else:
                            position = (e + factor)
                            del temp_list[position]
                            temp_list.insert(position, big_list[count - 1][e])
                    big_list[count] = temp_list
        return big_list
    return initial_list


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    dic = {}
    list_with_info = call_log.split(",")
    for element in list_with_info:
        list_with_names = element.split(":")
        for i in range(len(list_with_names)):
            if i + 1 <= len(list_with_names) - 1:
                if list_with_names[i] not in dic:
                    dic[list_with_names[i]] = [list_with_names[i + 1]]
                else:
                    if list_with_names[i + 1] not in dic[list_with_names[i]]:
                        dic[list_with_names[i]].append(list_with_names[i + 1])
    return dic
