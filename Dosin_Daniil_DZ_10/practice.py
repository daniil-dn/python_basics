from actions.operators import Bottle

our_bottles = set()  # коллекция пузырей

bottle_1 = Bottle(1, our_bottles)
bottle_2 = Bottle(0.5, our_bottles)
bottle_3 = Bottle(1.5, our_bottles)
print(f'we have {our_bottles}')
print(bottle_1.warehouse)
for bottle in our_bottles:
    print(f'\t{bottle}')

bottle_3(3)
from actions.my_extra import Warehouse

warehouse = Warehouse()
# __setattr__
warehouse.note = 'текст моей записки'
warehouse.title = 'Заначка'
warehouse.title = 6
warehouse.download_bottles(*our_bottles)
bottle_4 = Bottle(0.5, warehouse.our_bottles)
bottle_5 = Bottle(2, warehouse.our_bottles)
print()

# __getitem__
accepted_bottle = warehouse[1.0]
print('Соответствует условию объема больше 1 или равного ему:', *accepted_bottle, sep='\n')
print()

# __eq__
warehouse_2 = Warehouse()
if warehouse == warehouse_2:
    print(f'Кол-во бутылок на складах "{warehouse.title}", "{warehouse_2.title}" равны')
else:
    print(f'Кол-во бутылок на складах "{warehouse.title}", "{warehouse_2.title}" не равны')
print()

# __lt__
if warehouse < warehouse_2:
    print(f'Название склада "{warehouse.title}" КОРОЧЕ названия "{warehouse_2.title}"')
else:
    print(f'Название склада "{warehouse.title}" ДЛИННЕЕ названия "{warehouse_2.title}"')
print()

# __iadd__
bottle_6 = Bottle(5, warehouse_2.our_bottles)
warehouse_2 += bottle_6
print()
print()

# Интерфейс
from actions.my_interfaces import VacuumCleaner, VacuumCleaner2

# robot_1 = VacuumCleaner()
robot_2 = VacuumCleaner2()
robot_2.on_off_action()
robot_2.say()
print()
# Декоратор @property
from actions.my_iterators_advance import IterObjAdv, AccumulatorAdv, BatteryAdv
from actions.power_exceptions import PowerMessage, IsNotEnergyObject, PowerEmpty


def check_energy_object(obj):
    """Проверяем относится объект к заряжаемым или разряжаемым"""
    if not isinstance(obj, IterObjAdv):
        raise IsNotEnergyObject()


def func_charging(obj: IterObjAdv):
    """Заряжаем объекты"""
    try:
        check_energy_object(obj)
        while True:
            obj.charging()
    except PowerMessage as err:
        print(err)


def energy_consumption_adv(obj: IterObjAdv):
    try:
        check_energy_object(obj)
        for remainder in obj:
            print(remainder)
        else:
            raise PowerEmpty(f'{obj.__class__.__name__} - разряжен')
    except PowerMessage as err:
        print(err)
acum2 = AccumulatorAdv()
acum2.count = 100
print(acum2)
print()

print("Используем энергию нашего аккумулятора:")
energy_consumption_adv(acum2)
print(acum2.energy)

print("Пытаемся зарядить аккумулятор:")
func_charging(acum2)
print()

print('Пробуем повторно использовать энергию аккумулятора:')
energy_consumption_adv(acum2)
print()

print()