from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = []
        for i in args:

            if type(i) is int:
                result.append((f"{func.__name__}({func(i)}: type {type(i)})"))
        for k, v in kwargs.items():
            if type(v) is int:
                result.append((f"{func.__name__}({func(v)}: type {type(i)})"))
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
