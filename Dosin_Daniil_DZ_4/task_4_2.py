import requests
import re
from decimal import Decimal


def currency_rates(code: str) -> Decimal|None:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text
    code_ind = response.find(code.upper())
    if code_ind == -1:
        return None
    else:
        response = response[code_ind:]
        value_str = re.search(r"<Value>(\d+[,].\d+).</Value>", response)

        value_float = Decimal(re.sub(",", '.', value_str.group(1)))
    return value_float.quantize(Decimal("1.00"))

    #     value_float = float(re.sub(",", '.', value_str.group(1)))
    # return str("%.2f" % value_float)


print(currency_rates("AuD"))
print(currency_rates("euro"))
print(currency_rates("uSd"))
