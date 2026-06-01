class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты обьекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def rest(self):
        return print(f'{self.name} rested')

# обьект Ж экземпляр на основе класса
kirito = Hero('kirito', 45, 80)
asuna = Hero('Asuna', 111, 1111)

print(kirito.rest())
print(asuna.rest())
