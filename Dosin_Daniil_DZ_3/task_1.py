# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
#
# $ num_translate("one")
# "один"
# $ num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
# в теле функции или снаружи.


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский и с русского на английский
     :param value: number to translate
     :return string of translated word or None if number is more that 10
     """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    nums_dictionary_ru_en = {'один': "one", "два": "two", "три": "three", "четыре": "four", "пять": "five",
                             "шесть": "six",
                             "семь": "seven", "восемь": "eight", "девять": "nine", "десять": "ten"}
    nums_dictionary_en_ru = {e: r for r, e in nums_dictionary_ru_en.items()}
    if value in nums_dictionary_ru_en.keys():
        str_out = nums_dictionary_ru_en.get(value)
    elif value in nums_dictionary_en_ru.keys():
        str_out = nums_dictionary_en_ru.get(value)
    else:
        return None

    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("восемь"))
