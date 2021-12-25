# + Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# +  до минуты: <s> сек;
# +  до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

def count_time_from_sec(input_seconds):
    minutes = int(input_seconds / 60)
    hours = int(minutes / 60)
    days = int(hours / 24)
    hours_out_days = hours - days * 24
    minutes_out_hours = minutes - hours * 60
    seconds_out_minutes = input_seconds - minutes * 60

    if minutes == 0 and hours == 0:
        return (f"{input_seconds} сек")
    elif minutes > 0 and hours == 0:
        return (f'{minutes} мин {seconds_out_minutes} сек')
    elif hours > 0 and days == 0:
        return (f'{hours} час {minutes_out_hours} мин {seconds_out_minutes} сек')
    elif days > 0:
        return (f'{days} дн {hours_out_days} час {minutes_out_hours} мин {seconds_out_minutes} сек')

