from itertools import islice
import sys

test_gen = (n * 8 for n in range(100))
print(test_gen.__next__())
print(islice(test_gen, 10))
print(*islice(test_gen, 10))

print(sum(test_gen))
print(sum(test_gen))


# yield
def letter_generator(start: str, end: str):
    for code in range(ord(start), ord(end) + 1):
        # print("start funx generator")
        yield chr(code)
        # print("end funx generator")


testing = letter_generator("a", "z")
# print(*testing)
# print(*islice(testing, 10))
import time

# start = time.perf_counter()
# lc_list = [num ** 2 for num in range(1, 10 ** 7 + 1, 2)]
# # print(lc_list)
# print(time.perf_counter() - start)
#
# start = time.perf_counter()
# gen_exp = (num ** 2 for num in range(1, 10 ** 7 + 1, 2))
# lc_gen = [*gen_exp]
# print(time.perf_counter() - start)
#
# print(sys.getsizeof(lc_list))
# print(sys.getsizeof(lc_gen))
#


matrix_1 = [
    [1, 1, 1],
    [2, 2, 2]
]
matrix_2 = [
    [3, 3, 3],
    [4, 4, 4]
]
matrix_sum = []
for i in range(len(matrix_1)):
    matrix_row = []
    for j in range(len(matrix_1[i])):
        sum_el = matrix_1[i][j] + matrix_2[i][j]
        matrix_row.append(sum_el)
    matrix_sum.append(matrix_row)
print(matrix_sum)

box = 'pen pencil cat dog paper pen money dog cat paper'.split()
unique_box_2 = set()
tmp = set()
for el in box:
    if el not in tmp:
        unique_box_2.add(el)
    else:
        unique_box_2.discard(el)
    tmp.add(el)

print(tmp, unique_box_2)

unique_box_2 = set()
tmp = set()
