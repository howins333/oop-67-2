from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def get_health(self):
        return self.__health

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1
        print(f"Здоровье {self.name} увеличилось! Текущее здоровье: {self.__health}")

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        print(f"{self.name} использует магию!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")

if __name__ == "__main__":
    warrior = Warrior("Артур", 5, 100, 15)
    mage = Mage("Гэндальф", 7, 60, 5)
    assassin = Assassin("Эцио", 6, 80, 12)

    heroes = [warrior, mage, assassin]

    for hero in heroes:
        hero.greet()
        hero.attack()
        hero.rest()
        print("_" * 30)
