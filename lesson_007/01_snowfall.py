# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = 100
        self.y = 500
        self.length = 10

    def clear_previous_picture(self):
        point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        self.y -= 5

    def draw(self):
        point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=point, length=self.length)

    def can_fall(self):
        if self.y < 10:
            return False
        else:
            return True


flake = Snowflake()

while True:
    sd.clear_screen()
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
