import zipfile
from pprint import pprint

from random import randint

txt = 'строка'
print(f'{txt:*^30}')

# zip_file_name = 'voyna-i-mir.txt.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
stat = {}
file_name = 'voyna-i-mir.txt'
with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        for char in line:
            if char in stat:
                stat[char] += 1
            else:
                stat[char] = 1
pprint(stat)
