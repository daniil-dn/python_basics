import sys
from add_sale import PATH_FILE


def change_line_at_file(path: str, change_point: int = None, new_line: str = None) -> bool:
    """
    head-on solution
    get file lines from start to finish
    :param path: string with path to existed file
    :return: list
    """
    if change_point and new_line.replace(',', '').isdigit():
        with open(path, 'r+', encoding='utf-8') as f:
            list_out = list()
            line_counter = 1
            line = True
            while line:
                line = f.readline()
                if line_counter == change_point:
                    cur_point = f.tell()
                    f.seek(cur_point - 11)
                    new_line = new_line.ljust(10).replace(',', '.')
                    f.write(new_line)
                    print(f"{line.strip()} changed to {new_line}")
                    return True
                elif not line:
                    raise ValueError("<нет записи для редактирования>")
                line_counter += 1


if __name__ == "__main__":
    f_name, *args = sys.argv
    if (len(args) > 1) and (args[0].isdigit()):
        change_line_at_file(PATH_FILE, int(args[0]), args[1])

    else:
        raise ValueError("<Номер для редактироавния> <новое значение>")
