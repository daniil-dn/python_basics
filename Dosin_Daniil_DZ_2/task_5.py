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


def price_to_string(price):
    out_price_string = "{} руб {} коп"
    whole_rub = int(price)
    cent_rub = str(price).split('.')[1][:2]
    if whole_rub < 10:
        whole_rub = f'0{whole_rub}'

    if cent_rub == '' or cent_rub == "0":
        cent_rub = '00'
    elif int(cent_rub) < 10:
        cent_rub = f'0{int(cent_rub)}'

    return out_price_string.format(whole_rub, cent_rub)


# prices = [random.randint(10, 10000) / 100 for price in range(20)]

prices = [85.41, 91.07, 90.5, 13.79, 1.6, 66.88, 70.73, 68.9, 98.43, 76.43, 12.55, 76.88, 57.51, 78.09, 69.9, 12.56,
          43.49, 5.2, 77.5, 72.95]

print(*[price_to_string(n) for n in prices])

print(*[price_to_string(n) for n in sorted(prices)])  # функция sorted() не меняет список

reversed_prices = sorted(prices, reverse=True)
# print(reversed_prices)
print(*[price_to_string(reversed_prices[n]) for n in reversed(range(0, 5))])
