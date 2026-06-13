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


class Skeleton(NPC, IAttack):
    def __init__(self, id, name):
        super().__init__(id, name, 40, 8, "Agresywny")

    def attack(self, target):
        pass

    def show_info(self):
        print("Szkielet | ID: " + str(self.id) + " | Nazwa: " + self.name + " | HP: " + str(self.hp))


class Ork(NPC, IAttack):
    def __init__(self, id, name):
        super().__init__(id, name, 70, 12, "Agresywny")

    def attack(self, target):
        pass

    def show_info(self):
        print("Ork | ID: " + str(self.id) + " | Nazwa: " + self.name + " | HP: " + str(self.hp))


def main():
    skeleton1 = Skeleton(1, "Dr. Bones")
    ork1 = Ork(2, "Azog")

    characters = [skeleton1, ork1]

    for character in characters:
        character.show_info()


main()