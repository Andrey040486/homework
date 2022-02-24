# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777
CARMA_LEVEL = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    global CARMA_LEVEL
    dice = randint(1, 14)
    if dice == 1:
        CARMA_LEVEL -= 1
        raise IamGodError('I am a GOD!!!')
    elif dice == 2:
        CARMA_LEVEL -= 1
        raise DrunkError('I am DRUNK!!!')
    elif dice == 3:
        CARMA_LEVEL -= 1
        raise CarCrashError('I am CRASH!!!')
    elif dice == 4:
        CARMA_LEVEL -= 1
        raise GluttonyError('I am GLUTTONY!!!')
    elif dice == 5:
        CARMA_LEVEL -= 1
        raise DepressionError('I am DEPRESSED!!!')
    elif dice == 6:
        CARMA_LEVEL -= 1
        raise SuicideError('I am SUICIDE!!!')
    else:
        CARMA_LEVEL += randint(1, 7)
        print('День прошел без происшествий')


day = 0
while True:
    try:
        one_day()
    except IamGodError:
        print('Включился режим БОГА!!!')
    except DrunkError:
        print('Напился!!!')
    except CarCrashError:
        print('Разбился!!!')
    except GluttonyError:
        print('Нажрался!!!')
    except DepressionError:
        print('Депрессия!!!')
    except SuicideError:
        print('Самоликвидировался!!!')
    day += 1
    if CARMA_LEVEL == ENLIGHTENMENT_CARMA_LEVEL:
        print(f'Достигнуто просветление за {day} дней')
        break
# https://goo.gl/JnsDqu
