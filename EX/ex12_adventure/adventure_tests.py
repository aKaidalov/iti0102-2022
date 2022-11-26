"""Tests."""
from adventure import Adventurer, Monster, World


class TestAdventurer:

    def test_adventurer_basic(self):
        a1 = Adventurer("Danja", "Paladin", 85, 10)
        assert (a1.name, a1.class_type, a1.power, a1.experience) == ("Danja", "Paladin", 85, 10)

    def test_adventurer_advanced(self):
        a1 = Adventurer("Sasha", "Kkkmel", 100, -2)
        assert (a1.name, a1.class_type, a1.power, a1.experience) == ("Sasha", "Fighter", 10, 0)


class TestMonster:

    def test_monster_basic(self):
        m1 = Monster("Sasha", "Mouse", 10)
        assert (m1.name, m1.type, m1.power) == ("Sasha", "Mouse", 10)

    def test_monster_zombie(self):
        m1 = Monster("Danja", "Zombie", 5)
        assert (m1.name, m1.type, m1.power) == ("Undead Danja", "Zombie", 5)


class TestWorld:

    def test_world_add_adventurers(self):
        world = World("Sõber")
        hero1 = Adventurer("Danja", "Paladin", 85, 10)
        hero2 = Adventurer("Sasha", "Fighter", 10, 0)
        hero3 = Monster("Undead Timur", "Zombie", 5)
        hero4 = 4
        world.add_adventurer(hero1)
        world.add_adventurer(hero2)
        world.add_adventurer(hero3)
        world.add_adventurer(hero4)
        assert len(world.get_adventurer_list()) == 2

    def test_world_add_monsters(self):
        world = World("Sõber")
        hero1 = Adventurer("Danja", "Paladin", 85, 10)
        hero2 = Adventurer("Sasha", "Fighter", 10, 0)
        hero3 = Monster("Undead Timur", "Zombie", 5)
        hero4 = 4
        world.add_monster(hero1)
        world.add_monster(hero2)
        world.add_monster(hero3)
        world.add_monster(hero4)
        assert len(world.get_monster_list()) == 1
