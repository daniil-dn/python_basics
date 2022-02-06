class CheckerError(Exception):
    _default_detail: str = 'базовая ошибка чекера'

    def __init__(self, detail: str = None):
        if detail:
            self._default_detail = detail

    def __str__(self):
        return self._default_detail


# ошибки запросов к внешним ресурсам
class CheckerRequest(CheckerError):
    _default_detail = 'ошибки запросов'
    _default_code: int = 10000

    def __init__(self, detail: str = None, code: int = None):
        super(CheckerRequest, self).__init__(detail)
        if code:
            self._default_code = code

    def __str__(self):
        return f'code={self._default_code}, {self._default_detail}'


class CheckerBadRequest(CheckerRequest):
    _default_detail = 'ошибки запроса к внешнему ресурсу'
    _default_code = 40000


class CheckerExternalServerError(CheckerRequest):
    _default_detail = 'проблемы с внешним ресурсом'
    _default_code = 50000


# внутренние ошибки эксплуатации нашего чекера
class CheckerExploitationError(CheckerError):
    def __init__(self, detail: str):
        super(CheckerExploitationError, self).__init__(detail)


class CheckerLogicError(CheckerExploitationError):
    """Ошибки в логике работы чекера"""
    pass


class CheckerComponentError(CheckerExploitationError):
    """Ошибки в логике работы компонентов чекера"""
    pass




