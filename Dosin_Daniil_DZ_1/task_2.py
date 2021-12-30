# TODO Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# + a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#   Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#   Внимание: использовать только арифметические операции!
# + b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#   сумма цифр которых делится нацело на 7.

# + * Решить задачу под пунктом b, не создавая новый список.


def sum_list_1(dataset: list):
    res = 0
    for val in dataset:
        sum_nums = 0
        n = val
        while n > 0:
            dig = n % 10
            sum_nums += dig
            n = n // 10
        if sum_nums % 7 == 0:
            res += val
    return res


def sum_list_2(dataset: list):
    # in_list = [n + 17 for n in in_list]
    res = 0
    for val in dataset:
        val += 17
        sum_nums = 0
        n = val
        while n > 0:
            dig = n % 10
            sum_nums += dig
            n = n // 10
        if sum_nums % 7 == 0:
            res += val
    return res


my_list = [n ** 3 for n in range(0, 1000) if n % 2 != 0]  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
