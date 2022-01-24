# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        return Storm(part1=self, part2=other)

    def __add__(self, other):
        return Steam(part1=self, part2=other)

    def __add__(self, other):
        return Mud(part1=self, part2=other)


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        return Storm(part1=self, part2=other)

    def __add__(self, other):
        return Thunder(part1=self, part2=other)

    def __add__(self, other):
        return Dust(part1=self, part2=other)


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        return Steam(part1=self, part2=other)

    def __add__(self, other):
        return Thunder(part1=self, part2=other)

    def __add__(self, other):
        return Lava(part1=self, part2=other)


class Land:

    def __str__(self):
        return 'Зеля'

    def __add__(self, other):
        return Dust(part1=self, part2=other)

    def __add__(self, other):
        return Mud(part1=self, part2=other)

    def __add__(self, other):
        return Lava(part1=self, part2=other)


class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм. Возник из ' + str(self.part1) + ' и ' + str(self.part2)


class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар. Возник из ' + str(self.part1) + ' и ' + str(self.part2)


class Mud:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь. Возник из ' + str(self.part1) + ' и ' + str(self.part2)


class Thunder:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Гром. Возник из ' + str(self.part1) + ' и ' + str(self.part2)


class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль. Возник из ' + str(self.part1) + ' и ' + str(self.part2)


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава. Возник из ' + str(self.part1) + ' и ' + str(self.part2)


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Land(), '=', Water() + Land())
print(Air(), '+', Fire(), '=', Water() + Fire())
print(Air(), '+', Land(), '=', Water() + Land())
print(Land(), '+', Fire(), '=', Land() + Fire())