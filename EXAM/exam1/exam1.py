"""Exam1 (2023-01-04)."""
from math import floor
from typing import Optional


def count_digits(text: str) -> int:
    """
    Return the count of digits in a string.

    count_digits("123") => 3
    count_digits("a") => 0
    count_digits("") => 0
    count_digits("0a9r44") => 4
    """
    count = 0
    for element in text:
        if element.isdigit():
            count += 1
    return count


def pairwise_min(numbers: list[int]) -> list[int]:
    """
    Return a list where for every element pair in the input list the minimum of those is used.

    If there are odd number of elements, ignore the last lonely element.

    pairwise_min([1, 2, 3, 4]) => [1, 3]
    pairwise_min([]) => []
    pairwise_min([1, 9, 2]) => [1]
    pairwise_min([9, 9, 2, 2]) => [9, 2]
    """
    result = []
    if len(numbers) % 2 == 1:
        del numbers[-1]
    for i in range(0, len(numbers), 2):
        result.append(min([numbers[i], numbers[i + 1]]))
    return result


def same_length(texts: list[str]) -> list[str]:
    """
    Normalize the lengths of the elements and return a list of those normalized elements in reverse order.

    You have to find the longest element in the list.
    Append "_" to every shorter element so that all the lengths are equal.
    Return a list of those equal-length elements in reverse alphabetical order.

    same_length(["a", "ab", "abc"]) => ["abc", "ab_", "a__"]
    same_length([]) => []
    same_length(["_", "ab_", "a"]) => ["ab_", "a__", "___"]
    """
    if not texts:
        return []
    sorted_text = sorted(texts, key=lambda x: len(x), reverse=True)
    max = len(sorted_text[0])
    for i in range(len(sorted_text)):
        sorted_text[i] = sorted_text[i].ljust(max, "_")
    new_sorted_text = sorted(sorted_text, reverse=True)
    return new_sorted_text


def max_average(data: list, n: int) -> float:
    """
    Find maximum average with window width of n.

    max_average([1, 2, 3], 2) = (2 + 3) / 2
      possible variants with window 2: [1, 2], [2, 3]
    max_average([1, 7, 4, 5, 6], 3) = (7 + 4 + 5) / 3 = 5.333333
      possible variants with window 3: [1, 7, 4], [7, 4, 5], [4, 5, 6]

    :param data - data with at least n + 1 elements.
    :param n - Window width. Amount of consecutive numbers to take into calculation. n > 0.

    :return Maximum average achievable with current parameters.
    """
    sum = 0
    max_a = 0
    for i in range(len(data)):
        if len(data) - (i + n - 1) >= 1:
            for y in range(i, i + n):
                sum += data[y]
            average = sum / n
            if average > max_a:
                max_a = average
            sum = 0
    return max_a


def fuel_calculator(fuel: int) -> int:
    """
    Find needed amount of fuel for a given mass.

    Amount of fuel needed = mass divided by three, rounded down, subtract two
    + fuel needed for the fuel itself
    + fuel needed for the fuel's fuel + etc.

    Negative fuel rounds to zero.

    The solution has to be recursive! (no loops allowed)

    Examples:
    fuel_calculator(10) -> 1 + 0 = 1
    fuel_calculator(151) -> 48 + 14 + 2 + 0 = 64
    """
    r = floor(fuel / 3) - 2
    if r <= 0:
        return 0
    return r + fuel_calculator(r)


def longest_alphabet(text: str) -> str:
    """
    Find the longest substring which contains consecutive letters from alphabet.

    The input contains only lower case ascii letters (a - z).
    If there are several matches with the longest length, return the one which is lower alphabetically.

    longest_alphabet("abc") => "abc"
    longest_alphabet("abcklmn") => "klmn"
    longest_alphabet("klmabcopq") => "abc"
    longest_alphabet("a") => "a"
    longest_alphabet("xyab") => "ab"
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for i in range(len(text)):
        i_letter_index_in_alphabet = alphabet.index(text[i])
        if i + 1 < len(text) and text[i + 1] == alphabet[i_letter_index_in_alphabet + 1]:
            i_letter_index_in_alphabet += 1
            new_str = text[i] + text[i + 1]
            if i + 2 < len(text):
                for j in range(i + 2, len(text)):
                    i_letter_index_in_alphabet += 1
                    if i_letter_index_in_alphabet + 1 < len(alphabet) and text[j] == alphabet[i_letter_index_in_alphabet]:
                        new_str += text[j]
                    else:
                        break
            res.append(new_str)
        else:
            res.append(text[i])
    if len(res) > 0:
        result = sorted(res, key=lambda x: (-len(x), x))[0]
        return result
    return ""


class Donut:
    """Donut class."""

    def __init__(self, filling: str, icing: str):
        """
        Donut class constructor.

        :param filling: donut filling
        :param icing: donut icing
        """
        self.filling = filling
        self.icing = icing


class DonutFactory:
    """Donut factory class."""

    def __init__(self):
        """Donut factory class constructor."""
        self.factory_donuts = []

    def add_donuts(self, donuts: list):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        for donut in donuts:
            if isinstance(donut, Donut):
                self.factory_donuts.append(donut)

    def get_donuts(self) -> list:
        """
        Return list of all donuts present on the line at the moment.

        :return: list of all donuts
        """
        return self.factory_donuts

    def pack_donuts_by_filling_and_icing(self) -> dict:
        """
        Return dict with donuts divided by filling and icing.

        Dict key must be represented as tuple of filling and icing and value as list of donuts with
        given filling and icing.
        {(filling, icing): [donut1, donut2]}

        After packing, the production line for donuts should be empty (everything is packed).

        :return: dict
        """
        dic = {}
        for donut in self.factory_donuts:
            key = (donut.filling, donut.icing)
            if key not in dic:
                dic[key] = [donut]
            else:
                dic[key].append(donut)
        self.factory_donuts = []
        return dic

    def sort_donuts_by_icing_and_filling(self) -> list:
        """
        Return list of donuts sorted by icing in alphabetical order and then by filling in alphabetical order.

        :return: sorted list of donuts
        """
        return sorted(self.factory_donuts, key=lambda x: (x.icing, x.filling))

    def get_most_popular_donut(self) -> dict:
        """
        Return dict with icing and filling of the most popular donut.

        {'icing': most_pop_donut_icing, 'filling': most_pop_donut_filling}
        If there are several icing-filling combinations with the same amount of donuts,
        use the one which icing is alphabetically lower (a comes before b).

        Hint: you could use the result similar to pack_donuts_by_filling_and_icing method,
        but you cannot empty the production line of donuts.
        So, a common custom method can help here, which returns the dict.
        The most popular combination is the one element of the dict which has the most donuts
        (len on dict value is the highest).

        :return: dict with icing and filling of most pop donut
        """
        dic = {}
        filling_dic = {}
        icing_dic = {}
        for donut in self.factory_donuts:
            if donut.filling not in filling_dic:
                filling_dic[donut.filling] = 1
            elif donut.filling in filling_dic:
                filling_dic[donut.filling] += 1
            if donut.icing not in icing_dic:
                icing_dic[donut.icing] = 1
            elif donut.icing in icing_dic:
                icing_dic[donut.icing] += 1

        the_icing = sorted(icing_dic.items(), key=lambda x: (-x[1], x))
        the_filling = sorted(filling_dic.items(), key=lambda x: (-x[1], x))

        dic["icing"] = the_icing[0][0]
        dic["filling"] = the_filling[0][0]

        return dic

    def get_donuts_by_flavour(self, flavour: str) -> list:
        """
        Get list of donuts that have the same icing or filling as given in method parameter.

        :return: list of donuts with the given flavour.
        """
        result = []
        dic = {}
        for donut in self.factory_donuts:
            key = (donut.filling, donut.icing)
            if key not in dic:
                dic[key] = [donut]
            else:
                dic[key].append(donut)

        for recipe in dic:
            if flavour in recipe:
                result += dic[recipe]

        return result


class TravelItem:
    """Travel item."""

    def __init__(self, location: str, duration: int):
        """Initialize travel item with location and duration."""
        self.location = location
        self.duration = duration

    def get_location(self) -> str:
        """Return location."""
        return self.location

    def get_duration(self) -> int:
        """Return duration."""
        return self.duration


class TravelPackage:
    """Travel package combines multiple travel items."""

    def __init__(self, name: str):
        """Initialize the package with the given name."""
        self.name = name
        self.travel_package_items = []

    def create_duplicate(self, new_name: str) -> 'TravelPackage':
        """
        Create a duplicate travel package.

        The new package will be created with the new name.
        Also, all the items should be copied to the new package.
        """
        new_object = TravelPackage(new_name)
        new_object.travel_package_items = self.travel_package_items.copy()

    def get_total_duration(self) -> int:
        """Return the total duration of travel items in the package."""
        total_duration = 0
        for item in self.travel_package_items:
            total_duration += item.duration
        return total_duration

    def get_items(self) -> list[TravelItem]:
        """Return list of TravelItem objects."""
        return self.travel_package_items

    def get_name(self) -> str:
        """Return the name of the package."""
        return self.name


class TravelAgency:
    """Travel agency coordinates travel items and packages."""

    def __init__(self):
        """Initialize the agency."""
        self.agency = []

    def add_item_to_package(self, package_name: str, item: TravelItem) -> bool:
        """
        Add an item to the travel package.

        If this item already exists in the package with the given name,
        the method returns False (and the item is not added).

        Otherwise:
        If there is no package with the given name, then the package is created.
        The item is added to the package with the given name.
        The method returns True.
        """
        for package in self.agency:
            if package.name == package_name:
                for element in package.

    def get_packages(self) -> list[TravelPackage]:
        """Return list of packages in the insertion order."""
        pass

    def get_packages_by_location(self, location: str) -> list[TravelPackage]:
        """Return a list of TravelPackage objects where at least one item has the given location."""
        pass

    def search_package(self, locations: list, min_duration: int = None, max_duration: int = None) -> Optional[TravelPackage]:
        """
        Find a package which has all the locations specified in the list.

        If min_duration or max_duration is specified, then filter out packages,
        where total duration is between those values.

        If only min_duration is specified, use only those packages where total duration is greater or equal to that.
        If only max_duration is specified, use only those packages where total duration is less or equal to that.
        If both are specified, use packages where total duration is between those values.
        If none are specified, use all the packages.

        If locations list is empty, then every package matches.

        If multiple packages match, it doesn't matter which one to return.

        Return the found packages. If nothing matches, return None.
        """
        pass

    def get_package_overview_by_locations(self) -> str:
        """
        Create an overview where for every location all the packages are listed.

        The overview contains locations (strings) ordered alphabetically.
        And for every location a list of package names where this location is included, also ordered alphabetically.

        The format:

        location1:
         - package1
         - package2
        location2:
         - package1
         - package3

        The location has no spaces in front of it and is followed by the colon.
        The package has space, minus and space in front of it.
        There is no new line in the end of the string.

        If there are no packages, return empty string.
        """
        pass


if __name__ == '__main__':
    # print(count_digits("123")) #3
    # print(count_digits("a")) #0
    # print(count_digits("1aaasdsdd2dsdr45ktknt3"))

    # print(pairwise_min([1, 2, 4, 3]))
    # print(pairwise_min([1, 1, 4, 3, 5]))
    # print(pairwise_min([1, 1, 4, 3, 5, 6]))
    # print(pairwise_min([1, 1, 4, 3, 5, 4, 7]))

    # print(same_length(["aaa", "b"]) == ["b__", "aaa"])
    # print(same_length(["a", "b"]) == ["b", "a"])
    # print(same_length(["a", "c", "ab", "abc"])) #== ["abc", "ab_", "a__"])
    # print(same_length([]) == [])
    # print(same_length(["_", "ab_", "a"]) == ["ab_", "a__", "___"])

    # print(max_average([1, 2, 3, 3], 2) == 3.0)  # (3 + 3) / 2
    # print(max_average([1, 7, 2, 3, 3], 1) == 7.0)
    # print(max_average([1, 7, 2, 3, 3], 3) == 4.0)  # (7 + 2 + 3) / 3
    # print(max_average([8, 2, 9], 2) == 5.5)  # (2 + 9) / 2
    #
    # print(fuel_calculator(151) == 64)
    # print(fuel_calculator(-1) == 0)
    #
    # print(longest_alphabet("abc") == "abc")
    # print(longest_alphabet("abcklmn") == "klmn")
    # print(longest_alphabet("klmabcopq") == "abc")
    # print(longest_alphabet("a") == "a")
    # print(longest_alphabet("xyab") == "ab")
    #
    # # donut examples
    #
    # donut_factory = DonutFactory()
    # donut1 = Donut('chocolate', 'sugar')
    # donut2 = Donut('caramel', 'chocolate')
    # donut3 = Donut('cherry', 'marshmallow')
    # donut4 = Donut('chocolate', 'sugar')
    # donut5 = Donut('vanilla', 'cream')
    # donut6 = Donut('vanilla', 'cream')
    # donut7 = Donut('cherry', 'marshmallow')
    # donut8 = Donut('chocolate', 'sugar')
    #
    # donuts = [donut1, donut2, donut3, donut4, donut5, donut6, donut7, donut8]
    #
    # donut_factory.add_donuts(donuts)
    #
    # print(donut_factory.get_donuts_by_flavour("marshmallow") == [donut3, donut7])
    # print(donut_factory.get_most_popular_donut() == {'icing': 'sugar', 'filling': 'chocolate'})
    # print(donut_factory.sort_donuts_by_icing_and_filling() == [donut2, donut5, donut6, donut3, donut7, donut1,
    #                                                            donut4, donut8])
    # print(donut_factory.pack_donuts_by_filling_and_icing() == {
    #     ('chocolate', 'sugar'): [donut1, donut4, donut8],
    #     ('caramel', 'chocolate'): [donut2],
    #     ('cherry', 'marshmallow'): [donut3, donut7],
    #     ('vanilla', 'cream'): [donut5, donut6]
    # })
    #
    # # travel agency
    # item_tallinn = TravelItem("Tallinn", 200)
    # item_tartu = TravelItem("Tartu", 150)
    #
    # agency = TravelAgency()
    # assert agency.get_packages() == []
    #
    # assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is True
    # assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is False
    #
    # assert agency.add_item_to_package("Estonian trip", item_tallinn) is True
    # assert agency.add_item_to_package("Estonian trip", item_tartu) is True
    #
    # assert len(agency.get_packages()) == 2
    # assert agency.get_packages()[0].get_name() == "Shorty in Tallinn"
    # assert agency.get_packages()[1].get_name() == "Estonian trip"
    #
    # assert agency.get_packages()[1].get_total_duration() == 350
    #
    # packages = agency.get_packages_by_location("Tallinn")
    # assert len(packages) == 2
    # assert packages[0].get_name() == "Shorty in Tallinn"
    # assert packages[1].get_name() == "Estonian trip"
    #
    # assert agency.get_packages_by_location("Narva") == []
    #
    # package = agency.search_package(["Tartu"])
    # assert package.get_name() == "Estonian trip"
    # package = agency.search_package(["Tallinn"])
    # assert package.get_name() in ["Estonian trip", "Shorty in Tallinn"]
    # package = agency.search_package(["Tallinn"], min_duration=300)
    # assert package.get_name() == "Estonian trip"
    #
    # assert agency.get_package_overview_by_locations() == "Tallinn:\n - Estonian trip\n - Shorty in Tallinn\nTartu:\n - Estonian trip"