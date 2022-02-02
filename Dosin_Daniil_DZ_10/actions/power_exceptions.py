class PowerMessage(Exception):
    _default_message: str = 'инфа по энергии'

    def __init__(self, message: str = None):
        if message:
            self._default_message = message

    def __str__(self):
        return self._default_message


class IsNotEnergyObject(PowerMessage):
    _default_message = 'нельзя разряжать незаряженное!'


class PowerComplete(PowerMessage):
    _default_message = 'зарядка завершена'


class PowerEmpty(PowerMessage):
    _default_message = 'заряд закончился'


class PowerRestoreError(PowerMessage):
    _default_message = 'нельзя зарядить'
