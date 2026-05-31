#наследование
# СуперКласс, родительский класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} base action'

# дочерний класс, subclass
class Magehero(Hero):
    def __init__(self, name, lvl, hp, mp):
        Hero.__init__(self, name, lvl, hp)
        self.mp = mp
    def action(self):
        return f'{self.name} this new action'

kirito = Hero("Kirito", 1, 100)
asuna = Magehero("asuna", 50, 100, 100)

class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        super().action()
        print("C")

class D(B, C):
    def action(self):
        super().action()
        print("D")

test_obj = D()

test_obj.action()
print(D.mro())