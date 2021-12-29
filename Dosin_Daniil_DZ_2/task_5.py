# + Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# + Вывести на экран эти цены через запятую в одну строку,
#   цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
#   Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
#   (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
#   (доказать, что объект списка после сортировки остался тот же).
# +Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

import random

# prices = [random.randint(10, 10000) / 100 for price in range(20)]

prices = [85.41, 91.07, 90.5, 13.79, 1.6, 66.88, 70.73, 68.9, 98.43, 76.43, 12.55, 76.88, 57.51, 78.09, 69.9, 12.56,
          43.49, 5.2, 77.5, 72.95]

# print(*[price_to_string(n) for n in prices])
#
# print(*[price_to_string(n) for n in sorted(prices)])  # функция sorted() не меняет список
#
# reversed_prices = sorted(prices, reverse=True)
# # print(reversed_prices)
# print(*[price_to_string(reversed_prices[n]) for n in reversed(range(0, 5))])

from random import uniform


def price_to_string(price):
    out_price_string = "{} руб {} коп"
    whole_rub = int(price)
    if type(price) is float:  # protected from integer as argument)
        cent_rub = str(price).split('.')[1][:2]
    else:
        cent_rub = "00"

    if cent_rub == "0":
        cent_rub = f"0{cent_rub}"
    elif cent_rub[0] == "0":
        pass  # если число вида 01, 02, 03... - оно валидно для вывода
    elif int(cent_rub) < 10:  # число 7 - это 70 в копейках
        cent_rub = f"{int(cent_rub)}0"

    if int(whole_rub) < 10:
        whole_rub = f"0{int(whole_rub)}"
    # print(whole_rub)
    return out_price_string.format(whole_rub, cent_rub)


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""

    str_out = ", ".join([price_to_string(price) for price in list_in])
    return str_out


# my_list = [round(uniform(10, 1000), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
my_list = [10.1, 26.37, 26.01, 26.1, 100.1, 100.10, 0.12, 0.01, 10.0, 2]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    return ["отсортированный результирующий список"]


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = ["список элементов в списке по убыванию"]
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = ["список из пяти самых больших элементов"]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
