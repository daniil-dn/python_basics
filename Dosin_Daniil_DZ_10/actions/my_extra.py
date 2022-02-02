from .operators import Bottle


class Warehouse:
    def __init__(self):
        self.our_bottles: set = set()
        self.title = 'empty'

    def __setattr__(self, attr, value):
        if attr == 'title' and isinstance(value, str):
            self.__dict__[attr] = value
            print(f'Вы переписали название склада, теперь это "{self.title}"')
        elif attr == 'our_bottles':
            self.__dict__[attr] = value
        else:
            print(f'Атрибут "{attr}" или значение "{value}" недопустимы')

    def download_bottles(self, *args):
        """Притащить пузыри на склад"""
        count = 0
        for bottle in args:
            if not isinstance(bottle, Bottle):
                print(f'Я не складирую всякий мусор, только бутылки!')
                continue
            self.our_bottles.add(bottle)
            count += 1
        print(f'Фуух, перегрузил пузыри в количестве {count} на склад.')

    def __getitem__(self, volume_value: float):
        return list(filter(lambda bottle: bottle.volume >= volume_value, self.our_bottles))

    def __eq__(self, other):
        return len(self.our_bottles) == len(other.our_bottles)

    def __lt__(self, other):
        return len(self.title) < len(other.title)

    def __iadd__(self, other):
        if not isinstance(other, Bottle):
            raise TypeError('Добавлять можно только бутылки')
        self.our_bottles.add(other)
        print(f'Новый пузырь занесли на склад "{self.title}"')


