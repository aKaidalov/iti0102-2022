"""Adventure."""
import math
import random
import string


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
        if type == "Zombie":
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
                    deadman.name = f"Undead {deadman.name}"
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

    def go_adventure(self, deadly: bool = False):
        """Adfcg."""
        self.check_for_druid_and_monsters()
        self.check_for_paladin_and_zombies()  # Gives all Paladins power for this round
        active_adventurers = self.get_active_adventurers()
        active_monsters = self.get_active_monsters()
        active_a_power_sum = sum(list(map(lambda a: a.power, active_adventurers)))
        active_m_power_sum = sum(list(map(lambda m: m.power, active_monsters)))
        if not active_monsters:
            for adventurer in active_adventurers: adventurer.active_adventurer = False
        else:
            individual_experience = math.floor(active_m_power_sum / len(active_adventurers))

            if active_a_power_sum > active_m_power_sum:
                if not deadly:
                    self.return_paladin_power_back_to_normal()  # Takes all Paladins' power back at the end of the round
                    for adventurer in active_adventurers: adventurer.add_experience(individual_experience)
                    for adventurer in active_adventurers: adventurer.active_adventurer = False
                    for monster in active_monsters: monster.active_monster = False
                else:
                    individual_experience *= 2
                    print(individual_experience)
                    self.return_paladin_power_back_to_normal()  # Takes all Paladins' power back at the end of the round
                    for adventurer in active_adventurers: adventurer.add_experience(individual_experience)
                    for adventurer in active_adventurers: adventurer.active_adventurer = False
                    for monster in active_monsters: self.remove_character(
                        monster.name)  # Change active status to False in ".remove_character"
            elif active_a_power_sum < active_m_power_sum:
                if not deadly:
                    for adventurer in active_adventurers: adventurer.active_adventurer = False
                    for monster in active_monsters: monster.active_monster = False
                else:
                    for adventurer in active_adventurers: self.remove_character(adventurer.name)
                    for monster in active_monsters: monster.active_monster = False
            else:
                i_e = math.floor(individual_experience / 2)
                self.return_paladin_power_back_to_normal()  # Takes all Paladins' power back at the end of the round
                for adventurer in active_adventurers: adventurer.add_experience(i_e)
                for adventurer in active_adventurers: adventurer.active_adventurer = False
                for monster in active_monsters: monster.active_monster = False


if __name__ == "__main__":
    def generate_random_character(power):
        acceptable_classes = ["Fighter", "Druid", "Paladin", "Wizard"]
        return Adventurer(generate_string(30), random.choice(acceptable_classes), power)


    def generate_random_monster(power):
        return Monster(generate_string(3), generate_string(9), power)


    def generate_string(length):
        return "".join([random.choice(string.ascii_lowercase) for _ in range(length)])


    for _ in range(10):
        world = World("Mad God")
        hero_power = 0
        monster_power = 0
        monster_count = 0
        hero_count = 0
        for _ in range(random.randint(1, 5)):
            power = random.randint(0, 5)
            hero = generate_random_character(power)
            world.add_adventurer(hero)
            hero_power += power
            hero_count += 1
        for _ in range(random.randint(1, 5)):
            power = random.randint(0, 5)
            monster = generate_random_monster(power)
            world.add_monster(monster)
            monster_power += power
            monster_count += 1

        world.add_all_adventurers()
        world.add_all_monsters()
        world.go_adventure(True)

        if hero_power > monster_power:
            assert len(world.get_graveyard()) == monster_count
        elif hero_power == monster_power:
            assert len(world.get_graveyard()) == 0
        elif hero_power < monster_power:
            assert len(world.get_graveyard()) == hero_count
