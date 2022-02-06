from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple, Generator


class Manager(ABC):
    is_storage = False

    @property
    def parent(self) -> Manager:
        return self._parent

    @parent.setter
    def parent(self, parent: Manager):
        self._parent = parent

    @abstractmethod
    def get_info(self) -> str:
        pass


class SiteInfo(Manager):
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def get_info(self) -> Tuple[str, str]:
        return self.name, self.url


class Storage(Manager):
    def __init__(self) -> None:
        self._children: List[Manager] = []
        self.is_storage = True

    @property
    def is_empty(self):
        if len(self._children):
            return False
        return True

    def add(self, component: Manager) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Manager) -> None:
        self._children.remove(component)
        component.parent = None

    def get_info(self) -> Generator[Tuple[str, str]]:
        for child in self._children:
            yield child.get_info()

"""
сторедж 1
 - сайт
 - сторедж 2
    - сайт
    - сайт
 - сайт
"""