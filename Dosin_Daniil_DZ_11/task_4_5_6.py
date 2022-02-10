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
                item.add_warehouse(self)
                self.list_equipment.append(item)
                if not self.dict_equpment.get(item.__class__.__name__, 0):
                    self.dict_equpment.setdefault(item.__class__.__name__, 1)
                else:
                    self.dict_equpment[item.__class__.__name__] += 1

    def __del__(self):
        self.clean_warehouse(True)
        # del self

    def __add__(self, other):
        """
        Возвращает новый склад со всем оборудованием
        Удаляет все с двух складывающихся складов.
        """
        if type(other) is Warehouse:
            items = self.list_equipment.copy()
            items.extend(other.list_equipment.copy())
            n_warehouse = Warehouse(listing=items)
            for i in items:
                i.add_warehouse(n_warehouse)
            self.clean_warehouse(False)
            other.clean_warehouse(False)
            return n_warehouse
        else:
            print("this is not warehouse with equipment")

    def __gt__(self, other):  # >
        return len(self.list_equipment) > len(other.list_equipment)

    def __ge__(self, other):  # >
        return len(self.list_equipment) >= len(other.list_equipment)

    def __lt__(self, other):
        return len(self.list_equipment) < len(other.list_equipment)

    def __le__(self, other):
        return len(self.list_equipment) <= len(other.list_equipment)

    def __eq__(self, other):
        return len(self.list_equipment) == len(other.list_equipment)

    def __call__(self, *args) -> bool:
        """
        Добавляет оборудование на склад
        Принимает несколько аругментов
        """
        self.add_equipment(*args)
        return True

    def __iter__(self):
        for item in self.list_equipment:
            yield item
        # return self

    def __next__(self):
        for item in self.list_equipment:
            yield item

    @staticmethod
    def instance_validator(func):
        def wrapper(*args):
            remove_add_str = "удалить со" if func.__name__.find('remove') > 0 else 'добавить в'
            self, *other = args
            list_equipments_to_add = []
            for item in other:
                if type(item) is list:
                    wrapper(self, *item)
                else:
                    if isinstance(item, OfficeEquipment):
                        list_equipments_to_add.append(item)
                        continue
                    else:
                        print(f"Это нельзя {remove_add_str} склад - это не оборудование для офиса: {type(item)}")
                    return None
                    # raise TypeError(f"Это нельзя добавить на склад - это не оборудование для офиса: {type(item)}")

            return func(self, *list_equipments_to_add)

        return wrapper

    @staticmethod
    def year_validator(func):
        def wrapper(*args):
            self, year = args
            if year is not None and type(year) is int and 0 < year < datetime.date.today().year:
                return func(*args)

        return wrapper

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @instance_validator
    def add_equipment(self, *things) -> None:
        """
        Проверяет, чтобы на склад попадали только
        """
        for item in things:
            if self.check_equipment_year(item):
                item.add_warehouse(self)
                self.list_equipment.append(item)
                item_cls_name = item.__class__.__name__
                if not self.dict_equpment.get(item_cls_name):
                    self.dict_equpment.setdefault(item_cls_name, 1)
                else:
                    self.dict_equpment[item_cls_name] += 1
            else:
                print("This Office Equipment is very old for this warehouse")

    @instance_validator
    def remove_equipment(self, *things):
        for item in things:
            if item in self.list_equipment:
                item.clear_warehouse()
                self.list_equipment.remove(item)
            else:
                print("Данного оборудования нет на складе")
                continue
            item_cls_name = item.__class__.__name__
            # если элемента нет в словаре или количество элементов 0, то мы пропускаем этот цикл
            if not self.dict_equpment.get(item_cls_name) and self.dict_equpment.get(
                    item_cls_name) == 0:
                self.dict_equpment.setdefault(item_cls_name, 0)
                continue
            else:
                self.dict_equpment[item_cls_name] -= 1

    def print_storing_equipments(self):
        for item in self.list_equipment:
            print(item)
        print(self.dict_equpment)

    def clean_warehouse(self, items_parenting=False):
        if items_parenting:
            for item in self.list_equipment:
                item.clear_warehouse()
        self.dict_equpment = {}
        self.list_equipment = []

    @staticmethod
    def check_equipment_year(equipment_to_check) -> bool:
        if equipment_to_check.year < 2000:
            return False
        else:
            return True


class OfficeEquipment(ABC):
    def __init__(self, model, year=datetime.date.today().year, parent=None):
        self.model = model if type(model) is str else 'default model'
        self.parent = year if type(year) is Warehouse else None
        self.year = year if type(year) is int else datetime.date.today().year
        self.__cls_name = self.__class__.__name__

    def add_warehouse(self, warehouse):
        self.parent = warehouse

    def clear_warehouse(self):
        self.parent = None

    @property
    def cls_name(self):
        return self.__cls_name

    @cls_name.setter
    def cls_name(self, name):
        print("You cant change it - your name is ", self.__cls_name)

    @abstractmethod
    def print_model(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def print(self, string) -> None:
        print(f'{string} from printer: {self.model}')

    def print_model(self):
        print(f'printer: {self.model}')

    def __str__(self):
        return f'printer: {self.model}'


class Scanner(OfficeEquipment):
    def scan(self, page) -> str:
        print(f'scanner: {self.model}')
        return page

    def print_model(self):
        print(f'scanner: {self.model}')

    def __str__(self):
        return f'scanner: {self.model}'


class Copier(OfficeEquipment):
    def copy(self, page) -> object:
        print(f'copier: {self.model}')
        return copy.copy(page)

    def print_model(self):
        print(f'copier: {self.model}')

    def __str__(self):
        return f'copier: {self.model}'


printer = Printer('printer2000')

xerox = Copier('xerox - dc30')

scanner = Scanner('super scanner 88')

warehouse1 = Warehouse()
warehouse1.add_equipment([printer, xerox, scanner])
printer2 = Printer('printer234234')
xerox2 = Copier('xerox 2342- dc30')
scanner2 = Scanner('super2423 sca234234nner 88')
warehouse2 = Warehouse('warehouse2')
warehouse2.add_equipment(printer2, scanner2, xerox2)

print(warehouse1 > warehouse2)
print(warehouse1 >= warehouse2)
print(warehouse1 < warehouse2)
print(warehouse1 <= warehouse2)
print(warehouse1 == warehouse2)
# del warehouse2
new_warehouse = warehouse1 + warehouse2
new_warehouse.remove_equipment(printer2)
new_warehouse.remove_equipment(printer)
new_warehouse.remove_equipment(1)
new_warehouse.remove_equipment(printer)
print(new_warehouse.dict_equpment)
for i in new_warehouse:
    print(i)
