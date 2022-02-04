from typing import List
import itertools


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        if Matrix._check_valid_matrix(self, matrix):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def __str__(self):
        return self.__matrix_to_string

    def __add__(self, other):
        i = 0
        new_matrix = []
        while i < len(self.matrix):
            elements_on_lvl = itertools.zip_longest(self.matrix[i], other.matrix[i])
            sum_for_lvl = []
            for (i1, i2) in elements_on_lvl:
                sum_for_lvl.append(i1 + i2)
            new_matrix.append(sum_for_lvl)
            i += 1
        print(new_matrix)
        return Matrix(new_matrix)

    @property
    def __matrix_to_string(self):
        result_str = ''
        counter = 1
        for i in self.matrix:
            if not counter == 1:
                result_str = result_str + "\n| "

            else:
                counter += 1
                result_str = result_str + "| "

            for j in i:
                result_str += f'{j} '
            result_str += '|'
        return result_str

    def _check_valid_matrix(self, matrix):
        """
        Проверяет, содержит ли matrix только list в себе
        Проверяет размер каждого внутреннего элемента
        :matrix any type
        :return bool
        """
        if type(matrix) is list and matrix:
            length = len(matrix[0])
            for item in matrix:
                if type(item) is list and len(item) == length:
                    continue
                else:
                    return False
        else:
            return False
        return True


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2, 5], [3, 4, 5], [5, 6, 5]])
    second_matrix = Matrix([[6, 5, 5], [4, 3, 5], [2, 1, 5]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    n = first_matrix + second_matrix
    print(n)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
