import random


class Hero:
    def _init_(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def greet(self):
        return f'{self.name} greeting!'
    def attack(self):
        return "The Hero attacks!"
    def rest(self):
        return "The Hero rests!"

class Takamura(Hero):
    def _init_(self, name, lvl, hp, strength, defense):
        super()._init_(name, lvl, hp, strength)
        self.defense = defense
    def attack(self):
      return f'{self.name} hooked!'

class Ippo(Hero):
    def _init_(self, name, lvl, hp, strength, dodge_speed):
        super()._init_(name, lvl, hp, strength)
        self.dodge_speed = dodge_speed
    def attack(self):
        return f'{self.name} dempsey attack!'

class Ricardo(Hero):
    def _init_(self, name, lvl, hp, strength, reflex_speed):
        super()._init_(name, lvl, hp, strength)
        self.reflex_speed = reflex_speed
    def attack(self):
        return f'{self.name} ghost jab!'

Boxer = ['Ippo', 'Ricardo', 'Takamura']

def game():
    print("Welcome to Box sparring! and you want to exit write 'Joe'")
    while True:
        user = input("Choose your Boxer! [Ippo, Ricardo, Takamura]: ")
        if user == 'Joe':
            print('bye, Joe we never forget how you burned at fight')
            break
        print(f'You choose {user}')
        if user not in Boxer:
            print('you dont choose Boxer')
            continue
        programm = random.choice(Boxer)
        print(f'Enemy choose {programm}')
        if user == programm:
            print('Draw')
        elif (user == 'Takamura' and programm == 'Ricardo') or (user == 'Ricardo' and programm == 'Ippo') or (user == 'Ippo' and programm == 'Takamura'):
             print(f'{user} win!')
        else:
            print(f'{programm} win!')

if __name__ == '__main__':
    game()

