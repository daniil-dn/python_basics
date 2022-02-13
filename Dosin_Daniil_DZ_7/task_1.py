import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"""


"""
folders_pattern = {
    "my_project": [
        {
            "settings": [],
            "mainapp": [],
            "adminapp": [],
            "authapp": [],
        }
    ]
}


def create_from_pattern(path: str, pattern: dict):
    """
    create directories with the pattern: dict

    :param path: path for the new directory
    :param pattern: structure for creating
    :return:
    """
    for fn, fc in pattern.items():
        folder_path = os.path.join(path, fn)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        if len(fc) > 0:
            for node in fc:
                create_from_pattern(folder_path, node)


create_from_pattern(BASE_DIR, folders_pattern)
