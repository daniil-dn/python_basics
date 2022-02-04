class Cell:

    def __init__(self, cells: int):
        if type(cells) is int:
            self.cells = cells
        else:
            raise ValueError('Только int может быть аргументом конструктора класаа Cell')

    def _is_cells_validator(func):
        def wrapper(*args):
            self, other = args
            if type(self) is type(other):
                return func(self, other)
            else:
                raise TypeError('действие допустимо только для экземпляров того же класса')

        return wrapper

    @_is_cells_validator
    def __add__(self, other):
        return Cell(self.cells + other.cells)

    @_is_cells_validator
    def __sub__(self, other):
        sub = self.cells - other.cells
        if sub > 0:
            return Cell(sub)
        else:
            raise ValueError('недопустимая операция')

    @_is_cells_validator
    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    @_is_cells_validator
    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    @_is_cells_validator
    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, number: int) -> str:
        cells = self.cells
        lvls_count = self.cells // number
        result = []
        for i in range(lvls_count + 1):
            if cells >= number:
                result.append('*' * number)
                cells -= number
            elif cells < number and cells != 0:
                result.append('*' * cells)

        return '\n'.join(result)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """
    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса
