import zipfile
from pprint import pprint

from random import randint


# txt = 'строка'
# print(f'{txt:*^30}')

# zip_file_name = 'voyna-i-mir.txt.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
# stat = {}
# file_name = 'voyna-i-mir.txt'
# with open(file_name, 'r', encoding='cp1251') as file:
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 if char in stat:
#                     stat[char] += 1
#                 else:
#                     stat[char] = 1
# pprint(stat)


class Sum:
    amount = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line)

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                    self.amount += 1
                else:
                    self.stat[char] = 1
                    self.amount += 1
        # for char in self.stat:
        #     print(self.stat[char])
        #
    def amouent(self):
        print(f'| ИТОГО   | {self.amount}  |')
        print('+---------+----------+')

sum = Sum(file_name='voyna-i-mir.txt.zip')
sum.collect()
print('+---------+----------+')
print('|  буква  | частота  |')
print('+---------+----------+')
for key, value in sum.stat.items():
    print(f'|{key: >5}    | {value: <8} |')
print('+---------+----------+')
# pprint(sum.stat.keys())
sum.amouent()
