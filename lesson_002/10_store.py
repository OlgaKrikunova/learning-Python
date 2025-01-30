#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

stol_code = goods['Стол']
stol_item = store[stol_code][0]
stol_quantity = stol_item['quantity']
stol_price = stol_item['price']
stol_cost = stol_quantity * stol_price
print('Стол -', stol_quantity,'шт, стоимость', stol_cost, 'руб')

stol_code_1 = goods ['Стол']
stol_item_1 = store[stol_code_1][1]
stol_quantity_1 = stol_item_1['quantity']
stol_price_1 = stol_item_1 ['price']
stol_cost_1 = stol_quantity_1 * stol_price_1
print('Стол -', stol_quantity_1, 'шт, стоимость', stol_cost_1,'руб')

stol = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
print(stol)

stol_1 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print(stol_1)


divan_code = goods['Диван']
divan_item = store[divan_code][0]
divan_quantity = divan_item['quantity']
divan_price = divan_item['price']
divan_cost = divan_quantity * divan_price
print('Диван -', divan_quantity, 'шт,', 'стоимость', divan_cost, 'руб')

divan_code_1 = goods['Диван']
divan_item_1 = store[divan_code_1][1]
divan_quantity_1 = divan_item_1['quantity']
divan_price_1 = divan_item_1['price']
divan_cost_1 = divan_quantity_1 * divan_price_1
print('Диван -', divan_quantity_1, 'шт,', 'стоимость', divan_cost_1, 'руб')

divan = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
print(divan)


stul_code = goods['Стул']
stul_item = store[stul_code][0]
stul_quantity = stul_item['quantity']
stul_price = stul_item['price']
stul_cost = stul_quantity * stul_price
print('Стул -', stul_quantity, 'шт,', 'стоимость', stul_cost, 'руб')

stul_code_1 = goods['Стул']
stul_item_1 = store[stul_code_1][1]
stul_quantity_1 = stul_item_1['quantity']
stul_price_1 = stul_item_1['price']
stul_cost_1 = stul_quantity_1 * stul_price_1
print('Стул -', stul_quantity_1, 'шт,', 'стоимость', stul_cost_1, 'руб')


stul_code_2 = goods['Стул']
stul_item_2 = store[stul_code_2][2]
stul_quantity_2 = stul_item_2['quantity']
stul_price_2 = stul_item_2['price']
stul_cost_2 = stul_quantity_2 * stul_price_2
print('Стул -', stul_quantity_2, 'шт,', 'стоимость', stul_cost_2, 'руб')



# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






