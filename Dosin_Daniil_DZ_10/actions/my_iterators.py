class IterObj: ...  # просто класс-заглушка


class IteratorEnergy:
    """Объект-итератор, имитация иссякающей энергии"""
    def __init__(self, start=10):
        self.i = start + 1

    # У итератора есть метод __next__
    def __next__(self):
        self.i -= 1
        if self.i >= 1:
            return self.i
        else:
            raise StopIteration


class Accumulator(IterObj):
    """Объект Аккумулятор, поддерживающий интерфейс
        итерации (итерируемый объект)"""
    def __init__(self, energy=6):
        self.energy = energy

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор
        return IteratorEnergy(self.energy)


class Battery(IterObj):
    """Объект Батарейка, независимый итерируемый объект"""
    def __init__(self, energy=3):
        self.i = energy + 1

    # Метод __iter__ должен возвращать объект-итератор
    def __iter__(self):
        return self

    def __next__(self):
        self.i -= 1
        if self.i >= 1:
            return self.i
        else:
            raise StopIteration

