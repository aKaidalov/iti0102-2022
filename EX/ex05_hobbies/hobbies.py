"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    # dic = {}
    # split_data = data.split("\n")
    #
    # for element in split_data:
    #     set_of_hobbies = set()
    #     name_and_hobby = element.split(":")
    #     for el in split_data:
    #         split_el = el.split(":")
    #         if name_and_hobby[0] == split_el[0]:
    #             set_of_hobbies.add(el[len(name_and_hobby[0]) + 1:])     # First position([0]) is right, because len = 4,
    #     dic[name_and_hobby[0]] = set_of_hobbies                         # but ":" on pos 3 (0123) + 1 (+1 = char after :)
    #
    # return dic
    #
    dic = {}
    split_data = data.split("\n")
    for element in split_data:
        name_and_hobby = element.split(":")
        if name_and_hobby[0] in dic:
            hobbies = dic[name_and_hobby[0]]
            if name_and_hobby[1] not in hobbies:
                hobbies.append(name_and_hobby[1])
                del dic[name_and_hobby[0]]
                dic[name_and_hobby[0]] = hobbies
        else:
            dic[name_and_hobby[0]] = [name_and_hobby[1]]
    return dic


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
    sorted_names_list = sorted(dic.keys())

    for name in sorted_names_list:
        hobbies = dic[name]
        new_dic[name] = sorted(hobbies)

    return new_dic


# -----------------------------------------------------------------------


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
                set_of_names.add(el[:-len(name_and_hobby[1]) - 1])
        dic[name_and_hobby[1]] = sorted(list(set_of_names))

    return dic


# -----------------------------------------------------------------------


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    dic = create_dictionary(data)
    sorted_dic = sort_dictionary(dic)
    names = sorted_dic.keys()
    max_len = 0
    names_list = []

    for name in names:
        length = len(sorted_dic[name])
        if length > max_len:
            max_len = length
    for name in names:
        if len(sorted_dic[name]) == max_len:
            names_list.append(name)

    return names_list


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    dic = create_dictionary_with_hobbies(data)
    sorted_dic = sort_dictionary(dic)
    hobbies = sorted_dic.keys()
    min_len = 1000
    hobbies_list = []

    for hobby in hobbies:
        length = len(sorted_dic[hobby])
        if length < min_len:
            min_len = length
    for hobby in hobbies:
        if len(sorted_dic[hobby]) == min_len:
            hobbies_list.append(hobby)

    return hobbies_list


# -----------------------------------------------------------------------


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    dic = create_dictionary(data)
    sorted_dic = sort_dictionary(dic)
    names = sorted_dic.keys()
    list_for_tuple = []

    for name in names:
        hobbies = sorted_dic[name]
        hobbies_tuple = tuple(hobbies)
        one_person_tuple = tuple([name, hobbies_tuple])
        list_for_tuple.append(one_person_tuple)
    final_tuple = tuple(list_for_tuple)

    return final_tuple


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    dic = create_dictionary_with_hobbies(data)
    names_list = []
    union = set()

    for hobby in hobbies:
        if hobby in dic.keys():
            names_in_hobby = set(dic[hobby])
            names_list.append(names_in_hobby)
    if len(names_list) != 0:
        if len(names_list) == 1:
            return names_list[0]
        else:
            for i in range(1, len(names_list)):
                if i == 1:
                    union = names_list[i - 1] | names_list[i]
                else:
                    union = union | names_list[i]
            return union
    else:
        return set()


def find_two_people_with_most_common_hobbies(data: str) -> tuple:
    """
    Find a pair of people who have the highest ratio of common hobbies to different hobbies.

    Common hobbies are the ones which both people have.
    Different hobbies are the ones, which only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies, ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair (and in which order) is returned.

    If there are less than 2 people in the input, return None.
    """
    dic = create_dictionary(data)
    names = list(dic.keys())
    hobbies_list = []
    new_dic = {}

    for name in names:
        hobbies_in_name = set(dic[name])
        hobbies_list.append(hobbies_in_name)

    if len(names) > 1:
        for i in range(len(names) - 1):
            for j in range(i + 1, len(names)):
                common = set(hobbies_list[i]) & set(hobbies_list[j])
                diff = set(hobbies_list[i]) ^ set(hobbies_list[j])
                if diff != set():
                    ratio = len(common) / len(diff)
                    new_dic[round(ratio, 1)] = tuple([names[i], names[j]])
                else:
                    ratio = len(common) / 0.1
                    new_dic[ratio] = tuple([names[i], names[j]])

        best_ratio = max(new_dic)
        return new_dic[best_ratio]


if __name__ == '__main__':
    # sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    # dic = create_dictionary(sample_data)
    # print("shopping" in dic["Wendy"])  # -> True
    # print("fitness" in dic["Sophie"])  # -> False
    # print("gaming" in dic["Peter"])  # -> True
    # print(len(dic["Jack"]))  # ->  12
    # print(len(dic["Carmen"]))  # -> 10
    # print(len(dic["Molly"]))  # -> 5
    # print(len(dic["Sophie"]))  # -> 7
    # print("\n")

    # print(sort_dictionary({"b": [], "a": [], "c": []}))
    # print(sort_dictionary({"": ["a", "f", "d"]}))
    # print(sort_dictionary({"b": ["d", "a"], "a": ["c", "f"]}))
    # print(sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}))
    # print("\n")
    #
    # print(create_dictionary_with_hobbies(sample_data))
    # print("\n")

    # sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    # print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    #
    # sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    # dic = create_dictionary(sample_data)
    # print("shopping" in dic["Wendy"])  # -> True
    # print("fitness" in dic["Sophie"])  # -> False
    # print("gaming" in dic["Peter"])  # -> True
    # print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    # print(len(dic["Jack"]))  # ->  12
    # print(len(dic["Carmen"]))  # -> 10
    # print(len(dic["Molly"]))  # -> 5
    # print(len(dic["Sophie"]))  # -> 7
    # print(find_least_popular_hobbies(sample_data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']
    # print("\n")
    #
    # sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    #
    # sort_result = sort_names_and_hobbies(sample_data)
    # # if the condition after assert is False, error will be thrown
    # assert isinstance(sort_result, tuple)
    # assert len(sort_result) == 10
    # assert sort_result[0][0] == 'Alfred'
    # assert len(sort_result[0][1]) == 7
    # assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # # if you see this line below, then everything seems to be ok!
    # print("sorting works!")

    sample_data = "\n".join(f"name{i}:hobby{j}" for i in range(500) for j in range(100))
    from datetime import datetime
    date1 = datetime.now()
    print(create_dictionary(sample_data), ["hobby56", "hobby77", "hobby99"]) == {f"name{i}" for i in range(500)}
    date2 = datetime.now()
    print(date2 - date1)
    # print(find_people_with_hobbies(
    #     "John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting",
    #     ["running", "dancing"]
    # ))  # {"John", "Mary", "Jack"}

    # sample_data = 'name3:hobby8\nname0:hobby10\nname2:hobby10\nname0:hobby0\nname3:hobby13\nname0:hobby9\nname2:hobby3\nname1:hobby6\nna...y11\nname2:hobby0\nname0:hobby12\nname0:hobby4\nname0:hobby13\nname4:hobby6\nname1:hobby10\nname1:hobby8\nname3:hobby5'
    # print(find_two_people_with_most_common_hobbies(sample_data))
