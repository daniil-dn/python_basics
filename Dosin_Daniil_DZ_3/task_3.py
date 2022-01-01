# +Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся
# с соответствующей буквы.
# Например:
#
# $ thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"],
# "П": ["Петр"]
# }
#
# Подумайте:
# * полезен ли будет вам оператор распаковки? +
# * Как поступить, если потребуется сортировка по ключам?
# * Можно ли использовать словарь в этом случае?

from collections import OrderedDict


def thesaurus(*args):
    names_dict = {}
    for name in args:
        name = name.capitalize()
        if names_dict.get(name[0]):
            names_dict[name[0]].append(name)
        else:
            names_dict.setdefault(name[0], [name])
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

names_gen = tuple(
    "Иван дмитрий сергей дарья алина алексей Random Names Sanjeev Oakley Alessandro lyons Millie Callaghan Names Sanjeev Oakley Alessandro".split())
ready_name_dict = thesaurus(*names_gen)
ready_name_dict_value_sorting = thesaurus(*names_gen)
print(ready_name_dict)

# sorting with ordereddict
ready_name_dict = dict(OrderedDict(sorted(ready_name_dict.items())))
# sorting by keys with usual dict
ready_name_dict_value_sorting = dict(ready_name_dict.items(), key=lambda item: item[0])
ready_name_dict_value_sorting.popitem()  # remove lambda hash from dict

print(ready_name_dict)
print(ready_name_dict_value_sorting)
