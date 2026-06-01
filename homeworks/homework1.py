class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


hero1 = Hero("Арагорн", 10, 100, 20)
hero2 = Hero("Джайна", 12, 80, 15)

print(" Проверка Первого Героя ")
hero1.greet()
print(f"Сила до атаки: {hero1.strength}")
hero1.attack()
print(f"Сила после атаки: {hero1.strength}")

print("\n Проверка Второго Героя ")
hero2.greet()
print(f"Здоровье до отдыха: {hero2.health}")
hero2.rest()
print(f"Здоровье после отдыха: {hero2.health}")
