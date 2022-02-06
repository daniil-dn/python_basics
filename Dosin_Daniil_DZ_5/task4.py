import time
import random
from itertools import islice


def get_numbers(src: list):
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
            yield src[i]


src = [random.randint(0, 10009) for _ in range(10 ** 7)]

start = time.perf_counter()
sum(get_numbers(src))
time_1 = time.perf_counter() - start
print(time_1)

start = time.perf_counter()
nums = [i for i in range(1, len(src)) if src[i] > src[i - 1]]
sum(nums)
print("generator time is ", time_1)
print("list comprehension time is", time.perf_counter() - start)
