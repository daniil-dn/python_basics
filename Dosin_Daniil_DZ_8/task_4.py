from functools import wraps


def val_checker(cb_validator=None):
    print("val_checker")

    def _val_checker(func):
        print("_____val_checker")

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("wrapper")
            for arg in args:
                if cb_validator is not None and cb_validator(arg):
                    return func(arg)
                else:
                    raise ValueError

        return wrapper

    return _val_checker


def validator(to_valid):
    if type(to_valid) is not int:
        return False
    elif type(to_valid) is int and to_valid < 0:
        return False
    else:
        return True


@val_checker(validator)  # не забудьте про аргумент-функцию
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(4))
    # print(calc_cube.__name__)
    try:
        print(calc_cube('ss'))
    except ValueError as err:
        print(type(err))
