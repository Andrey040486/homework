# -*- coding: utf-8 -*-
from random import randint, random

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def clear_previous_picture(self):
        point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        self.y -= randint(5, 10)
        self.x += randint(-10, 10)

    def draw(self):
        point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=point, length=self.length)

    def can_fall(self):
        if self.y < 10:
            return False
        else:
            return True


# flake = Snowflake(x=100, y=500, length=10)

# while True:
#     sd.clear_screen()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

def get_flakes(count):
    _flakes = []
    for i in range(0, count-1):
        _flakes.append(Snowflake(x=randint(50, 600), y=500, length=randint(5, 15)))
    return _flakes

def get_fallen_flakes():
    pass


def append_flakes(count):
    pass

N = 20
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
