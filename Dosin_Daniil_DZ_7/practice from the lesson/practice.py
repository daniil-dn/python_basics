import os.path
import os
from time import perf_counter
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("root: ", BASE_DIR)
print(__file__)

# get all files and directories
print(os.listdir(BASE_DIR))
parent_dir = os.path.dirname(BASE_DIR)
print("parant: ", parent_dir)
print(os.listdir(parent_dir))
print([filename for filename in os.listdir(BASE_DIR) if filename.endswith('.py')])

folder = os.path.join(BASE_DIR, "some_data")

if os.path.exists(folder):
    start = perf_counter()
    size_threshold = 15 * 2 ** 10
    small_files = [filename for filename in os.listdir(folder) if
                   os.stat(os.path.join(folder, filename)).st_size < size_threshold]
    print(len(small_files))
    print(perf_counter() - start)
    start = perf_counter()
    small_files = [obj for obj in os.scandir(folder) if
                   obj.stat().st_size < size_threshold]
    print(len(small_files))
    print(perf_counter() - start)
else:
    print(f"dirs {folder} doesn't exists")

new_dir_name = os.path.join(BASE_DIR, "some_date_2")
if not os.path.exists(new_dir_name) and os.path.exists(folder):
    os.rename(folder, new_dir_name)
# if not os.path.exists(folder) and os.path.exists(new_dir_name):
#     os.rename(new_dir_name, folder)

# os.rmdir(new_dir_name)  # OSError: [Errno 66] Directory not empty:

import shutil
import random

# shutil.rmtree(new_dir_name)

path_hello_file = os.path.join(BASE_DIR, "hello.txt")
path_summary_file = os.path.join(BASE_DIR, "summary.txt")

for _ in range(3):
    with open(path_hello_file, encoding='utf-8') as src:
        with open(path_summary_file, 'a', encoding='utf-8') as dst:
            head_size = random.randrange(21)
            print(head_size, src.read(head_size))
            # shutil.copyfileobj(src, dst)


def show_stat(f_path):
    stat = os.stat(f_path)
    print(f"{f_path}: perm - {oct(stat.st_mode)}, modify {stat.st_mtime:.0f}, access {stat.st_atime:.0f}")


path_summary_file_2 = os.path.join(BASE_DIR, '../trash/summery_clone.txt')
path_summary_file_3 = os.path.join(BASE_DIR, '../trash/summery_clone_2.txt')

show_stat(path_summary_file)
show_stat(shutil.copyfile(path_summary_file, path_summary_file_2))
show_stat(shutil.copy(path_summary_file, os.path.dirname(path_summary_file_2)))
show_stat(shutil.copy2(path_summary_file, path_summary_file_3))

# for root, dirs, files in os.walk(BASE_DIR):
#     print(root, len(dirs), len(files))

current_file_path = __file__

try:
    with open(current_file_path, 'r', encoding='utf-8') as fr:
        content = fr.read()
except Exception as err:
    print('catched: ', err)
except:
    pass
else:
    print(content)
    print('good job!')
finally:
    pass


def do_calc(f_path):
    f = open(f_path, 'a', encoding='utf-8')
    try:
        x = float(input('enter x val: '))
        y = float(input('enter y val: '))

    except Exception as err:
        print(f"wrong val: {err}")
    else:
        result = x / y
        f.write(f"{x} / {y} = {result} \n")
    finally:
        print(f"closing file - {f_path}")
        f.close()


try:
    path_calc_file = os.path.join(BASE_DIR, 'calc_log.txt')

    do_calc(path_calc_file)
except ZeroDivisionError as err:
    print(type(err).__name__)

primes: List[int] = []


def nums_get(length: int, *args) -> typing.List[int]:
    """
    Функция комплектования списка нужной длины length из нечетных чисел, выбираемых из итерируемых
    объектов, полученных в качестве аргументов функции
    :param length: требуемая длина результирующего списка
    :param args: some objects Iterable[int]
    :return: List[int]
    """
    nums = []
    try:
        for series in args:
            while series:
                random.shuffle(series)
                num = series.pop()
                if num % 2:
                    nums.append(num)
                if len(nums) == length:
                    raise Exception
    except Exception:
        return nums
    else:
        return nums


nums_1 = [3, 6, 8, 9, 17]
nums_2 = [16, 22, 25]
nums_3 = [7, 11, 18]
print(nums_get(5, nums_1, nums_2, nums_3))  # args = [nums_1, nums_2, nums_3]
