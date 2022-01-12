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


make_a_number()
num = 1234
def check_a_number(num):
    bulls = 0
    cows = 0
    dct = {}
    num = str(num)
    for i in range(4):
        dct[i] = num[i]
    for j in range(4):
        if dct[j] == _holder[j]:
            bulls += 1
    for h in range(4):
        if
