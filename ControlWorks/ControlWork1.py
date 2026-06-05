from abc import ABC, abstractmethod


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero: Hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return self.__password == password

    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Баланс: {self._balance} SOM"

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return "Ошибка: Сложение возможно только с другим банковским счетом!"

        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl


class AbstractSms(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(AbstractSms):
    def send_otp(self, phone):
        return f"Код подтверждения отправлен на номер {phone}"


if __name__ == "__main__":
    merlin = MageHero("Merlin", 50, 100, 150)
    gandalf = MageHero("Gandalf", 50, 120, 200)
    conan = WarriorHero("Conan", 50, 300, 0)

    acc1 = BankAccount(merlin, 5000, "magic_pass")
    acc2 = BankAccount(gandalf, 3000, "shadow_pass")
    acc3 = BankAccount(conan, 4500, "steel_pass")

    print(acc1.hero.action())
    print(acc3.hero.action())

    print(acc1)
    print(acc2)

    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    print("\n--- Проверка add ---")
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)

    print("\n--- Проверка eq ---")
    print("Mage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)

    sms = KGSms()
    print("\n" + sms.send_otp("+996777123456"))