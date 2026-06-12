# | Оператор | Магический метод | Пример   |
# | -------- | ---------------- | -------- |
# | `+`      | `__add__`        | `a + b`  |
# | `-`      | `__sub__`        | `a - b`  |
# | `*`      | `__mul__`        | `a * b`  |
# | `/`      | `__truediv__`    | `a / b`  |
# | `//`     | `__floordiv__`   | `a // b` |
# | `%`      | `__mod__`        | `a % b`  |
class Test:

    def __init__(self, value):
        self.value = value
        self.view_count = 0

    def __call__(self, *args, **kwargs):
        self.view_count += 1

    def __str__(self):
        return self.value

    def __add__(self, other):
        if type(self) == type(other):
            return self.value + other.value
        else:
            return "Классы не равны!!"
    # obj[2]
    def __getitem__(self, item):
        print(self.value)
        print(item)
       # return self.value[item]

# int_1 = Test(12)
# int_2 = Test(13)
# int_3 = int_1 + int_2
# print(int_3)

# my_list_2 = Test([1,2,34,45])
# my_list = [1,2,34,5,6,7]
# print(my_list_2[2])

# my_int = 123
# my_int_2 = 123
# my_list = [1,2,34,5,6,7]
# my_str = "text"
# int_2 = Test("13")
# int_2()
# int_2()
# print(int_2.view_count)
# int_2()
# print(int_2.view_count)
# print(my_int)
# print(my_str)
# print(my_list)
# print(int_2)

class Money:

    def convert_money(self):
        pass

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return  self.value + other.value
        else:
            print("Не можем сложить разный валюты")

