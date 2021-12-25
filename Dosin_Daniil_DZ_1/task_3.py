# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
#   Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

def transform_string(number: int) -> str:
    b = "а"
    c = "ов"
    if number in range(11, 15):
        return f"{number} процент{c}"
    elif number % 10 == 1:
        return f"{number} процент"
    elif 1 < number % 10 < 5:
        return f"{number} процент{b}"
    elif number > 4:
        return f"{number} процент{c}"


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
