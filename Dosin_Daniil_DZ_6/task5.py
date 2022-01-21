"""Решить задачу 4 и реализовать интерфейс командной строки,
чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
Проверить работу скрипта."""

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
        if not user_line and hobby_line:
            exit(1)
        elif not user_line:
            break
        elif not hobby_line:
            result_dict.setdefault(user_line.strip('\n').replace(',', ' '), None)
            continue
        hobby_line_list = [hobby.strip('\n') for hobby in hobby_line.split(',')]
        result_dict.setdefault(user_line.strip('\n').replace(',', ' '), hobby_line_list)

    return result_dict  # верните словарь, либо завершите исполнение программы кодом 1


def dataset_to_file(data_dict: dict, path: str) -> bool:
    """
    dict {'Иванов Иван Иванович': ['скалолазание', 'охота'],} to file like Иванов,Иван,Иванович: скалолазание,охота
    :param data_dict: seriolize dict to file
    :param path: path to file
    :return: True after closing file
    """
    with open(path, 'w', encoding='utf-8') as fw:
        for k, v in data_dict.items():
            full_name = k.replace(' ', ',')
            if v is None:
                hobby = ''
            else:
                hobby = ','.join(v)

            line_name_hobby = f'{full_name}: {hobby}\n'  # Иванов,Иван,Иванович: скалолазание,охота
            fw.write(line_name_hobby)
    return True


if len(sys.argv) >= 2 and sys.argv[1] == 'help':
    print('[path for file with names], [path for file with hobbies], [path for union file from those files]')
elif len(sys.argv) == 4:
    file, *paths = sys.argv
    dict_out = prepare_dataset(paths[0], paths[1])  # users.csv hobby.csv
    dataset_to_file(dict_out, paths[2])  # users_hobby.txt
else:
    exit(1)

# # print(dict_out)
# dataset_to_file(dict_out, "users_hobby.txt")
# with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
#     json.dump(dict_out, fw, ensure_ascii=False, indent=2)
