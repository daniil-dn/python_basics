from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            print(f"{func.__name__}({i}: type {type(i)})")
        for k, v in kwargs.items():
            print(f"{func.__name__}({k}: {v} with type {type(i)})")

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(4,3 ,3, k = 2)
