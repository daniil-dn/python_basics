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


print(thesaurus('name', 'ivan', "иван", 'inna'))
names_gen = tuple(
    "Random Names Sanjeev Oakley Alessandro Lyons Millie Callaghan Names Sanjeev Oakley Alessandro Lyons Millie CallaghanNames Sanjeev Oakley Alessandro Lyons Millie CallaghanNames Sanjeev Oakley Alessandro Lyons Millie CallaghanNames Sanjeev Oakley Alessandro Lyons Millie Callaghan Jake Curry Maaria Kirkland Jake Curry Maaria Kirkland Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy CantrellJake Curry Maaria Kirkland Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy CantrellJake Curry Maaria Kirkland Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy CantrellJake Curry Maaria Kirkland Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy CantrellJake Curry Maaria Kirkland Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy CantrellJake Curry Maaria Kirkland Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy Cantrell Eliott Robins Jennie Neville Tiya Hood Andreas Goulding Buddy Cantrell".split())
ready_name_dict = thesaurus(*names_gen)
print(ready_name_dict)

# sorting with ordereddict
ready_name_dict = OrderedDict(sorted(ready_name_dict.items()))
print(dict(ready_name_dict))
