# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.soviet_street.house1 import room1 as soviet_r1h1
from district.soviet_street.house1 import room2 as soviet_r2h1
from district.soviet_street.house2 import room1 as soviet_r1h2
from district.soviet_street.house2 import room2 as soviet_r2h2
from district.central_street.house1 import room1 as central_r1h1
from district.central_street.house1 import room2 as central_r2h1
from district.central_street.house2 import room1 as central_r1h2
from district.central_street.house2 import room2 as central_r2h2

all_folks = soviet_r1h2.folks + soviet_r2h1.folks + soviet_r1h1.folks + soviet_r2h2.folks + central_r2h1.folks + \
            central_r1h1.folks + central_r1h2.folks + central_r2h2.folks

print('На районе живут :', ', '.join(all_folks))
