"""
Есть два файла users.csv и hobby.csv:
в первом хранятся ФИО пользователей сайта,
а во втором — данные об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.

Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби (список строковых переменных).
Сохранить словарь в файл task_6_3_result.json. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом 1.


"""

import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    result_dict = dict()
    line_users_counter = 0
    line_hobby_counter = 0
    while True:
        with open(path_users_file, 'r', encoding='utf-8') as fr:
            fr.seek(int('0' + str(line_users_counter)))
            user_line = fr.readline()
            line_users_counter = fr.tell()
        with open(path_hobby_file, 'r', encoding='utf-8') as fr:
            fr.seek(int('0' + str(line_hobby_counter)))
            hobby_line = fr.readline()
            line_hobby_counter = fr.tell()
        if not user_line:
            break
        elif not hobby_line:
            result_dict.setdefault(user_line, None)
            continue
        hobby_line_list = [hobby.strip('\n') for hobby in hobby_line.split(',')]
        result_dict.setdefault(user_line.strip('\n').replace(',', ' '), hobby_line_list)

    return result_dict  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
