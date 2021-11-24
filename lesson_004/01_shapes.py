# -*- coding: utf-8 -*-

import simple_draw as sd
# sd.resolution = (1200, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(x=0, y=0, angle=0, length=0):
#     point = sd.get_point(x, y)
#     for i in range(3):
#
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         point = v1.end_point
#         angle += 120
#         v1.draw()
#
# triangle(100, 100, 0, 100)
#
# def square(x=0, y=0, angle=0, length=0):
#     point = sd.get_point(x, y)
#     for i in range(4):
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         point = v1.end_point
#         angle += 90
#         v1.draw()
# square(400, 100, 0, 100)
#
# def pentagon(x=0, y=0, angle=0, length=0):
#     point = sd.get_point(x, y)
#     for i in range(5):
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         point = v1.end_point
#         angle += 72
#         v1.draw()
# pentagon(100, 400, 0, 100)
#
# def hexagon(x=0, y=0, angle=0, length=0):
#     point = sd.get_point(x, y)
#     for i in range(6):
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         point = v1.end_point
#         angle += 60
#         v1.draw()
# hexagon(400, 400, 0, 100)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def figure(x, y, side, angle, length):
    point = sd.get_point(x, y)
    for i in range(side - 1):

        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        point = v1.end_point
        angle += 360/side
        v1.draw()
    sd.line(point, sd.get_point(x, y), width=3)

triangle = figure(100, 100, 3, 0,length=100)
square = figure(400, 100, 4, 0,length=100)
pentagon = figure(100, 400, 5, 0,length=100)
hexagon = figure(400, 400, 6, 0,length=100)
sd.pause()
