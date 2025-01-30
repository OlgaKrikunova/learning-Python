#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)
# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)

print(zoo)

# уберите слона
#  и выведите список на консоль
del (zoo[3])
print(zoo)

# Ведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
p = zoo.index('lion')  +1
print(p)
k = zoo.index('lark') +1
print(k)




