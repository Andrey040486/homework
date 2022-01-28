# -*- coding: utf-8 -*-

from termcolor import cprint

from random import randint


class House:
    dust = 0

    def __init__(self):
        self.food = 30
        self.money = 100


class Human:
    pass


class Husband:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        pass

    def gaming(self):
        pass


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')


for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    House.dust += 5
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')