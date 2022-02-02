from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Упрощенная реализация одного из паттернов проектирования "Компоновщик"

class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    @abstractmethod
    def diagnostics(self) -> str:
        pass


class HardDisk(Component):
    def diagnostics(self) -> str:
        return f"Я {self.__class__.__name__}!"


class Monitor(Component):
    def diagnostics(self) -> str:
        return f"Я {self.__class__.__name__}!"


class Mouse(Component):
    def diagnostics(self) -> str:
        return f"Я {self.__class__.__name__}!"


class Computer(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def diagnostics(self) -> str:
        results = []
        for child in self._children:
            results.append(child.diagnostics())
        return f'{self.__class__.__name__} - опрос дочерних устройств: {", ".join(results)}'
