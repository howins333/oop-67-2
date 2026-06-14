#FIRST PART OF HOMEWORK
# Библиотека colorama нужна для окрашивания текста
from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.GREEN + "Зеленый текст")
print(Fore.YELLOW + "Желтый текст")

print(Back.BLUE + Fore.BLACK + "Черный текст на синем фоне")

print(Fore.CYAN + Style.BRIGHT + "Яркий голубой текст")

# SECOND PART OF HOMEWORK

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(f"наши номера {nums}, наш таргет {target}")
print("Индексы чисел, дающих в сумме target:")
print(result)