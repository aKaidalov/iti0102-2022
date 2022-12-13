"""Santa's workshop."""

import requests


class Child:
    """Class for children."""

    def __init__(self, name, country):
        """Child constructor."""
        self.name = name
        self.country = country
        self.is_nise = True
        self.present = "Present"

    def __repr__(self):
        """Child representation."""
        return f"Name: {self.name}, country: {self.country}."


class Workshop:
    """Christmas class."""

    def __init__(self):
        """Christmas constructor."""
        self.nice_children = []
        # self.naughty_children = []

        self.wishlist = {}
        self.storage = {}

    def parse_nice_list(self, filename: str):
        """Parse nice list."""
        response = requests.get(filename)
        children = response.text.rstrip("\n").split("\n")
        for child in children:
            name_and_country = child.split(", ")
            self.nice_children.append(Child(name_and_country[0], name_and_country[1]))
        print(self.nice_children)

    # def parse_naughty_list(self, filename: str):
    #     response = requests.get(filename)
    #     children = response.text.rstrip("\n").split("\n")
    #     for child in children:
    #         name_and_country = child.split(", ")
    #         object_child = Child(name_and_country[0], name_and_country[1])
    #         object_child.is_nise = False
    #         self.naughty_children.append(object_child)
    #     print("\n")
    #     print(self.naughty_children)

    def parse_wishlist(self, filename: str):
        """Parse wishlist."""
        response = requests.get(filename)
        wishlist = response.text.rstrip("\n").split("\n")
        for child_and_wishes in wishlist:
            child_and_wishes = child_and_wishes.split(", ")
            self.wishlist[child_and_wishes[0]] = child_and_wishes[1]
            # if len(child_and_wishes) > 2:
            #     for i in range(2, len(child_and_wishes)):
            #         self.wishlist[child_and_wishes[0]].append(child_and_wishes[i])
        keys = self.wishlist.keys()
        print("\n")
        print(keys)

    def get_presents_for_nice_children(self):
        """
        Only nice children receive presents this year.

        Nice children get 1 present, naughty get nothing.
        """
        for child in self.nice_children:
            child.present = self.wishlist[child.name]
            print(child.present)

    def add_presents_to_storage(self):
        """Add all presents to storage."""
        for child in self.nice_children:
            present = child.present
            new_present_name = present.replace(" ", "%20")
            response = requests.get(f"https://cs.ttu.ee/services/xmas/gift?name={new_present_name}")
            self.storage[child.name] = response.json()

        print("\n")
        print(self.storage)


if __name__ == '__main__':
    workshop = Workshop()
    workshop.parse_nice_list("https://iti0102-2020.pages.taltech.ee/info/files/ex15_nice_list.csv")
    # workshop.parse_naughty_list("https://iti0102-2020.pages.taltech.ee/info/files/ex15_naughty_list.csv")
    workshop.parse_wishlist("https://iti0102-2020.pages.taltech.ee/info/files/ex15_wish_list.csv")
    workshop.get_presents_for_nice_children()
    workshop.add_presents_to_storage()
