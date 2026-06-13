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

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        print(self.name + " otrzymuje " + str(damage) + " obrazen. HP: " + str(self.hp))


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
        print("- " + self.name + " atakuje koscia.")
        target.take_damage(self.damage)

    def show_info(self):
        print("Szkielet | ID: " + str(self.id) + " | Nazwa: " + self.name + " | HP: " + str(self.hp))


class Ork(NPC, IAttack):
    def __init__(self, id, name):
        super().__init__(id, name, 70, 12, "Agresywny")

    def attack(self, target):
        print("- " + self.name + " atakuje toporem.")
        target.take_damage(self.damage)

    def show_info(self):
        print("Ork | ID: " + str(self.id) + " | Nazwa: " + self.name + " | HP: " + str(self.hp))


def main():
    skeleton1 = Skeleton(1, "Dr. Bones")
    ork1 = Ork(2, "Azog")

    characters = [skeleton1, ork1]

    for character in characters:
        character.show_info()

    print("--------------------------------------")

    attacker1 = skeleton1
    attacker2 = ork1

    print("-=-=( Bitwa: " + skeleton1.name + " vs " + ork1.name + " )=-=-")

    while ork1.hp > 0 and skeleton1.hp > 0:
        attacker1.attack(ork1)

        if ork1.hp <= 0:
            break

        attacker2.attack(skeleton1)

    print("-=-=( Wygrywa: " + (skeleton1.name if ork1.hp == 0 else ork1.name) + " )=-=-")


main()