import random
import sys


def add_note(note, path):
    note = note.replace(',', '.')
    with open(path, 'a+', encoding='utf-8') as fa:
        fa.write(f'{note}\n')


PATH_FILE = "bakery.csv"
if __name__ == "__main__":
    f_name, *args = sys.argv

    if args and args[0].replace(',', '').isdigit():
        add_note(args[0], PATH_FILE)
    else:
        raise ValueError("Ожидалась <цена>, например 129,2")
