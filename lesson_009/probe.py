# -*- coding: utf-8 -*-
import os
import zipfile


class Parser:
    pref_char = 0
    step = 1
    z = 0

    def __init__(self, file_name):
        self.file_name = file_name
        # self.stat = {}

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
                self.z += 1
                if 'NOK' in line:
                    if line[16] == self.pref_char:
                        self.step += 1
                        # file = open('result.txt', mode='a')  # mode (режим): запись в конец
                        # file_content = line
                        # file.write(file_content)
                    else:
                        self.pref_char = line[16]
                        if self.z > 2:
                            print(f'{line[0:17]}] {self.step}')
                        self.step = 1

    def collect_hour(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.z += 1
                if 'NOK' in line:
                    if line[12:14] == self.pref_char:
                        self.step += 1
                        # file = open('result.txt', mode='a')  # mode (режим): запись в конец
                        # file_content = line
                        # file.write(file_content)
                    else:
                        self.pref_char = line[12:14]
                        if self.z > 2:
                            print(f'{line[0:14]}] {self.step}')
                        self.step = 1


parser = Parser(file_name='events.txt')
parser.collect_min()
