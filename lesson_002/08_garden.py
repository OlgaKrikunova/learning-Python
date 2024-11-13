#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

garden_set = set(garden)

print(garden_set)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

meadow_set = set(meadow)
print(meadow_set)

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =


# выведите на консоль все виды цветов
blume = (garden_set | meadow_set)
print(blume)

# выведите на консоль те, которые растут и там и там
blume_1 = (garden_set & meadow_set)
print(blume_1)

# выведите на консоль те, которые растут в саду, но не растут на лугу
blume_2 = (garden_set - meadow_set)
print(blume_2)

# выведите на консоль те, которые растут на лугу, но не растут в саду
blume_3 = (meadow_set - garden_set)
print(blume_3)


