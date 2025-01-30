from random import randint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def go_to_house(self, house):
        self.house = house
        resident_of_house.append(self)
        self.fullness -= 10
        print('{} Въехал в дом'.format(self.name))

    def pick_up_a_cat(self, cat):
        self.house.cat = cat
        cat.house = self.house
        resident_of_house.append(cat)
        print('{} подобрал кота'.format(self.name))

    def buy_cat_food(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой кошаку'.format(self.name))
            self.house.money -= 50
            self.house.food_bowl += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def house_cleaning(self):
        if self.house.dirt >= 100 and self.fullness >= 30:
            print('{} убрался в доме'.format(self.name))
            self.house.dirt -= 100
            self.fullness -= 20
        else:
            self.eat()
            print('{} нужно поесть!'.format(self.name))

    def watch_MTV(self):
        print('{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_bowl < 10:
            self.buy_cat_food()
        elif self.house.dirt > 100:
            self.house_cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()

        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_bowl = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота {}, грязи {}'.format(
            self.food, self.money, self.food_bowl, self.dirt)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def cat_is_sleeping(self):
        if self.fullness >= 50:
            print('{} спит целый день'.format(self.name))
            self.fullness -= 10
        else:
            print('{} ходит по квартире'.format(self.name))


    def cat_eat(self):
        if self.house.food_bowl >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food_bowl -= 10
        else:
            print('У {} нет еды. Орёт на всю квартиру!'.format(self.name))

    def rips_wallpaper(self):
        if self.fullness >= 20:
            print('{}  дерет обои'.format(self.name))
            self.fullness -= 10
            self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.house.food_bowl < 10:
            self.cat_eat()

        elif dice == 1:
            self.rips_wallpaper()
        elif dice == 2:
            self.cat_eat()


        else:
            self.cat_is_sleeping()



man_1 = Man(name='Мэн')
cat_1 = Cat(name='Котэ')
resident_of_house = []

my_sweet_home = House()

man_1.go_to_house(house=my_sweet_home)
man_1.pick_up_a_cat(Cat(name='Котэ'))

for day in range(1, 366):
    print("===== день {} =====".format(day))
    for resident in resident_of_house:
        resident.act()
    print("----- в конце дня -----")
    for resident in resident_of_house:
        print(resident)
    print(my_sweet_home)
