input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+5', '"', 'градусов']

# todo обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов
index_of_int_list = [n for n in range(len(input_list)) if input_list[n].strip('=+-;:"\'').isdigit()]
for ind in reversed(index_of_int_list):
    input_list.insert(ind, '"')
    input_list.insert(ind + 2, '"')
for i in range(len(input_list)):
    element = input_list[i]
    if element.strip('=+-;:"\'').isdigit():
        if not element[0].isdigit() and int(element.strip('=+-;:"\'')) < 10:
            input_list[i] = '{}0{}'.format(element[0], int(element.strip('=+-;:"\'')))
        elif int(element.strip('=+-;:"\'')) < 10:
            input_list[i] = '0{}'.format(int(element.strip('=+-;:"\'')))
print(input_list)