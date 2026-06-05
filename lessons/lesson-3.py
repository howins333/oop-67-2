class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password
        self._balance = balance

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return 'не верный пароль'

art = BankAccount("art", "artmarsh", 1000)

print(art._BankAccount__password)