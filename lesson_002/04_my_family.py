#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mutter', 'vater', 'bruder']


# список списков приблизительного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['mutter', 170],
    ['vater', 175],
    ['bruder', 180],
]
print(my_family_height[1][1])

print(f'рост отца {my_family_height[1][1]}')

rost = (my_family_height[0][1] + my_family_height[1][1] + my_family_height [2][1])

print(rost)

print(f'общий рост семьи {rost}')

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
