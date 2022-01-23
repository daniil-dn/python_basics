# reading text files

file_1 = open('hello.txt', mode='r')
content = file_1.read()
print(content)
file_1.close()

file_2 = open('hello.txt', 'r', encoding='utf-8')
print(file_2.readline())
print(file_2.readline())
print(file_2.readline())
file_2.close()
file_3 = open('hello.txt', 'r', encoding='utf-8')
for line in file_3:  # \n
    print(line.strip())
file_3.close()

file_4 = open('hello.txt', 'r', encoding='utf-8')
print(file_4.readlines())
file_4.close()

# context manager
with open('qwerty.txt', 'w+', encoding='utf-16') as fw:
    print('i can write to file!!!', file=fw)
    fw.write('qwe\nafter slash\n')
    fw.writelines(['1 row', '2 row'])
with open('qwerty_2.txt', 'a+', encoding='utf-8') as fw:
    from datetime import datetime

    cur_time = datetime.now()
    fw.write(f'{cur_time}\n')

import random

task = [f'{random.randrange(1, 10)} {random.randrange(1, 10)}\n' for _ in range(10)]
with open('../trash/summator.txt', 'w', encoding='utf-8') as f:
    f.writelines(task)


def send_sum(val_1: int, val_2: int) -> int:
    """простейшая фкнеция суммирования двух значений"""
    return val_1 + val_2


res = 0
with open('../trash/summator.txt', 'r', encoding='utf-8') as fr:
    for row in fr.readlines():
        v1, v2 = row.split(' ')
        res = send_sum(*map(int, [v1, v2]))
print(res)
with open('../trash/summator.txt', 'r', encoding='utf-8') as fr:
    for row in fr:
        v1, v2 = row.split(' ')
        res = send_sum(*map(int, [v1, v2]))
print(res)
with open('../trash/summator.txt', 'r', encoding='utf-8') as fr:
    while True:
        row = fr.readline()
        if not row:
            break

        v1, v2 = row.split(' ')
        print(v1, v2)
        res = send_sum(*map(int, [v1, v2]))

print(res)

import json

my_dataset: list = [
    {'name': "тимур", 'level': 50},
    {'name': "анатолий", 'level': 49},
    {'name': "светала", 'level': 69}
]
with open('../trash/tasks_json.json', 'w', encoding='utf-8') as f:
    data_str = json.dumps(my_dataset, ensure_ascii=False, indent=4)
    f.write(data_str)
with open('../trash/tasks_json.json', 'r', encoding='utf-8') as f:
    import_data = json.loads(f.read())
    # import_data = json.load(f)
    print(type(import_data), import_data)

import pickle

data: dict = {
    1: [random.randrange(1, 10) for _ in range(5)],
    2: ('i am smth', b'binary data'),
    3: {None, True, False}
}
with open('../trash/tasks.pickle', 'wb') as f:
    # pickle.dump(data, f)
    data_pickle = pickle.dumps(data)
    f.write(data_pickle)
with open('../trash/tasks.pickle', 'rb') as f:
    # print(pickle.load(f, encoding='utf-8'))
    import_data = pickle.loads(f.read())
    print(import_data)

from time import perf_counter

nums = [random.random() * 10 ** 6 for _ in range(10 ** 6)]
start = perf_counter()

with open('../trash/random.json', 'w', encoding='utf-8') as fw:
    json.dump(nums, fw)

print('json saved', perf_counter() - start)
start = perf_counter()
with open('../trash/random.pickle', 'wb') as fw:
    pickle.dump(nums, fw)

print('pickle saved', perf_counter() - start)

start = perf_counter()

with open('../trash/random.json', 'r', encoding='utf-8') as fw:
    json.load(fw)

print('json saved', perf_counter() - start)
start = perf_counter()
with open('../trash/random.pickle', 'rb') as fw:
    pickle.load(fw)

print('pickle saved', perf_counter() - start)

chunk_size = 256
with open('../trash/random.json', 'r') as fr:
    str_data = []
    while True:
        chunk = fr.read(chunk_size)
        if not chunk:
            break
        str_data.append(chunk)
    nums_j = json.loads(''.join(str_data))
print(f'{type(nums_j)},{len(nums_j)}')

with open('../trash/random.pickle', 'rb') as fr:
    binary_data = bytearray()
    while True:
        chunk = fr.read(chunk_size)
        if not chunk:
            break
        binary_data.extend(chunk)
    nums_p = pickle.loads(binary_data)
print(f'{type(nums_j)},{len(nums_j)}')
