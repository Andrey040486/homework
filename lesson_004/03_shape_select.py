# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def figure(x, y, side, angle, length):
    point = sd.get_point(x, y)
    for i in range(side - 1):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        point = v1.end_point
        angle += 360 / side
        v1.draw()
    sd.line(point, sd.get_point(x, y), width=3)


figures = ('ТРЕУГОЛЬНИК', 'КВАДРАТ', 'ПЯТИУГОЛЬНИК',
           'ШЕСТИУГОЛЬНИК')

print('Возможные фигуры:')
for j in enumerate(figures):
    print(j)

num_figure = input('Введите желаемую фигуру : ')
df = int(num_figure)
if df == 0:
    figure(200, 200, 3, 0, length=200)
elif df == 1:
    figure(200, 200, 4, 0, length=200)
elif df == 2:
    figure(200, 200, 5, 0, length=200)
elif df == 3:
    figure(200, 200, 6, 0, length=200)
else:
    print('Вы ввели некорректный номер!')

sd.pause()
