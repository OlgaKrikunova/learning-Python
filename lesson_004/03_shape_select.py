# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (800, 600)

user_input = input('Возможные фигуры:\n 0: треугольник,\n 1: квадрат,'
                   '\n 2: пятиугольник,\n 3: шестиугольник\n '
                   'Введите желаемую фигуру:')
shapes_index = int(user_input)
print('Вы ввели', shapes_index)

def draw_vectors(point, angle, angle_change, len_, qty):

    for i in range(qty):
        v1 = sd.get_vector(start_point=point, angle=angle, length=len_, width=5)
        v1.draw()
        angle += angle_change
        point = v1.end_point

# треугольник
point_0 = sd.get_point(300, 200)

def triangle(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=120, len_=200, qty=3)

# квадрат
point_1 = sd.get_point(350, 200)

def square(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=angle + 90, len_=200, qty=4)

#
# # пятиугольник
length_1 = 100
point_2 = sd.get_point(350, 200)

def polygon(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=angle + 72, len_=length_1, qty=5)

#
#
# # шестиугольник
length_2 = 100
point_3 = sd.get_point(350, 200)

def polygon_1(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=angle + 60, len_=length_2, qty=6)

#

if shapes_index == 0:
    triangle(point=point_0, angle=0)
elif shapes_index == 1:
    square(point=point_1, angle=0)
elif shapes_index == 2:
    polygon(point_2, angle=0)
elif shapes_index == 3:
    polygon_1(point_3, angle=0)

sd.pause()
