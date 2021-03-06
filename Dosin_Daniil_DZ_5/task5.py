"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""


def get_uniq_numbers(src: list):
    tmp = set()
    res = list()
    for i in src:
        if i in tmp:
            if i in res:
                res.remove(i)
        else:
            res.append(i)
        tmp.add(i)
    return res


# refactored
def get_uniq_numbers(src: list):
    tmp = set()
    res_set = set()
    res_ordered_list = list()
    for i in src:
        if i in tmp:
            if i in res_set:
                res_set.remove(i)
        else:
            res_set.add(i)
        tmp.add(i)
    for item in src:
        if item in res_set:
            res_ordered_list.append(item)
    return res_ordered_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 111]
print(*get_uniq_numbers(src))
