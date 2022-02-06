# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
#
# $ get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """
    Возвращает список шуток в количестве count

    :param count: count of jokes
    :return: list of jokes
    """

    list_out = []
    while count > 0:
        str_out = random.choice(nouns)
        str_out += " " + random.choice(adverbs)
        str_out += " " + random.choice(adjectives)
        list_out.append(str_out)
        count -= 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, is_unique: bool = False) -> list:
    """
    make jokes from different words in the dictionaries
    :param count: count of jokes
    :param is_unique: stop repeating words in jokes
    :return: list of jokes
    """
    in_nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    in_adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    in_adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_out = []
    if is_unique:
        while count > 0:
            if len(in_nouns) != 0 and len(in_adverbs) != 0 and len(in_adjectives) != 0:
                # from nouns
                ind_to_delete = random.randint(0, len(in_nouns) - 1)
                str_out = in_nouns.pop(ind_to_delete)
                # from adverbs
                ind_to_delete = random.randint(0, len(in_adverbs) - 1)
                str_out += " " + in_adverbs.pop(ind_to_delete)
                # from adjectives
                ind_to_delete = random.randint(0, len(in_adjectives) - 1)
                str_out += " " + in_adjectives.pop(ind_to_delete)

                list_out.append(str_out)
                count -= 1
            else:
                break
    else:
        list_out = get_jokes(count)
    return list_out


print(get_jokes_adv(1, True))
print(get_jokes_adv(10, True))
