import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(^[\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)+[a-zA-Z]{2,7}$)')
    RE_USER = re.compile(r'')

    email_valid = RE_MAIL.match(email)
    if email_valid:

        result = {
            "username": email_valid.group(1),
            'domain': email_valid.group(2)
        }
        return result
    else:
        raise ValueError('Invalid email')


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    # email_parse('someone@geekbrainsru')
