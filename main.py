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


def main():
    print("Program RPG")


main()