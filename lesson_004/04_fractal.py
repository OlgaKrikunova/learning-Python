# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 600)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции


_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

point_0 = sd.get_point(400, 5)
angle_0 = 90
len_0 = 100
schag_0 = 0
user_input = input("Введите, пожалуйста, номер цвета:")
color_index = int(user_input)
print('Вы ввели', color_index)
color = _colors[color_index]


def draw_branches(point, angle, length):
    global schag_0
    schag_0 += 1
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
    v1.draw(color=color)

    draw_branches(point=v1.end_point, angle=angle - 38, length=length * .78)

    v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
    v2.draw(color=color)
    draw_branches(point=v2.end_point, angle=angle + 38, length=length * .78)

draw_branches(point=point_0, angle=angle_0, length=len_0)
print(schag_0)


# с рандомными показателями

_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

point_0 = sd.get_point(400, 5)
angle_0 = 90
len_0 = 100
schag_0 = 0
user_input = input("Введите, пожалуйста, номер цвета:")
color_index = int(user_input)
print('Вы ввели', color_index)
color = _colors[color_index]

def draw_branches(point, angle, length):
    global schag_0
    schag_0 += 1

    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
    v1.draw(color=color)

    draw_branches(point=v1.end_point, angle= angle - sd.random_number(a=12,b=42),
                  length=length - sd.random_number(a=8,b=10))

    v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
    v2.draw(color=color)
    draw_branches(point=v2.end_point, angle=angle + sd.random_number(a=12,b=42),
                  length=length - sd.random_number(a=8,b=10))

draw_branches(point=point_0, angle=angle_0, length=len_0)
print(schag_0)


sd.pause()









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

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


