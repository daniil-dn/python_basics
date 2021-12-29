# todo обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов
# from io import StringIO

import timeit
import time

# WORK IN PLACE
def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    index_of_int_list = [n for n in range(len(list_in)) if list_in[n].strip('=+-;:"\'').isdigit()]
    for ind in reversed(index_of_int_list):
        list_in.insert(ind, '"')
        list_in.insert(ind + 2, '"')
    # ноль перед одностоящим числом
    for i in range(len(list_in)):
        element = list_in[i]
        # print(element)
        if element.strip('=+-;:"\'').isdigit():
            if not element[0].isdigit() and int(element.strip('=+-;:"\'')) < 10:
                list_in[i] = '{}0{}'.format(element[0], int(element.strip('=+-;:"\'')))

            elif int(element.strip('=+-;:"\'')) < 10:
                list_in[i] = '0{}'.format(int(element.strip('=+-;:"\'')))
    # CONVERT LIST TO STRING
    str_out_list = []
    i = 0
    while i < len(list_in):
        element = list_in[i]
        if i < len(list_in) - 2 and (element in ["'", '"'] and list_in[i + 1].strip('+-').isdigit()):
            str_out_list.append(f"{element}")
            str_out_list.append(f"{list_in[i + 1]}")
            i += 2
        else:
            str_out_list.append(f"{element} ")
            i += 1
    return ''.join(str_out_list)


# WORK IN PLACE
def convert_list_in_str_concatenate(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    index_of_int_list = [n for n in range(len(list_in)) if list_in[n].strip('=+-;:"\'').isdigit()]
    for ind in reversed(index_of_int_list):
        list_in.insert(ind, '"')
        list_in.insert(ind + 2, '"')
    # ноль перед одностоящим числом
    for i in range(len(list_in)):
        element = list_in[i]
        # print(element)
        if element.strip('=+-;:"\'').isdigit():
            if not element[0].isdigit() and int(element.strip('=+-;:"\'')) < 10:
                list_in[i] = '{}0{}'.format(element[0], int(element.strip('=+-;:"\'')))

            elif int(element.strip('=+-;:"\'')) < 10:
                list_in[i] = '0{}'.format(int(element.strip('=+-;:"\'')))
    # CONVERT LIST TO STRING
    str_out_list = ''
    i = 0
    while i < len(list_in):
        element = list_in[i]
        if i < len(list_in) - 2 and (element in ["'", '"'] and list_in[i + 1].strip('+-').isdigit()):
            str_out_list += element
            str_out_list += list_in[i + 1]
            i += 2
        else:
            str_out_list += element
            str_out_list += " "
            i += 1
    return str_out_list


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+50', 'градусов']*2000
print("id before: ", id(my_list))
start = time.time()
result = convert_list_in_str(my_list)
end = time.time()
print(end - start)


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+50', 'градусов']*2000
start = time.time()
result_test = convert_list_in_str_concatenate(my_list)
end = time.time()
print(end - start)
