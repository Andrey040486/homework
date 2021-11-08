# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
#firstpoint = sd.get_point(50, 50)
#endpoint = sd.get_point(350, 450)
#step = 0
#for j in range(7):

#for i in rainbow_colors:

#    firstpoint = sd.get_point(step + 50, 50)
#    endpoint = sd.get_point(step + 350, 450)
#    step += 10
 #   sd.line(firstpoint, endpoint, i, 5)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
step =0
for i in rainbow_colors:
    point = sd.get_point(1200, 0)
    step += 20
    sd.circle(point, 600 + step, i, 10 )

sd.pause()
