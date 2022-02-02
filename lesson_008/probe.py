# -*- coding: utf-8 -*-

from termcolor import cprint

from random import randint


class House:

    def __init__(self):
        self.food = 30
        self.money = 100
        self.dust = 0
        self.cats_food = 30

    def __str__(self):
        return 'В доме еды осталось {}, кошачий корм {}, денег осталось {}, загрязненность дома {}'.format(
            self.food, self.cats_food, self.money, self.dust)


class Human:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = None
        self.happiness = None
        self.all_food = 0

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happiness)

    def get_a_cat(self):
        cprint('{} притащил кота'.format(self.name), color='cyan')
        self.fullness -= 10

    def petting_the_cat(self):
        cprint('{} гладил(а) кота'.format(self.name), color='cyan')
        self.fullness -= 10
        self.happiness += 5

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Живет в доме '.format(self.name, self.house), color='cyan')

    def eat(self):
        if self.house.food >= 30:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            self.all_food += 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')


class Husband(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.fullness = 50
        self.happiness = 100
        self.all_money = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        elif self.happiness <= 0:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.dust > 90:
            self.happiness -= 10
        elif self.happiness <= 10:
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        else:
            self.petting_the_cat()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        self.all_money += 150

    def gaming(self):
        cprint('{} Играл в World of Tanks целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.fullness = 30
        self.happiness = 100
        self.all_coat = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла от голода...'.format(self.name), color='red')
            return
        elif self.happiness <= 0:
            cprint('{} умерла от депрессии...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 60:
            self.shopping()
        elif self.house.cats_food <= 10:
            self.shopping_by_cat()
        elif self.house.dust >= 100:
            self.clean_house()
        elif self.house.dust > 90:
            self.happiness -= 10
        elif self.happiness <= 10:
            self.bye_for_coat()
        elif dice == 1:
            self.petting_the_cat()
        elif dice == 2:
            self.eat()
        else:
            self.vatch_TV()

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_by_cat(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cats_food += 50

    def bye_for_coat(self):
        cprint('{} Купила шубу'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 60
        self.all_coat += 1

    def clean_house(self):
        cprint('{} убрала квартиру'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.dust -= 100

    def vatch_TV(self):
        cprint('{} Смотрела ТВ целый день'.format(self.name), color='green')
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def act(self):
        if self.fullness <= 0:
            cprint('{} сдох...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10

    def eat(self):
        cprint('{} ест'.format(self.name), color='magenta')
        self.fullness += 10
        self.house.cats_food -= 5

    def sleep(self):
        cprint('{} дрыхнет'.format(self.name), color='magenta')
        self.fullness -= 10

    def soil(self):
        cprint('{} дерет обои'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.dust += 5


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kisa = Cat(name='Тимошка')
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
serge.get_a_cat()
kisa.go_to_the_house(house=home)

for day in range(1, 366):
    home.dust += 5
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kisa.act()
    print('--- в конце дня ---')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kisa, color='cyan')
    cprint(home, color='cyan')
cprint('===== еды съедено {}, заработано денег {}, куплено шуб {} ====='.format(serge.all_food + masha.all_food
                                                                                , serge.all_money, masha.all_coat),
       color='red')
