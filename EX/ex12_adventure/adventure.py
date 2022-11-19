"""Adventure."""
import math


class Adventurer:
    """
    Adventurer class.

    Every object must have a name, class type,
    power and experience.
    """

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Initialize the Adventurer class."""
        self.name = name

        if class_type not in {"Druid", "Wizard", "Paladin"}:
            class_type = "Fighter"
        self.class_type = class_type

        if power > 99:
            power = 10
        self.power = power

        self.experience = max(0, experience)    # ( , ) - tuple? max() finds largest number. if exp < 0 -> 0.

    def __repr__(self):
        """Class representation."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def add_power(self, power: int):
        """Add power to Adventurer."""
        self.power += power

    def add_experience(self, exp: int):
        """Add experience to Adventurer."""
        if exp > 0:
            self.experience = self.experience + exp
            if self.experience > 99:
                self.power += math.floor(self.experience / 10)
                self.experience = 0


class Monster:
    """Monster class."""

    def __init__(self, name: str, type: str, power: int):
        """Initialize the Monster class."""
        if type == "Zombie" and "Undead " not in name:
            name = "Undead " + name
        self.name = name
        self.type = type
        self.power = power

    def __repr__(self):
        """Class representation."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """World class."""

    def __init__(self, python_master: str):
        """Initialize the World class."""
        self.python_master = python_master
        self.graveyard = []
        self.adventurers = []
        self.monsters = []
        self.active_necromancers = False

    def __repr__(self):
        """Class representation."""
        pass

    def get_python_master(self):
        """Return a python master."""
        return self.python_master

    def get_graveyard(self):
        """Return a graveyard."""
        return self.graveyard

    def get_adventurer_list(self):
        """Return an adventurer list."""
        return self.adventurers

    def get_monster_list(self):
        """Return a monster list."""
        return self.monsters

    def add_adventurer(self, element: Adventurer):
        """Add an Adventurer class object to the adventurers list."""
        if isinstance(element, Adventurer):
            self.adventurers.append(element)

    def add_monster(self, element: Monster):
        """Add a Monster class object to the monsters list."""
        if isinstance(element, Monster):
            self.monsters.append(element)

    def remove_character(self, name: str):
        """Remove character."""
        for adventurer in self.adventurers:
            if name == adventurer.name:
                self.graveyard.append(adventurer)
                self.adventurers.remove(adventurer)
                break
        for monster in self.monsters:
            if name == monster.name:
                self.graveyard.append(monster)
                self.monsters.remove(monster)
                break
        for deadman in self.graveyard:
            if name == deadman.name:
                self.graveyard.remove(deadman)
                break

    def necromancers_active(self, element: bool):
        """Activate necromancers."""
        self.active_necromancers = element

    def revive_graveyard(self):
        """Revive graveyard."""
        if self.active_necromancers:
            for deadman in self.graveyard:
                if isinstance(deadman, Monster):
                    deadman.type = "Zombie"
                    self.monsters.append(deadman)
                elif isinstance(deadman, Adventurer):
                    self.monsters.append(Monster(f"Undead {deadman.name}", f"Zombie {deadman.class_type}", deadman.power))
            self.active_necromancers = False
            self.graveyard = []


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
