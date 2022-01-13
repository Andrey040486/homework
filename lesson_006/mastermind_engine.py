from random import randint

_holder = {}



def make_a_number():
    global _holder
    _holder = {}
    for i in range(4):
        _holder[i] = randint(0, 9)
        if _holder[0] == 0:
            continue
    print(_holder)


def check_a_number(num):
    bulls = 0
    cows = 0
    dct = {}
    num = str(num)
    for j in range(4):
        if int(num[j]) == _holder[j]:
            bulls += 1
    for h in range(4):
        for g in range(4):
            if int(num[g]) == _holder[h]:
                cows += 1
    if bulls == 4:
        return "Вы выиграли! Идите в ЖОПУ!"

    else:
        dct.setdefault('БЫКИ', bulls)
        dct.setdefault('КОРОВЫ', cows)
        return dct


def game_over():
    return bulls == 4
