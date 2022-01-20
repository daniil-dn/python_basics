# todo
# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается
# с соответствующей буквы.
# Например:
#
# $ thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }
#
# Как поступить, если потребуется сортировка по ключам?
from collections import OrderedDict


def thesaurus_adv(*args: str) -> dict:
    """
    make a dict from list of names and the keys are the first characters of the names
    :param **kwargs: **{names and forenames}
    :return: dict of names and forenames - keys are the first characters of the names
    """
    dict_out = {}
    for name_forename_str in args:
        name_forename_str = name_forename_str.title()
        try:
            forename_char = name_forename_str[name_forename_str.find(' ') + 1]
        except IndexError as er:
            print(er, '\n there is not forename')
            break
        name_char = name_forename_str[0]
        forname_dict = dict_out.get(forename_char)
        list_names = [] if forname_dict is None else forname_dict.get(name_char)

        if forname_dict is None:
            forname_dict = {name_char: [name_forename_str]}
        else:
            if list_names is not None:
                forname_dict.get(name_char).append(name_forename_str)
            else:
                list_names = [name_forename_str]
                forname_dict.setdefault(name_char, list_names)

        dict_out.setdefault(forename_char, forname_dict)
        forname_dict = dict_out.get(forename_char)

    return dict_out


# { "А": {  "П": ["Петр Алексеев"] }}

test_1 = thesaurus_adv("iван sргеев", "Инна Серова", "Петр Алексеев", "Илья j ", "Анна Савельева", )
test_2 = thesaurus_adv("Иван Сергеев", "Инsdfgна Серова", "sdfg sfdgАлексеев", "Илья j ", "Анна Савельева",
                       "Инна Серова",
                       "Петр Алексеев", "sdfg j ", "dfgdg Савельева Инна Серова", "Петр Алексеев", "плья а ",
                       "Анна Савельева")
print(test_1, test_2, sep='\n')
