"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Initialize the AlchemicalElement class."""
        self.name = name

    def __repr__(self) -> str:
        """Class representation."""
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.alchemical_storage = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if not isinstance(element, AlchemicalElement):
            raise TypeError("Only alchemical elements are allowed")
        self.alchemical_storage.append(element)

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        names = list(map(lambda x: x.name, self.alchemical_storage))
        count = names.count(element_name)
        if count > 0:
            for e in reversed(self.alchemical_storage):
                if e.name == element_name:
                    self.alchemical_storage.remove(e)
                    return e
        return None

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        e = self.alchemical_storage
        self.alchemical_storage = []
        return e

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        res = "Content:"
        if len(self.alchemical_storage) != 0:
            names = list(map(lambda x: x.name, self.alchemical_storage))
            filtered_names = []
            for el in sorted(names):
                if el not in filtered_names:
                    filtered_names.append(el)
            for element in filtered_names:
                count = names.count(element)
                res += f"\n * {element} x {count}"
            return res
        return res + "\n Empty."


# 2. osa
# ----------------------------------------------------------------------------------------------------------------------


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.alchemical_recipes = {}

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        if first_component_name == second_component_name or product_name == first_component_name or product_name == second_component_name:
            raise DuplicateRecipeNamesException
        for key in self.alchemical_recipes:
            if first_component_name in self.alchemical_recipes[key] and second_component_name in self.alchemical_recipes[key]:
                raise RecipeOverlapException
        self.alchemical_recipes[product_name] = (first_component_name, second_component_name)

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        if first_component_name != second_component_name:
            for key in self.alchemical_recipes:
                if first_component_name in self.alchemical_recipes[key] and second_component_name in self.alchemical_recipes[key]:
                    return key


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        self.recipes = recipes
        self.list_to_extract = []
        super(Cauldron, self).__init__()

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        check = True
        if len(self.alchemical_storage) == 0:
            super().add(element)
        else:
            for elem in reversed(self.alchemical_storage):  # [w, e, i] -> [i, e, w]
                result = self.recipes.get_product_name(elem.name, element.name)
                if result is not None:
                    super().pop(elem.name)
                    super().add(AlchemicalElement(result))
                    check = False
                    break
            if check:
                super().add(element)


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')
    recipes.add_recipe('Water', 'Wind', 'Ice')

    print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'
    print(recipes.get_product_name('Water', 'Wind'))
    print(recipes.get_product_name('Wind', 'Water'))

    try:
        recipes.add_recipe('Fire', 'Something else', 'Fire')
        print('Did not raise, not working as intended.')

    except DuplicateRecipeNamesException:
        print('Raised DuplicateRecipeNamesException, working as intended!')

    try:
        recipes.add_recipe('Fire', 'Earth', 'Gold')
        print('Did not raise, not working as intended.')

    except RecipeOverlapException:
        print('Raised RecipeOverlapException, working as intended!')

    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Fire'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]

    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Fire'))     # e, e, i
    cauldron.add(AlchemicalElement('Fire'))     # e, i, i
    cauldron.add(AlchemicalElement('Water'))    # e, i, r

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]
