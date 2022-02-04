import sys
from time import perf_counter

from add_sale import PATH_FILE


def get_all_file_lines_generator(path):
    with open(path, 'r', encoding='utf-8') as fr:
        while True:
            line = fr.readline()
            if not line:
                break
            else:
                yield line.strip()


def get_file_lines_from_to(path: str, start: int = 1, finish: int = None) -> list:
    """
    head-on solution
    get file lines from start to finish
    :param path: string with path to existed file
    :return: list
    """

    with open(path, 'r', encoding='utf-8') as fr:
        list_out = list()
        line_counter = 1
        line = True
        while line and not (finish is not None and line_counter > finish):
            line = fr.readline()
            if line_counter >= start and line:
                list_out.append(line.strip())
            line_counter += 1
    return list_out


if __name__ == "__main__":
    f_name, *args = sys.argv
    if not args:
        print(*get_file_lines_from_to(PATH_FILE), sep='\n')
    elif len(args) == 1 and args[0].isdigit():
        args = list(map(int, args))
        print(*get_file_lines_from_to(PATH_FILE, args[0]), sep='\n')
    elif len(args) == 2 and args[0].isdigit() and args[1].isdigit():
        args = list(map(int, args))
        print(*get_file_lines_from_to(PATH_FILE, args[0], args[1]), sep='\n')
    else:
        raise ValueError("<Номер записи с...> <Номер записи до...>")
# start_1 = perf_counter()
# print(*get_all_file_lines_generator(PATH_FILE), sep='\n')
# end_1 = perf_counter()
# print('1- ', end_1 - start_1)
#
# start = perf_counter()
# print(get_all_file_lines(PATH_FILE), sep='\n')
# print('1- ', end_1 - start_1)
# print('2- ', perf_counter() - start)
"""# функция без генератора быстрее"""
