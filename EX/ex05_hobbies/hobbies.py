"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    dic = {}
    split_data = data.split("\n")
    for element in split_data:
        set_of_hobbies = set()
        name_and_hobby = element.split(":")
        for el in split_data:
            if name_and_hobby[0] in el:
                set_of_hobbies.add(el[len(name_and_hobby[0]) + 1:])     # First position([0]) is right, because len = 4,
        dic[name_and_hobby[0]] = set_of_hobbies                         # but ":" on pos 3 (0123) + 1 (+1 = char after :)
    return dic
    #
    # dic = {}
    # split_data = data.split("\n")
    # for element in split_data:
    #     name_and_hobby = element.split(":")
    #     if name_and_hobby[0] in dic:
    #         hobbies = dic[name_and_hobby[0]]
    #         if name_and_hobby[1] not in hobbies:
    #             hobbies.append(name_and_hobby[1])
    #             del dic[name_and_hobby[0]]
    #             dic[name_and_hobby[0]] = hobbies
    #     else:
    #         dic[name_and_hobby[0]] = [name_and_hobby[1]]
    # return dic


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    new_dic = {}
    for name in dic:
        hobbies = dic[name]
        new_dic[name] = sorted(hobbies)
    return new_dic



def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.
    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    dic = {}
    split_data = data.split("\n")
    for element in split_data:
        set_of_names = set()
        name_and_hobby = element.split(":")
        for el in split_data:
            if name_and_hobby[1] in el:
                set_of_names.add(el[:-len(name_and_hobby[1]) - 1])  # First position([0]) is right, because len = 4,
        dic[name_and_hobby[1]] = sorted(list(set_of_names))
    return dic




if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(sample_data)
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print("\n")
    print(sort_dictionary({"b": [], "a": [], "c": []}))
    print(sort_dictionary({"": ["a", "f", "d"]}))
    print(sort_dictionary({"b": ["d", "a"], "a": ["c", "f"]}))
    print(sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}))
    print("\n")
    print(create_dictionary_with_hobbies(sample_data))
