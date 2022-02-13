"""
Урок 11. Объектно-ориентированное программирование. Полезные дополнения
"""

# Пример ООП-программы
"""
Предварительное проектирование:

1. Сформулировать задачу.
2. Определить объекты предметной области, участвующие в решении задачи.
3. Выделить классы, на основе которых генерируются объекты
    При необходимости определить базовые классы и классы-потомки.
4. Установить основные атрибуты и методы объектов.
5. Создать классы, их атрибуты и методы.
6. Создать объекты классов.
7. Выполнить итоговое решение задачи, организовав взаимодействие объектов.

Проект нашей ООП-программы под названием "Cheker доступности ресурсов"
1. Создать программу позволяющую с заданной периодичностью проверять доступность внешних сайтов
2. Объектами предметной области является информация о доступности сайтов
3. Определение классов программы:
    * свои наборы Exceptions
    * Checker - исполнитель запросов
    * Storage - хранилище проверяемых ресурсов
    * SiteInfo - объекты внешних ресурсов
4. Глобальные атрибуты и методы объектов:
    * Checker: атрибуты хранилища и обработчика информации, методы организации запросов к внешним ресурсам
    * Storage: методы добавления и удаления объектов внешних ресурсов, итерирование по хранимым объектам
    * SiteInfo: атрибуты url, name
5 - 7 достигается разработкой

https://refactoring.guru/ru/design-patterns/python - популярные паттерны проектирования
"""

# from checker import Checker
# import time
#
#
dataset = {
    'GeekBrains': 'https://gb.ru',
    'VK': 'https://vk.com',
    'Почемучка': 'http://ps.fail',
    'Мурзилка': 'https://gb.ru/page/error/123.jpeg'
}
#
# checker = Checker.prepare_app(dataset)
# checker.get_info()
# time.sleep(5)
# checker.get_info()


# Атрибуты и встроенные методы объектов классов
import checker as my_module

print(my_module.__doc__,
      my_module.Checker.get_info.__doc__)   # Строки документации модуля, класса, функции, метода
print(my_module.Checker.__module__,
      my_module.SiteInfo.__module__)        # Имя модуля
print(my_module.Checker.__bases__,
      my_module.Storage.__bases__,
      my_module.SiteInfo.__bases__)         # Кортеж с базовыми классами
print(dataset.__class__)                    # Объект-класс, экземпляром которого является этот инстанс
print(hash('строка'),
      hash('строка') == hash('не строка'))  # Возвращает хеш-значение объекта, равное 32-битному числу


print()


# Библиотека psutil - https://psutil.readthedocs.io/en/latest/
import psutil

#  Информация о системных вызовах и контекстных переключателях
print(psutil.cpu_stats())
#  Информация о диске
# print(psutil.disk_usage("D:"))
print(psutil.disk_usage("/home/"))
#  Информация о состоянии памяти
print(psutil.virtual_memory())

print('end')
