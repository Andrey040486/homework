# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


# class House:
#
#     def __init__(self):
#         pass
#
#
# class Husband:
#
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 30
#         self.house = None
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def work(self):
#         pass
#
#     def gaming(self):
#         pass
#
#
# class Wife:
#
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 30
#         self.house = None
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def shopping(self):
#         pass
#
#     def buy_fur_coat(self):
#         pass
#
#     def clean_house(self):
#         pass
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
#

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# #


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

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

    def have_a_child(self):
        cprint('{} родила ребенка'.format(self.name), color='green')
        self.fullness -= 10

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


class Child(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name
        self.fullness = 30
        self.house = None
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} помер...'.format(self.name), color='red')
            return
        elif self.fullness <= 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        cprint('{} ест'.format(self.name), color='magenta')
        self.fullness += 10
        self.house.food -= 10

    def go_to_the_house(self, house):
        self.house = house

    def sleep(self):
        cprint('{} дрыхнет'.format(self.name), color='magenta')
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
kolyan = Child(name='Колян')
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
kolyan.go_to_the_house(house=home)
serge.get_a_cat()
masha.have_a_child()
kisa.go_to_the_house(house=home)

for day in range(1, 366):
    home.dust += 5
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolyan.act()
    kisa.act()
    print('--- в конце дня ---')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolyan, color='cyan')
    cprint(kisa, color='cyan')
    cprint(home, color='cyan')
cprint('===== еды съедено {}, заработано денег {}, куплено шуб {} ====='.format(serge.all_food + masha.all_food
                                                                                , serge.all_money, masha.all_coat),
       color='red')