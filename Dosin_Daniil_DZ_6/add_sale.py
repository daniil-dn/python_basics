import sys


def add_note(note, path):
    with open(path, 'a+', encoding='utf-8') as fa:
        fa.write(f'{note}\n')


file_name, *args = sys.argv
file_path = "bakery.csv"
if args and args[0].replace(',', '').isdigit():
    add_note(args[0], file_path)
