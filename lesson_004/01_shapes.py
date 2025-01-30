# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (800, 600)

# треугольник
point_0 = sd.get_point(500, 400)
def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
    v3.draw()
triangle(point=point_0, angle=0)


# квадрат
point_0 = sd.get_point(500, 100)
def square(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=200, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=200, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270.2, length=200, width=3)
    v4.draw()
square(point=point_0, angle=0)

# пятиугольник

length_1 = 100
point_1 = sd.get_point(100, 400)
def polygon(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length_1, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length_1, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length_1, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length_1, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288.2, length=length_1, width=3)
    v5.draw()
polygon(point_1, angle=0)


# шестиугольник
length_2 = 100
point_2 = sd.get_point(100, 100)
def polygon(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length_1, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length_1, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length_1, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length_1, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length_1, width=3)
    v5.draw()
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 301.2, length=length_1, width=3)
    v6.draw()
polygon(point_2, angle=0)




sd.resolution = (800, 600)


def draw_vectors(point, angle, angle_change, len_, qty):
    for i in range(qty):
        v1 = sd.get_vector(start_point=point, angle=angle, length=len_, width=3)
        v1.draw()
        angle += angle_change
        point = v1.end_point


# треугольник
point_0 = sd.get_point(500, 400)

def triangle(point, angle=0):
    draw_vectors(point=point, angle=angle, angle_change=120, len_=200, qty=3)
triangle(point=point_0, angle=0)

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

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
