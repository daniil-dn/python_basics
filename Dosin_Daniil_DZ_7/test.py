def main(argv):
    program, position, new_value = argv
    line_len = 10
    pos_b = (int(position) - 1) * (line_len + len('\n'))
    file_name = 'bakery.csv'
    with open(file_name, 'r+', encoding='utf-8') as f1:
        last_line = f1.seek(0, 2)
        if last_line <= pos_b:
            raise TypeError(f"Запись №{position} отсутствует")
        else:
            f1.seek(pos_b)
            f1.write(f'{new_value.ljust(line_len, " ")}\n')


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        exit(main(sys.argv))
    else:
        raise TypeError("Ожидались <номер_записи_для_редактирования> <новое_значение>")
