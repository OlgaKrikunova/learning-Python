# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x = 0
x_1 = 100
y = 0
y_1 = 50
layer = "a"

for _ in range(17):
    for i in range(10):
        simple_draw.rectangle(left_bottom=simple_draw.get_point(x, y),
        right_top=simple_draw.get_point(x_1, y_1), width=1)
        x = x_1
        x_1 += 100

    if layer == 'a':
        x = -50
        x_1 = 50
        layer = 'b'
    else:
        x = 0
        x_1 = 100
        layer = 'a'
    y = y_1
    y_1 += 50




























simple_draw.pause()
