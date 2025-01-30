# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import lines


sd.resolution = (800, 600)

_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


user_input = input("Введите, пожалуйста, номер цвета:")
color_index = int(user_input)
print('Вы ввели', color_index)
color = _colors[color_index]

def draw_vectors(point, angle, angle_change, len_, qty):

    for i in range(qty):
        v1 = sd.get_vector(start_point=point, angle=angle, length=len_, width=5)
        v1.draw(color=color)
        angle += angle_change
        point = v1.end_point


# треугольник
point_0 = sd.get_point(500, 400)

def triangle(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=120, len_=200, qty=3)
triangle(point=point_0, angle=0)
#
# квадрат
point_0 = sd.get_point(500, 100)

def square(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=angle + 90, len_=200, qty=4)
square(point=point_0, angle=0)
#
# # пятиугольник
length_1 = 100
point_1 = sd.get_point(100, 400)

def polygon(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=angle + 72, len_=length_1, qty=5)
polygon(point_1, angle=0)
#
#
# # шестиугольник
length_2 = 100
point_2 = sd.get_point(100, 100)

def polygon(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=angle + 60, len_=length_2, qty=6)
polygon(point_2, angle=0)
# #
#



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



sd.pause()
