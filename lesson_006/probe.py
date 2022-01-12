from random import randint

_holder = {}

def make_a_number():
    global _holder
    _holder = {}
    for i in range(4):
        _holder[i] = randint(0, 9)
        if _holder[0] == 0
            continue
    print(_holder)


make_a_number()