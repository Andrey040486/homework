# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
point_0 = sd.get_point(600, 5)

# def draw_branches(point, angle, length):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=3)
#     v2 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=3)
#     v1.draw()
#     v2.draw()

# def draw_branches(point, angle, length):
#     v0 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v0.draw()
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=v0.end_point, angle=angle + 30, length=length, width=1)
#     v2 = sd.get_vector(start_point=v0.end_point, angle=angle - 30, length=length, width=1)
#     v1.draw()
#     v2.draw()
#     next1_point = v1.end_point
#     next2_point = v2.end_point
#     next1_angle = angle + 30
#     next2_angle = angle - 30
#     next_length = length * .75
#     draw_branches(point=next1_point, angle=next1_angle, length=next_length)
#     draw_branches(point=next2_point, angle=next2_angle, length=next_length)
#
#
# draw_branches(point_0, 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(point, angle, length):
    v0 = sd.get_vector(start_point=point, angle=angle, length=length)
    v0.draw()
    if length < 1:
        return
    v1 = sd.get_vector(start_point=v0.end_point, angle=angle + sd.random_number(a=18, b=42), length=length, width=1)
    v2 = sd.get_vector(start_point=v0.end_point, angle=angle - sd.random_number(a=18, b=42), length=length, width=1)
    v1.draw()
    v2.draw()
    next1_point = v1.end_point
    next2_point = v2.end_point
    next1_angle = angle + 30
    next2_angle = angle - 30
    next_length = length * sd.random_number(a=6, b=9) / 10
    draw_branches(point=next1_point, angle=next1_angle, length=next_length)
    draw_branches(point=next2_point, angle=next2_angle, length=next_length)


draw_branches(point_0, 90, 100)

sd.pause()


