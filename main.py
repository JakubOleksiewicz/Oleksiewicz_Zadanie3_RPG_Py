from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, id, name, hp, damage):
        self.id = id
        self.name = name
        self.hp = hp
        self.damage = damage

    @abstractmethod
    def show_info(self):
        pass


class IAttack(ABC):
    @abstractmethod
    def attack(self, target):
        pass


class NPC(Character):
    def __init__(self, id, name, hp, damage, attitude):
        super().__init__(id, name, hp, damage)
        self.attitude = attitude


def main():
    print("Program RPG")


main()