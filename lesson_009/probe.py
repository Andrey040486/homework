# -*- coding: utf-8 -*-
import os
import zipfile


class Parser:
    pref_char = 0
    step = 0

    def __init__(self, file_name):
        self.file_name = file_name

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_min(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    if line[0:17] == self.pref_char:
                        self.step += 1
                    elif self.pref_char == 0:
                        self.step += 1
                        self.pref_char = line[0:17]
                    else:
                        file = open('result_min.txt', mode='a')  # mode (режим): запись в конец
                        file_content = f'\n{self.pref_char}] {self.step}'
                        file.write(file_content)
                        self.pref_char = line[0:17]
                        self.step = 1

    def collect_hour(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    if line[0:14] == self.pref_char:
                        self.step += 1
                    elif self.pref_char == 0:
                        self.step += 1
                        self.pref_char = line[0:14]
                    else:
                        file = open('result_hour.txt', mode='a')  # mode (режим): запись в конец
                        file_content = f'{self.pref_char}] {self.step}\n'
                        file.write(file_content)
                        self.pref_char = line[0:14]
                        self.step = 1

    def collect_month(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    if line[0:8] == self.pref_char:
                        self.step += 1
                    elif self.pref_char == 0:
                        self.step += 1
                        self.pref_char = line[0:8]
                    else:
                        self.pref_char = line[0:8]
                        self.step = 1
            file = open('result_month.txt', mode='a')  # mode (режим): запись в конец
            file_content = f'\n{self.pref_char}] {self.step}'
            file.write(file_content)

parser = Parser(file_name='events.txt')
# parser.collect_min()
# parser.collect_hour()
# parser.collect_month()