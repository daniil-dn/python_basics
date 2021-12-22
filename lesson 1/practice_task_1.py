#+ Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# +  до минуты: <s> сек;
# +  до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

input_seconds = int(input('enter how much seconds i have to convert: '))

minutes = int(input_seconds / 60)
hours = int(minutes / 60)
days = int(hours / 24)
hours_out_days = hours - days * 24
minutes_out_hours = minutes - hours * 60
seconds_out_minutes = input_seconds - minutes * 60

if minutes == 0 and hours == 0:
    print(f"{input_seconds} sec")
elif minutes > 0 and hours == 0:
    print(f'{minutes} minutes {seconds_out_minutes} seconds')
elif hours > 0 and days == 0:
    print(f'{hours} hours {minutes_out_hours} minutes {seconds_out_minutes} seconds')
elif days > 0:
    print(f'{days} days {hours_out_days} hours {minutes_out_hours} minutes {seconds_out_minutes} seconds')
