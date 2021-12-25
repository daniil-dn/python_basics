# TODO Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# + a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# + b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

# + * Решить задачу под пунктом b, не создавая новый список.


def return_list_cubes():
    return [n ** 3 for n in range(0, 1000) if n % 2 != 0]


def sum_div_7(in_list: list):
    res = 0
    for val in in_list:
        sum = 0
        n = val
        while n > 0:
            dig = n % 10
            sum += dig
            n = n // 10
        if sum % 7 == 0:
            res += val
    return res


def sum_div_7_plus_17(in_list: list):
    in_list = [n + 17 for n in in_list]
    res = 0
    for val in in_list:
        sum = 0
        n = val
        while n > 0:
            dig = n % 10
            sum += dig
            n = n // 10
        if sum % 7 == 0:
            res += val
    return res


print(sum_div_7(return_list_cubes()))
print(sum_div_7_plus_17(return_list_cubes()))
