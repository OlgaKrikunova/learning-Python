# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# y = 350
#
# for color in rainbow_colors:
#     sd.line(start_point=sd.get_point(50,y), end_point=sd.get_point(500, y), width=5, color=color)
#     y += 5



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

y = 150
for color_1 in rainbow_colors:
    sd.circle(center_position=sd.get_point(300, y), radius=350, width=5, color=color_1)
    y +=5




sd.pause()
