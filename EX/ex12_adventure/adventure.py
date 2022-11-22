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
        self.experience = max(0, experience)  # ( , ) - tuple? max() finds largest number. if exp < 0 -> 0.
        self.active_adventurer = False

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
        self.active_monster = False

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
        # self.active_adventurers = []
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

    # adventurers
    # ----------------------------------------------------------------------------------------------------------------------

    def add_adventurer(self, element: Adventurer):
        """Add an Adventurer class object to the adventurers list."""
        if isinstance(element, Adventurer):
            self.adventurers.append(element)

    def get_adventurer_list(self):
        """Return an adventurer list."""
        return list(filter(lambda a: not a.active_adventurer, self.adventurers))

    def get_active_adventurers(self):
        """Get active adventurers."""
        active_adventurers = list(filter(lambda a: a.active_adventurer, self.adventurers))
        return sorted(active_adventurers, key=lambda x: -x.experience)

    def add_strongest_adventurer(self, class_type: str):
        """Add strongest adventurer."""
        strongest_adventurer = max(
            list(filter(lambda x: x.class_type == class_type and not x.active_adventurer, self.adventurers)),
            key=lambda a: a.power)
        strongest_adventurer.active_adventurer = True

    def add_weakest_adventurer(self, class_type: str):
        """Add weakest adventurer."""
        weakest_adventurer = min(
            list(filter(lambda x: x.class_type == class_type and not x.active_adventurer, self.adventurers)),
            key=lambda a: a.power)
        weakest_adventurer.active_adventurer = True

    def add_most_experienced_adventurer(self, class_type: str):
        """Add most experienced adventurer."""
        most_experienced_adventurer = max(
            list(filter(lambda x: x.class_type == class_type and not x.active_adventurer, self.adventurers)),
            key=lambda a: a.experience)
        most_experienced_adventurer.active_adventurer = True

    def add_least_experienced_adventurer(self, class_type: str):
        """Add least experienced adventurer."""
        most_experienced_adventurer = min(
            list(filter(lambda x: x.class_type == class_type and not x.active_adventurer, self.adventurers)),
            key=lambda a: a.experience)
        most_experienced_adventurer.active_adventurer = True

    def add_adventurer_by_name(self, name: str):
        """Add adventurer by name."""
        for adventurer in self.adventurers:
            if adventurer.name == name and not adventurer.active_adventurer:
                adventurer.active_adventurer = True
                break

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Add all adventurers by class_type."""
        for adventurer in self.adventurers:
            if adventurer.class_type == class_type and not adventurer.active_adventurer:
                adventurer.active_adventurer = True

    def add_all_adventurers(self):
        """Add all adventurers."""
        for adventurer in self.adventurers:
            if not adventurer.active_adventurer:
                adventurer.active_adventurer = True

    # monsters
    # ----------------------------------------------------------------------------------------------------------------------

    def add_monster(self, element: Monster):
        """Add a Monster class object to the monsters list."""
        if isinstance(element, Monster):
            self.monsters.append(element)

    def get_monster_list(self):
        """Return a monster list."""
        return list(filter(lambda m: not m.active_monster, self.monsters))

    def get_active_monsters(self):
        """Get active monsters."""
        active_monsters = list(filter(lambda m: m.active_monster, self.monsters))
        return sorted(active_monsters, key=lambda x: -x.power)

    def add_monster_by_name(self, name: str):
        """Add adventurer by name."""
        for monster in self.monsters:
            if monster.name == name and not monster.active_monster:
                monster.active_monster = True
                break

    def add_strongest_monster(self):
        """Add the strongest monster."""
        if len(self.monsters) > 0:
            strongest_monster = max(list(filter(lambda x: not x.active_monster, self.monsters)), key=lambda m: m.power)
            strongest_monster.active_monster = True

    def add_weakest_monster(self):
        """Add the weakest adventurer."""
        if len(self.monsters) > 0:
            weakest_monster = min(list(filter(lambda x: not x.active_monster, self.monsters)), key=lambda m: m.power)
            weakest_monster.active_monster = True

    def add_all_monsters_of_type(self, type: str):
        """Add all adventurers by class_type."""
        for monster in self.monsters:
            if monster.type == type and not monster.active_monster:
                monster.active_monster = True

    def add_all_monsters(self):
        """Add all monsters."""
        for monster in self.monsters:
            if not monster.active_monster:
                monster.active_monster = True

# ----------------------------------------------------------------------------------------------------------------------

    def remove_character(self, name: str):
        """Remove character."""
        for adventurer in self.adventurers:
            if name == adventurer.name:
                adventurer.active_adventurer = False
                self.graveyard.append(adventurer)
                self.adventurers.remove(adventurer)
                return
        for monster in self.monsters:
            if name == monster.name:
                monster.active_monster = False
                self.graveyard.append(monster)
                self.monsters.remove(monster)
                return
        for deadman in self.graveyard:
            if name == deadman.name:
                self.graveyard.remove(deadman)
                return
        # self.graveyard = list(filter(lambda a: a.name != name, self.adventurers))

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
                    self.monsters.append(
                        Monster(f"Undead {deadman.name}", f"Zombie {deadman.class_type}", deadman.power))
            self.active_necromancers = False
            self.graveyard = []

    # 3. osa
    # ----------------------------------------------------------------------------------------------------------------------
    # -----------------

    def find_druid(self):
        """Show if there is a driud."""
        active_adventurers = self.get_active_adventurers()
        for adventurer in active_adventurers:  # Kak napisat' odnoi strochkoi?
            if adventurer.class_type == "Druid":
                return True
        return False

    def check_for_druid_and_monsters(self):
        """Deactivate monsters with Animal and Ent type if there is a Druid."""
        if self.find_druid():
            active_monsters = self.get_active_monsters()  # Mozno srazu self isspolsovat' v for?
            for monster in active_monsters:
                if monster.type == "Animal" or monster.type == "Ent":
                    monster.active_monster = False

    # -----------------

    def find_zombie(self):
        """Show if there are any zombies."""
        for monster in self.get_active_monsters():
            if "Zombie" in monster.type:
                return True
        return False

    def check_for_paladin_and_zombies(self):
        """Double Paladin power if there are any zombies."""
        if self.find_zombie():
            active_adventurers = self.get_active_adventurers()
            for adventurer in active_adventurers:
                if adventurer.class_type == "Paladin":
                    adventurer.power *= 2

    def return_paladin_power_back_to_normal(self):
        """Return paladin power back to normal"""
        if self.find_zombie():
            for adventurer in self.adventurers:
                if adventurer.class_type == "Paladin":
                    adventurer.power = math.floor(adventurer.power / 2)

    # -----------------

    # def add_more_power_after_winn(self, active_adventurers: list, individual_experience: int):
    #     """Add power."""
    #     for adventurer in active_adventurers:
    #         adventurer.experience += individual_experience

    def go_adventure(self, deadly: bool = False):
        """A."""
        self.check_for_druid_and_monsters()
        self.check_for_paladin_and_zombies()  # Gives all Paladins power for this round
        active_adventurers = self.get_active_adventurers()
        active_monsters = self.get_active_monsters()
        active_a_power_sum = sum(list(map(lambda a: a.power, active_adventurers)))
        active_m_power_sum = sum(list(map(lambda m: m.power, active_monsters)))
        print(active_a_power_sum)
        print(active_m_power_sum)
        print(active_monsters)
        print(active_adventurers)
        if not active_monsters:
            for adventurer in active_adventurers: adventurer.active_adventurer = False
        else:
            individual_experience = math.floor(active_m_power_sum / len(active_monsters))

            if active_a_power_sum > active_m_power_sum:
                if not deadly:
                    for adventurer in active_adventurers: adventurer.add_experience(individual_experience)
                    self.return_paladin_power_back_to_normal()  # Takes all Paladins' power back at the end of the round
                    for adventurer in active_adventurers: adventurer.active_adventurer = False
                    for monster in active_monsters: monster.active_monster = False
                else:
                    individual_experience *= 2
                    print(individual_experience)
                    for adventurer in active_adventurers: adventurer.add_experience(individual_experience)
                    self.return_paladin_power_back_to_normal()  # Takes all Paladins' power back at the end of the round
                    for adventurer in active_adventurers: adventurer.active_adventurer = False
                    for monster in active_monsters: self.remove_character(
                        monster.name)  # Change active status to False in ".remove_character"
            elif active_a_power_sum < active_m_power_sum:
                if not deadly:
                    for adventurer in active_adventurers: adventurer.active_adventurer = False
                    for monster in active_monsters: monster.active_monster = False
                else:
                    for adventurer in active_adventurers: self.remove_character(adventurer)
                    for monster in active_monsters: monster.active_monster = False
            else:
                i_e = math.floor(individual_experience / 2)
                for adventurer in active_adventurers: adventurer.experience.add_experience(i_e)
                self.return_paladin_power_back_to_normal()  # Takes all Paladins' power back at the end of the round
                for adventurer in active_adventurers: adventurer.active_adventurer = False
                for monster in active_monsters: monster.active_monster = False


if __name__ == "__main__":
    # print("Kord oli maailm.")
    # world = World("Sõber")
    # print(world.get_python_master())  # -> "Sõber"
    # print(world.get_graveyard())  # -> []
    # print()
    # print("Tutvustame tegelasi.")
    # hero = Adventurer("Sander", "Paladin", 50)
    # friend = Adventurer("Peep", "Druid", 25)
    # another_friend = Adventurer("Toots", "Wizard", 40)
    # annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    # print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # # Ei maksa liiga tugevaks ka ennast alguses teha!
    # print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    # print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    # print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    # print()
    #
    # print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    # friend.add_power(20)
    # print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    # print()
    #
    # world.add_adventurer(hero)
    # world.add_adventurer(friend)
    # world.add_adventurer(another_friend)
    # print(world.get_adventurer_list())  # -> Sander, Peep ja Toots
    #
    # world.add_monster(annoying_friend)
    # # Ei, tüütu sõber, sa ei saa olla vaenlane.
    # print(world.get_monster_list())  # -> []
    # world.add_adventurer(annoying_friend)
    # print()
    #
    # print("Oodake veidikene, ma tekitan natukene kolle.")
    # zombie = Monster("Rat", "Zombie", 10)
    # goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    # goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    # big_ogre = Monster("Big Ogre", "Ogre", 120)
    # gargantuan_badger = Monster("Massive Badger", "Animal", 1590)
    #
    # print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    # print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."
    #
    # world.add_monster(goblin_spear)
    #
    # print()
    # print("Mängime esimese seikluse läbi!")
    # world.add_strongest_adventurer("Druid")
    # world.add_strongest_monster()
    # print(world.get_active_adventurers())  # -> Peep
    # print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    # print()
    #
    # world.go_adventure(True)
    #
    # world.add_strongest_adventurer("Druid")
    # print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    # print("Surnuaias peaks üks goblin olema.")
    # print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    # print()
    #
    # world.add_monster(gargantuan_badger)
    # world.add_strongest_monster()
    #
    # world.go_adventure(True)
    # # Druid on loomade sõber ja ajab massiivse mägra ära.
    # print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    # print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]
    #
    # world.remove_character("Massive Badger")
    # print(world.get_monster_list())  # -> []
    # print()
    #
    # print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
    #       "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
    world = World("Sõber")
    assert world.get_python_master() == "Sõber"
    assert world.get_graveyard() == []

    hero = Adventurer("Sander", "Paladin", 50)
    hero2 = Adventurer("Toomas", "Druid", 50)


    monster = Monster("Giant Badger", "Animal", 39043)
    monster2 = Monster("Monsu", "Zombie", 149)

    world.add_monster(monster)
    world.add_monster(monster2)
    world.add_adventurer(hero)
    world.add_adventurer(hero2)

    world.add_all_adventurers()
    world.add_all_monsters()

    world.go_adventure(True)

    print(hero2)
    print(hero)
