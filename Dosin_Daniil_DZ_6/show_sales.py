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


def get_all_file_lines(path):
    with open(path, 'r', encoding='utf-8') as fr:
        list_out = list()
        while True:
            line = fr.readline()
            if not line:
                break
            else:
                list_out.append(line.strip())
    return list_out


def get_file_lines_from(from_pos, path):
    list_in = get_all_file_lines(path)
    res_from = list_in[from_pos - 1:]
    return res_from


if __name__ == "__main__":
    f_name, *args = sys.argv
    if not args:
        print(get_all_file_lines(PATH_FILE), sep='\n')
    elif len(args) == 1 and args[0].isdigit():
        print(get_file_lines_from(int(args[0]), PATH_FILE))
    elif len(args) == 2 and args[0].isdigit() and args[1].isdigit():
        pass

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
