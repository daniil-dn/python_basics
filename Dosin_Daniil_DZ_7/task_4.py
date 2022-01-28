import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def stat_size(path_to_stat: str) -> dict:
    """
    выводит статистику для заданной папки в виде словаря,
    в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
    а значения — общее количество файлов

    :param path_to_stat: where to find all files to stat
    :return: dict with statistics of file sizes
    """
    res_dict: dict = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0,
    }

    for root, dirs, files in os.walk(path_to_stat):
        # print(root, dirs, files)
        for file in files:
            # print(os.stat(os.path.join(root, file)).st_size)
            if os.stat(os.path.join(root, file)).st_size < 100:
                res_dict[100] += 1
            elif 100 < os.stat(os.path.join(root, file)).st_size < 1000:
                res_dict[1000] += 1
            elif 1000 < os.stat(os.path.join(root, file)).st_size < 10000:
                res_dict[10000] += 1
            elif 10000 < os.stat(os.path.join(root, file)).st_size < 100000:
                res_dict[100000] += 1
    return res_dict


path_stat = os.path.join(BASE_DIR, 'practice_from_the_lesson')
print(stat_size(path_stat))
