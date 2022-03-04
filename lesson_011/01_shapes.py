# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
def figure(point, side, angle, length):
    start_point = point
    for i in range(side - 1):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        point = v1.end_point
        angle += 360 / side
        v1.draw()
    sd.line(point, start_point, width=3)


def get_polygon(n):
    def get_figure(point, angle, length):
        def figure(point=point, side=n, angle=angle, length=length):
            start_point = point
            for i in range(side - 1):
                v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
                point = v1.end_point
                angle += 360 / side
                v1.draw()
            sd.line(point, start_point, width=3)
        return figure()
    return get_figure


draw_triangle = get_polygon(n=7)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
