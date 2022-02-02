from abc import ABC, abstractmethod
from .power_exceptions import PowerRestoreError, PowerComplete, PowerEmpty


class IteratorEnergy:
    """Объект-итератор, имитация иссякающей энергии"""
    def __init__(self, start=10):
        self.i = start + 1

    def __next__(self):
        self.i -= 1
        if self.i >= 1:
            return self.i
        else:
            raise StopIteration


class IterObjAdv(ABC):
    max_power: int = 0
    is_restore: bool = False
    __count: int = 1

    @property
    def count(self):
        """Доступное количество использований"""
        return self.__count

    @count.setter
    def count(self, value: int):
        if not isinstance(value, int):
            print('Кол-во использований должно быть целочисленным')
            return
        self.__count = value

    def __init__(self, energy: int = 0):
        self.energy = energy
        self.max_power = energy

    def __iter__(self):
        if not self.is_restore and not self.count:
            raise PowerEmpty()
        self.__count -= 1
        return IteratorEnergy(self.energy)

    def __str__(self):
        return f'{self.__class__.__name__}: Доступное количество использований {self.count}'

    def charging(self):
        """Постепенная зарядка элемента"""
        print(self.energy)
        if not self.is_restore:
            raise PowerRestoreError()
        if self.energy >= self.max_power:
            raise PowerComplete()
        self.energy += 1


class AccumulatorAdv(IterObjAdv):
    """Объект Аккумулятор, поддерживающий интерфейс итерации (итерируемый объект)"""
    is_restore = True

    def __init__(self, energy=7):
        super(AccumulatorAdv, self).__init__(energy)
        self.i = energy + 1


class BatteryAdv(IterObjAdv):
    """Объект Батарейка, поддерживающий интерфейс итерации (итерируемый объект)"""
    def __init__(self, energy=3):
        super(BatteryAdv, self).__init__(energy)
        self.i = energy + 1


