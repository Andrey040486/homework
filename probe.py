# -*- coding: utf-8 -*-
import simple_draw as sd

# def figure(x, y, side, angle, length, color):
#     point = sd.get_point(x, y)
#     for i in range(side - 1):
#
#         v1 = sd.vector(start=point, angle=angle, length=length, color=color, width=3)
#         point = v1.end_point
#         angle += 360/side
#         v1.draw()
#     sd.line(point, sd.get_point(x, y), width=3)
#
# triangle = figure(100, 100, 3, 0, length=100, color=sd.COLOR_RED)
# square = figure(400, 100, 4, 0, length=100, color=sd.COLOR_RED)
# pentagon = figure(100, 400, 5, 0, length=100, color=sd.COLOR_RED)
# hexagon = figure(400, 400, 6, 0, length=100, color=sd.COLOR_RED)

def figure(x, y, side, angle, length, color):
    point = sd.get_point(x, y)
    for i in range(side - 1):

        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        point = v1.end_point
        angle += 360/side
        v1.draw(color=color)
    sd.line(point, sd.get_point(x, y), color=color, width=3)

triangle = figure(100, 100, 3, 0,length=100, color=sd.COLOR_RED)
square = figure(400, 100, 4, 0,length=100, color=sd.COLOR_RED)
pentagon = figure(100, 400, 5, 0,length=100, color=sd.COLOR_RED)
hexagon = figure(400, 400, 6, 0,length=100, color=sd.COLOR_RED)



sd.pause()