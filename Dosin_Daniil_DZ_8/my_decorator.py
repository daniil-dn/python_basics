def my_decorator(func):
    def wrapper(word):
        func(word)
        print('decorator')

    return wrapper


def say_hi(word):
    print(f"HI, {word}")


say_hi = my_decorator(say_hi)('ss')
