from __future__ import annotations
import requests
from requests.exceptions import RequestException
from typing import List
from .component.models import Storage, SiteInfo
from .setting import LOG_FILE
from .exceptions import CheckerError, CheckerExternalServerError, CheckerBadRequest, \
    CheckerRequest


class Checker(Storage):
    __storages: List[Storage] = []

    def __init__(self):
        super(Checker, self).__init__()
        self.__errors: List[str] = []
        self.log_file: str = LOG_FILE

    @property
    def is_empty(self):
        return all([child.is_empty for child in self.__storages])

    @property
    def errors(self):
        return self.__errors

    def clear_errors(self):
        self.__errors = []

    @staticmethod
    def __my_get_request(url: str):
        """Статические метод для GET-запроса по переданному url"""
        try:
            response = requests.get(url, timeout=5)
        except RequestException as err:
            raise CheckerExternalServerError(detail=str(err))
        if response.status_code // 100 == 5:
            raise CheckerExternalServerError(code=response.status_code)
        if response.status_code // 100 == 4:
            raise CheckerBadRequest(code=response.status_code)

    def __result_processing(self, source_name: str, url: str):
        error: str = ''
        try:
            Checker.__my_get_request(url)
            return 'OK'
        except CheckerRequest as err:
            error = f'Ресурс "{source_name}" - {err}'
            self.errors.append(error)
        finally:
            if error:
                with open(self.log_file, 'a', encoding='utf-8') as log_file:
                    log_file.write(f'{error}\n')

    def get_info(self):
        """Внешний интерфейс для проверки доступности ресурсов"""
        for storage in self._children:
            storage: Storage
            if storage.is_empty:
                continue
            generator = storage.get_info()
            for name, url in generator:
                result = self.__result_processing(name, url)
                if result:
                    print(f'С ресурсом "{name} - всё ОК')
                else:
                    print(f'"{name}" - проблемы, смотрите в логе')

    @classmethod
    def prepare_app(cls, data: dict) -> Checker:
        """Готовит к работе наш чекер и возвращает его экземпляр"""
        storage = Storage()  # инициализируем объект хранилища сайтов
        checker = cls()  # инициализируем объект чекер

        # перебираем исходные ресурсы
        for key, value in data.items():
            site = SiteInfo(key, value)  # инициализируем объект Сайт
            storage.add(site)  # добавляем сайт в хранилище

        checker.add(storage)  # добавляем хранилище в чекер
        return checker
