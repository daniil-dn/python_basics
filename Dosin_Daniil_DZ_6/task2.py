"""Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>) . Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""

from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line_list = line.split(' ')
    res = tuple([line_list[0], line_list[5].strip("'\""), line_list[6]])
    return res  # кортеж значений <remote_addr>, <request_type>, <requested_resource>


def add_spammer(spammers_list: dict, line_tuple: tuple) -> bool:
    """
    add spammer to spammers list by reference
    :param spammers_list: reference of spammers list
    :param line_tuple:tuple like <remote_addr>, <request_type>, <requested_resource>
    :return: True if spammer is already in spammers list or False if there weren't this spammer
    """
    if line_tuple[0] in spammers_list:
        spammers_list[line_tuple[0]] += 1
        return True
    else:
        spammers_list.setdefault(line_tuple[0], 1)
        return False


list_out = list()
spammers = dict()  # {remote_addr: requests count}
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line: break
        line_tuple = get_parse_attrs(line)
        list_out.append(line_tuple)
        add_spammer(spammers, line_tuple)  # change spammers list by reference
print(spammers)
max_spammer = sorted(spammers.items(), key=lambda x: x[1])[-1]

pprint(list_out)
print('spammer is ', max_spammer[0])
