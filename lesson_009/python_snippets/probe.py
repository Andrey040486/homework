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
                else:
                    self.stat[char] = 1


sum = Sum(file_name='voyna-i-mir.txt.zip')
sum.collect()
pprint(sum.stat)
