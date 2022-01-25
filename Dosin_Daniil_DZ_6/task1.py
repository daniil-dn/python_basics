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
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)
    :param line: line of nginx logs
    :return tuple: return tuple like (<remote_addr>, <request_type>, <requested_resource>)
    """
    line_list = line.split(' ')
    res = tuple([line_list[0], line_list[5].strip("'\""), line_list[6]])
    return res  # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line: break
        line_tuple = get_parse_attrs(line)
        list_out.append(line_tuple)

pprint(list_out)
