from random import randint

_holder = {}
dct1 = 0


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
    global dct1
    dct1 = {}
    dct2 = {}
    for i in range(4):
        dct1[i] = int(num[i])
    for j in range(4):
        if dct1[j] == _holder[j]:
            bulls += 1
    for h in range(4):
        for g in range(4):
            if dct1[g] == _holder[h]:
                cows += 1
    if bulls == 4:
        return "Вы выиграли! Идите в ЖОПУ!"

    else:
        dct2.setdefault('БЫКИ', bulls)
        dct2.setdefault('КОРОВЫ', cows)
        return dct2


def game_over():
    return dct1 == _holder
