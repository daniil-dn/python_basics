from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = []
        for i in args:
            print(f"{func.__name__}({i}: type {type(i)})")
            if type(i) is int:
                result.append(func(i))
        for k, v in kwargs.items():
            print(f"{func.__name__}({k}: {v} with type {type(i)})")
            if type(v) is int:
                result.append(func(v))
        return result

    return wrapper


@type_logger
def calc_cube(x) -> int:
    """
    Возводит число в куб
    :param x: int
    :return: int
    """
    return x ** 3


print(calc_cube(4, 3, 3, k=2))
