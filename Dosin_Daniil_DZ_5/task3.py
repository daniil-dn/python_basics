# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
#
# ('Станислав', None)

# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
#
from sys import getsizeof


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', ]


def check_gen(tutors: list, klasses: list):
    for tutor in tutors:
        if tutors.index(tutor) < len(klasses):
            klass = klasses[tutors.index(tutor)]
        else:
            klass = None
        yield (tutor, klass)


generator = check_gen(tutors, klasses)
print(type(generator), getsizeof(generator), sep='  with size ')  # -> <class 'generator'>
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
