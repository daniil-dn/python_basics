input_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

input_names = [name.split(' ')[-1].lower().capitalize() for name in input_names]

print(*["Привет, {}".format(hello_name) for hello_name in input_names], sep="\n")
