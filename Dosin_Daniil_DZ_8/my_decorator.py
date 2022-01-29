def my_decorator(func):
    def wrapper(word):
        func(word)
        print('decorator')

    return wrapper


def say_hi(word):
    print(f"HI, {word}")


# # say_hi = my_decorator(say_hi)('ss')

def my_decorator_args(decorator_arg):
    print(decorator_arg)

    def _my_decorator_args(func):
        def wrapper(word):
            func(word)
            print('decorator')

        return wrapper

    return _my_decorator_args


def say_word(word):
    print(f"HI, {word}")


say_word = my_decorator_args('docorator\'s arg')(say_word)
say_word('s')

