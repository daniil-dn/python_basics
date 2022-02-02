from abc import ABC, abstractmethod


class Robot(ABC):
    """Абстрактный класс робота"""

    def __init__(self):
        self.switcher: bool = False

    @abstractmethod
    def say(self):
        pass

    def on_off_action(self):
        self.switcher = not self.switcher
        if self.switcher:
            print(f'{self.__class__.__name__}: включился')
        else:
            print(f'{self.__class__.__name__}: вЫключился')


class VacuumCleaner(Robot):
    """Робот пылесос"""
    pass


class VacuumCleaner2(Robot):
    """Робот-пылесос усовершенствованная модель"""

    def say(self):
        print('Пшш-шш')
