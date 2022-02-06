from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def calculate(self):
        """
        расчёты расхода ткани
        """
        pass


class Coat(Clothes):

    def __init__(self, size):
        try:
            self.size = float(size)

        except ValueError:
            print('could not convert string to float: ', size)
            exit(1)

    @property
    def calculate(self):
        """
        расчёты расхода ткани
        """
        return float("%.2f" % (self.size / 6.5 + 0.5))


class Costume(Clothes):
    def __init__(self, length):
        try:
            self.length = float(length)
        except ValueError:
            print('could not convert string to float: ', length)
            exit(1)

    @property
    def calculate(self):
        """
        расчёты расхода ткани
        """
        return float("%.2f" % (2 * self.length + 0.3))


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)
    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
