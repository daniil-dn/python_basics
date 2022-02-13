from typing import List


class ZeroDivError(ArithmeticError):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'Zero Division Error: {self.txt}'


def int_division(ls: List[str]) -> int:
    """
    Программа деления целых чисел
    Raise ZeroDivError, если второй элемент аргумента == 0
    Raise TypeError, если элементы аргумента - не int

    ls: list[str]
    return: int
    """
    if ls[1].isdigit() and int(ls[1]) == 0:
        raise ZeroDivError('Нельзя делить на ноль')
    elif ls[0].isdigit() and ls[1].isdigit():
        return int(ls[0]) // int(ls[1])
    else:
        raise TypeError("Вы ввели не число")


if __name__ == "__main__":
    while True:
        inputs = []
        for i in range(2):
            num = input('Введите число: ')
            inputs.append(num)
        try:
            print(int_division(inputs))
        except ZeroDivError as err:
            print(err)
            print("Повторите попытку")
            continue
        except TypeError as err:
            print(err)
            print("Повторите попытку")
            continue
        else:
            break
