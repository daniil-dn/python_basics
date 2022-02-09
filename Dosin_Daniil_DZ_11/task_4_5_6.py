import copy
import datetime
from abc import ABC, abstractmethod


class Warehouse:

    def __init__(self, title='default', listing: list = None):
        self.list_equipment = []
        self.dict_equpment = {}
        self.title = title
        if listing is not None:
            for item in listing:
                item._add_warehouse(self)
                self.list_equipment.append(item)
                if not self.dict_equpment.get(item.__class__.__name__, 0):
                    self.dict_equpment.setdefault(item.__class__.__name__, 1)
                else:
                    self.dict_equpment[item.__class__.__name__] += 1

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    def add_equipment(self, *things):
        for item in things:
            if self.check_equipment_year(item):
                item._add_warehouse(self)
                self.list_equipment.append(item)
                if not self.dict_equpment.get(item.__class__.__name__, 0):
                    self.dict_equpment.setdefault(item.__class__.__name__, 1)
                else:
                    self.dict_equpment[item.__class__.__name__] += 1
            else:
                print("This Office Equipment is very old for this warehouse")

    def remove_equipment(self, *things):
        for item in things:
            if item in self.list_equipment:
                item._remove_warehouse(self)
                self.list_equipment.remove(item)
            else:
                print("Данного оборудования нет на складе")
                continue
            # если элемента нет в словаре или количество элементов 0, то мы пропускаем этот цикл
            if not self.dict_equpment.get(item.__class__.__name__, 0) and self.dict_equpment.get(
                    item.__class__.__name__) == 0:
                self.dict_equpment.setdefault(item.__class__.__name__, 0)
                continue
            else:
                self.dict_equpment[item.__class__.__name__] -= 1

    def print_storing_equipments(self):
        for item in self.list_equipment:
            print(item)

    def clean_warehouse(self):
        for item in self.list_equipment:
            item._remove_warehouse(self)
        self.dict_equpment = {}
        self.list_equipment = []

    @staticmethod
    def check_equipment_year(equipment_to_check) -> bool:
        if equipment_to_check.year < 2000:
            return False
        else:
            return True

    def __add__(self, other):
        if type(other) is Warehouse:
            items = self.list_equipment
            items.extend(other.list_equipment)
            return Warehouse(listing=items)
        else:
            print("this is not warehouse with equipment")


class OfficeEquipment(ABC):
    def __init__(self, model, year=datetime.date.today().year, parent=None):
        self.model = model
        self.parent = parent
        self.year = year

    def _add_warehouse(self, warehouse):
        self.parent = warehouse

    def _remove_warehouse(self, warehouse):
        self.parent = None

    @abstractmethod
    def print_model(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def print(self, str) -> None:
        print(f'{str} from printer: {self.model}')

    def print_model(self):
        print(f'printer: {self.model}')

    def __str__(self):
        return (f'printer: {self.model}')


class Scanner(OfficeEquipment):
    def scan(self, page) -> str:
        print(f'scanner: {self.model}')
        return page

    def print_model(self):
        print(f'scanner: {self.model}')

    def __str__(self):
        return (f'scanner: {self.model}')


class Copier(OfficeEquipment):
    def copy(self, page) -> object:
        print(f'copier: {self.model}')
        return copy.copy(page)

    def print_model(self):
        print(f'copier: {self.model}')

    def __str__(self):
        return (f'copier: {self.model}')


printer = Printer('printer2000')

xerox = Copier('xerox - dc30')

scanner = Scanner('super scanner 88')

warehouse1 = Warehouse()
warehouse1.add_equipment(printer)
warehouse1.add_equipment(xerox)
warehouse1.add_equipment(scanner)
printer2 = Printer('printer234234')
xerox2 = Copier('xerox 2342- dc30')
scanner2 = Scanner('super2423 sca234234nner 88')
warehouse2 = Warehouse('warehouse2')
warehouse2.add_equipment(printer2, scanner2, xerox2)


new_warehouse = warehouse1 + warehouse2
new_warehouse.remove_equipment(printer2)
new_warehouse.remove_equipment(printer)
new_warehouse.remove_equipment(printer)
print(new_warehouse.dict_equpment)
print(warehouse1.dict_equpment)
print(warehouse2.dict_equpment)
