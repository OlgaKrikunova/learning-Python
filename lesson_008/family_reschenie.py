from random import randint
from tkinter.font import names


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt_in_house = 0
        self.coats = 0
        self.geld = 0
        self.foods = 0

    def __str__(self):
        return ('В доме еды осталось {}, денег осталось {}, грязи {}, '
                'еды кошака осталось {}').format(self.food, self.money,
                                                 self.dirt_in_house, self.cat_food)


home = House()


class Family:
    food = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = home

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food -= 20
            self.house.dirt_in_house += 5
            self.house.foods += 20

        else:
            print('{} нет еды'.format(self.name))

    def __str__(self):
        return 'Я - {}, сытость - {}, счастье - {}'.format(
            self.name, self.fullness, self.happiness)


class Husband(Family):

    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession

    def __str__(self):
        return super().__str__()

    def work(self):
        print('{} сходил на работу.'.format(self.name))
        self.house.money += 150
        self.fullness -= 10
        self.happiness -= 20
        self.house.geld += 150

    def gaming(self):
        print('{} весь день играл в компьютерные игры.'.format(self.name))
        self.fullness -= 10
        self.happiness += 20
        self.house.dirt_in_house += 5

    def pet_cat(self):
        print('{} погладил кота'.format(self.name))
        self.happiness += 5

    def act(self):
        if self.fullness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.happiness < 10:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 400:
            self.work()
        elif self.happiness >= 10:
            self.pet_cat()
        elif dice == 6:
            self.gaming()


class Wife(Family):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def shopping(self):
        if self.house.money > 70:
            print('{} сходила в магазин за продуктами.'.format(self.name))
            self.house.food += 60
            self.house.money -= 60
            self.fullness -= 10
            self.happiness -= 5

        if self.house.money > 70:
            print('{} сходила в магазин за едой кошаку.'.format(self.name))
            self.house.cat_food += 20
            self.house.money -= 20

    def buy_fur_coat(self):
        if self.house.money > 350:
            print('{} сходила в магазин за шубой.'.format(self.name))
            self.happiness += 60
            self.house.money -= 350
            self.fullness -= 10
            self.house.coats += 1

    def clean_house(self):
        if self.house.dirt_in_house > 100:
            print('{} убрался в доме'.format(self.name))
            self.house.dirt_in_house -= 80
            self.fullness -= 10
            self.happiness -= 10

    def pet_cat(self):
        print('{} погладил кота'.format(self.name))
        self.happiness += 5

    def act(self):
        if self.fullness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.happiness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.fullness < 20:
            self.eat()
        elif self.happiness < 50:
            self.buy_fur_coat()
        elif self.house.dirt_in_house > 100:
            self.clean_house()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.shopping()
        dice = randint(1, 8)
        if dice == 1:
            self.pet_cat()


class Cat(Family):

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.cat_food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10

    def slip(self):
        if self.fullness > 10:
            print('{} спал'.format(self.name))
            self.fullness -= 10

    def wallpaper(self):
        if self.fullness > 10:
            print('{} дерет обои'.format(self.name))
            self.fullness -= 10
            self.house.dirt_in_house += 5

    def act(self):
        if self.fullness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.fullness <= 10:
            self.eat()
        elif self.fullness > 30:
            self.slip()
        else:
            self.wallpaper()


serge = Husband(name='Сережа', profession="айтишник")
masha = Wife(name='Маша')
cit = Cat(name='Котэ')

for day in range(1, 366):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    cit.act()
    print(serge)
    print(masha)
    print(cit)
    print(home)
print()
print('Всего заработано денег {}, всего съедено еды {},'
      ' всего куплено шуб {}.'.format(home.geld, home.foods, home.coats))
