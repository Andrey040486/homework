# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)

snow_x = (100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050)
y = 500
snow_lenght = (1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11)

# y = 500
# x = 100
#
# y2 = 450
# x2 = 150
length = 1
while True:
    sd.clear_screen()
    for i in snow_x:
        point = sd.get_point(i, y)
        sd.snowflake(center=point, length=length)
        length = sd.random_number(1, 10)
    y -= 10
    if y < 5:
        break


    # point2 = sd.get_point(x2, y2)
    # sd.snowflake(center=point2, length=30)
    # y2 -= 10
    # if y2 < 5:
    #     break
    # x2 = x2 + 20

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


# while True:
#     sd.clear_screen()
#     for i in range(50, 1000, 50):
#         point = sd.get_point(i, y)
#         sd.snowflake(center=point, length=10)
#     y -= 10
#     if y < 5:
#         break
#     i = i + 10
#
#     # point2 = sd.get_point(x2, y2)
#     # sd.snowflake(center=point2, length=30)
#     # y2 -= 10
#     # if y2 < 5:
#     #     break
#     # x2 = x2 + 20
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()
