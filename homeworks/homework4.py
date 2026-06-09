rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()
    def convert_to_kgs(self):
        if self.currency not in rates:
            raise ValueError(f"Currency {self.currency} is not supported!")
        return self.amount * rates[self.currency]
    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only add Money object to another Money object")
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        total_amount = total_kgs / rates[self.currency]
        return Money(total_amount, self.currency)
    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only subtract Money object from another Money object")
        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        total_amount = total_kgs / rates[self.currency]
        return Money(total_amount, self.currency)
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Money can only be multiplied by a number")
        return Money(self.amount * other, self.currency)
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Money can only be divided by a number")
        if other == 0:
            raise ZeroDivisionError("Cannot divide money by zero!")
        return Money(self.amount / other, self.currency)
    def __str__(self):
        return f'{round(self.amount, 2)} {self.currency}'


money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
result = money1 + money2
print(result)