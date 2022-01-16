from itertools import islice

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

start = time.perf_counter()
lc_list = [num ** 2 for num in range(1, 10 *  + 1, 2)]
print(lc_list)
print(time.perf_counter() - start)

start = time.perf_counter()
gen_exp = (num ** 2 for num in range(1, 10 ** 7 + 1, 2))
lc_gen = [*gen_exp]
print(time.perf_counter() - start)
