import requests
import re
from decimal import Decimal
import time
from datetime import datetime


def currency_rates_adv(code: str) -> tuple | None:
    """возвращает курс валюты `code` по отношению к рублю"""
    time_start = time.perf_counter()
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text
    print("request took: ", time.perf_counter() - time_start)
    date_str = str(re.search(r'Date="(\d+[.].\d+[.].\d+).', response).group(1))
    date_str_list = date_str.split('.')
    date_obj = datetime(year=int(date_str_list[2]), month=int(date_str_list[1]), day=int(date_str_list[0]))
    print(date_str_list)
    code_ind = response.find(code.upper())
    if code_ind == -1:
        return None
    else:
        response = response[code_ind:]
        value_str = re.search(r"<Value>(\d+[,].\d+).</Value>", response)
        date_str = re.search(r'Date="(\d+[.].\d+[.].\d+).', response)

        value_float = Decimal(re.sub(",", '.', value_str.group(1)))
    return (value_float.quantize(Decimal("1.00")), date_obj.date)

    #     value_float = float(re.sub(",", '.', value_str.group(1)))
    # return str("%.2f" % value_float)


print(*currency_rates_adv("AuD"))
print(currency_rates_adv("eur"))
print(*currency_rates_adv("uSd"))
