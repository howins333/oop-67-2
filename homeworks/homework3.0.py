from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.__hp = hp
        self.strength = strength

    def greet(self):
        return f'{self.name} greeting!'
    def rest(self):
        print(f"{self.name} rests")
        self.__hp += 1
        print(f"{self.name}'s health increased! Current health: {self.__hp}")

    @abstractmethod
    def attack(self):
        pass

class Takamura(Hero):
    def __init__(self, name, lvl, hp, strength, defense):
        super().__init__(name, lvl, hp, strength)
        self.defense = defense
    def attack(self):
      print(f'{self.name} hooked!')

class Ippo(Hero):
    def __init__(self, name, lvl, hp, strength, dodge_speed):
        super().__init__(name, lvl, hp, strength)
        self.dodge_speed = dodge_speed
    def attack(self):
        print(f'{self.name} dempsey attack!')

class Ricardo(Hero):
    def __init__(self, name, lvl, hp, strength, reflex_speed):
        super().__init__(name, lvl, hp, strength)
        self.reflex_speed = reflex_speed
    def attack(self):
        print(f'{self.name} ghost jab!')

if __name__ == "__main__":
    Takamura = Takamura("Такамура", 5, 100, 15, 100)
    Ippo = Ippo("Иппо", 7, 60, 5, 100)
    Ricardo = Ricardo("Рикардо", 6, 80, 12, 100)

    heroes = [Takamura, Ippo, Ricardo]

    for hero in heroes:
        hero.greet()
        hero.attack()
        hero.rest()
        print("_" * 30)