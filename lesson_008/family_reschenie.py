from random import randint
from tkinter.font import names


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt_in_house = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязи {}'.format(
            self.food, self.money, self.dirt_in_house)


home = House()


class People:
    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = home

    def eat(self):
        if self.house.food >= 20:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food -= 20
            self.house.dirt_in_house += 5

        else:
            print('{} нет еды'.format(self.name))

    def __str__(self):
        return 'Я - {}, сытость - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)


class Husband(People):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession

    def __str__(self):
        return super().__str__()

    def work(self):
        print('{} сходил на работу.'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        print('{} весь день играл в компьютерные игры.'.format(self.name))
        self.fullness -= 10
        self.happiness += 20
        self.house.dirt_in_house += 5

    def act(self):
        if self.fullness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.happiness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 200:
            self.work()
        else:
            self.gaming()


class Wife(People):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def shopping(self):
        if self.house.money > 70:
            print('{} сходила в магазин за продуктами.'.format(self.name))
            self.house.food += 50
            self.house.money -= 50
            self.fullness -= 10
        else:
            print('{} деньги кончились!'.format(self.name))

    def buy_fur_coat(self):
        if self.happiness < 40 and self.house.money > 400:
            print('{} сходила в магазин за шубой.'.format(self.name))
            self.happiness += 60
            self.house.money -= 350
            self.fullness -= 10

    def clean_house(self):
        if self.house.dirt_in_house > 80:
            print('{} убрался в доме'.format(self.name))
            self.house.dirt_in_house -= 80
            self.fullness -= 10

    def act(self):
        if self.fullness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.happiness < 10:
            print('{} умер...'.format(self.name))
            return
        if self.fullness < 20:
            self.eat()
        elif self.happiness < 20:
            self.buy_fur_coat()
        elif self.house.dirt_in_house > 80:
            self.clean_house()
        elif self.house.food < 30:
            self.shopping()


serge = Husband(name='Сережа', profession="айтишник")
masha = Wife(name='Маша')

for day in range(1, 366):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    print(serge)
    print(masha)
    print(home)
