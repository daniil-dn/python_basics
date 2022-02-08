import datetime
import types
from typing import Dict, Tuple


class Date:
    def __int__(self, str):
        self.date_str = str

    @classmethod
    def date_to_int(cls, date_str: str, valid_cb=None) -> Dict[str, int] | Tuple[None, str]:
        """
        Извлекает дату из строки вида "dd-mm-yy" и привод его в словарь вида {day: "dd", month: "mm", year: "yy"}

        """

        if valid_cb is not None and type(valid_cb) is types.FunctionType:
            validation = valid_cb(date_str)
            print(f"date validation is {validation}")
            if validation is False:
                return (None, "Not valid")

        template_date = ('day', 'month', 'year')
        ls_date = date_str.split('-')
        try:
            ls_date = list(map(int, ls_date))
        except ValueError as err:
            return (None, str(err))

        return {template_date[i]: ls_date[i] for i in range(3)}

    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        """
        Проверяет дату на валидность по таким параметрам как:
        День положительное число, меньше 31
        Месяц положительное число, меньше 12
        Год положительное число, меньше текущего года или равен ему

        :date_str строка с датой
        :return bool Если дата проходит валидацию, возвращает True
        """
        valid = False
        date_ints = Date.date_to_int(date_str)
        if type(date_ints) is tuple and date_ints[0] is None:
            return valid

        for name, num in date_ints.items():
            if name == "day":
                valid = True if 0 < num < 31 else False
            elif name == "month":
                valid = True if 0 < num < 12 else False
            elif name == 'year':
                valid = True if 0 < num <= datetime.date.today().year else False
        return valid


print(Date.date_to_int('11-12-2002-32', Date.is_valid_date))
print()
print(Date.date_to_int('11-12-2002-3'))

print()
print(Date.is_valid_date('11-12-2002'))

print(Date.date_to_int('11-12-dddd'))
