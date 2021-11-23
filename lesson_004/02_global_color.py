# -*- coding: utf-8 -*-
import simple_draw as sd


def figure(x, y, side, angle, length, color):
    point = sd.get_point(x, y)
    for i in range(side - 1):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        point = v1.end_point
        angle += 360 / side
        v1.draw(color=color)
    sd.line(point, sd.get_point(x, y), color=color, width=3)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = {'КРАСНЫЙ': sd.COLOR_RED, 'ОРАНЖЕВЫЙ': sd.COLOR_ORANGE, 'ЖЕЛТЫЙ': sd.COLOR_YELLOW, 'ЗЕЛЕНЫЙ': sd.COLOR_GREEN,
          'ГОЛУБОЙ': sd.COLOR_CYAN, 'СИНИЙ': sd.COLOR_BLUE, 'ФИОЛЕТОВЫЙ': sd.COLOR_PURPLE}

print('Возможные цвета:')
for i in enumerate(colors):
    print(i)

num_color = input('Введите желаемый цвет : ')
df = int(num_color)
if df == 0:
    figure(100, 100, 3, 0, length=100, color=colors['КРАСНЫЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['КРАСНЫЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['КРАСНЫЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['КРАСНЫЙ'])
elif df == 1:
    figure(100, 100, 3, 0, length=100, color=colors['ОРАНЖЕВЫЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['ОРАНЖЕВЫЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['ОРАНЖЕВЫЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['ОРАНЖЕВЫЙ'])
elif df == 2:
    figure(100, 100, 3, 0, length=100, color=colors['ЖЕЛТЫЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['ЖЕЛТЫЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['ЖЕЛТЫЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['ЖЕЛТЫЙ'])
elif df == 3:
    figure(100, 100, 3, 0, length=100, color=colors['ЗЕЛЕНЫЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['ЗЕЛЕНЫЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['ЗЕЛЕНЫЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['ЗЕЛЕНЫЙ'])
elif df == 4:
    figure(100, 100, 3, 0, length=100, color=colors['ГОЛУБОЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['ГОЛУБОЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['ГОЛУБОЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['ГОЛУБОЙ'])
elif df == 5:
    figure(100, 100, 3, 0, length=100, color=colors['СИНИЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['СИНИЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['СИНИЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['СИНИЙ'])
elif df == 6:
    figure(100, 100, 3, 0, length=100, color=colors['ФИОЛЕТОВЫЙ'])
    figure(400, 100, 4, 0, length=100, color=colors['ФИОЛЕТОВЫЙ'])
    figure(100, 400, 5, 0, length=100, color=colors['ФИОЛЕТОВЫЙ'])
    figure(400, 400, 6, 0, length=100, color=colors['ФИОЛЕТОВЫЙ'])


else:
    print('Вы ввели некорректный номер!')

# def figure(x, y, side, angle, length, color):
#     point = sd.get_point(x, y)
#     for i in range(side - 1):
#
#         v1 = sd.vector(start=point, angle=angle, length=length,color=color, width=3)
#         point = v1.end_point
#         angle += 360/side
#         v1.draw()
#     sd.line(point, sd.get_point(x, y), width=3)
#
# triangle = figure(100, 100, 3, 0,length=100)
# square = figure(400, 100, 4, 0,length=100)
# pentagon = figure(100, 400, 5, 0,length=100)
# hexagon = figure(400, 400, 6, 0,length=100)


sd.pause()
