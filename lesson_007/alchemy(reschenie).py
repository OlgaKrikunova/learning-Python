class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(self, Water) and isinstance(other, Air):
            return Storm()
        elif isinstance(self, Water) and isinstance(other, Earth):
            return Dirt()


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(self, Air) and isinstance(other, Fire):
            return Lightning()
        elif isinstance(self, Air) and isinstance(other, Earth):
            return Dirt()


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(self, Earth) and isinstance(other, Fire):
            return Lava()


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(self, Fire) and isinstance(other, Water):
            return Steam()


class Storm:
    def __str__(self):
        return 'Шторм'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'

class Steam:
    def __str__(self):
        return 'Пар'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Earth(), '+', Fire(), '=', Earth() + Fire())
print(Fire(), '+', Water(), '=', Fire() + Water())

# Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
