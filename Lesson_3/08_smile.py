# -*- coding: utf-8 -*-
from random import randint

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


sd.resolution = (1200, 600)

def r_eya(x, y):
    radius = 10
    x += 35
    y += 20
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, width=5)

def l_eya(x, y):
    radius = 10
    x -= 35
    y += 20
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, width=5)

def bubble(x, y):
    radius = 70
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, width=5)
    r_eya(x,y)
    l_eya(x,y)

    a = x - 10
    b = y - 15
    a_1 = x + 15
    b_1 = y - 15
    point = sd.get_point(a, b)
    point_1 = sd.get_point(a_1, b_1)
    sd.line(start_point=point, end_point=point_1, width=50)


for _ in range(5):
    x = randint(100, 1000)
    y = randint(100, 500)
    bubble(x,y)





# TODO здесь ваш код

sd.pause()
