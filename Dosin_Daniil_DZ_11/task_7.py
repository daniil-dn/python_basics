class ComplexNums:
    def __init__(self, complex_obj=None, *n):
        for s in n[:2]:
            if type(s) is int:
                continue
            else:
                raise TypeError(f"нельзя создать комплексное число не от {type(s)}")
        self.complex_obj = complex(*n[:2])

    def __add__(self, other):
        result_obj = ComplexNums()
        result_obj.complex_obj = self.complex_obj + other.complex_obj
        return result_obj

    def __sub__(self, other):
        result_obj = ComplexNums()
        result_obj.complex_obj = self.complex_obj - other.complex_obj
        return result_obj

    def __mul__(self, other):

        result_obj = ComplexNums()
        result_obj.complex_obj = self.complex_obj * other.complex_obj
        return result_obj


def __str__(self):
    return str(self.complex_obj)


n1 = ComplexNums(1, 2)
print(n1)
n2 = ComplexNums(3, 4)
n = n1 + n2

print(n)
print(type(n))
n = n1 * n2
print(n)
print(type(n))
