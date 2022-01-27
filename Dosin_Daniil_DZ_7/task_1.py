import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Хранение конфигурации я сделаю в task_2.py

"""


def create_new_dir(name: str, path: str = '') -> str:
    """
    create a new directory in path and check existing
    :param name: name of a new directory
    :param path: path for the new directory
    :return: path for the new directory
    """
    if not os.path.exists(os.path.join(path, name)):
        os.mkdir(os.path.join(path, name))
        return os.path.join(path, name)
    else:
        return os.path.join(path, name)


path_new = create_new_dir('my_project', BASE_DIR)
create_new_dir('settings', path_new)
create_new_dir('mainapp', path_new)
create_new_dir('adminapp', path_new)
create_new_dir('authapp', path_new)
