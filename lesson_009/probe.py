# -*- coding: utf-8 -*-
import os
import zipfile


class Parser:
    pref_char = 0
    step = 1

    def __init__(self, file_name):
        self.file_name = file_name
        # self.stat = {}

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
                if 'NOK' in line:
                    if line[16] == self.pref_char:
                        self.step += 1
                        # file = open('result.txt', mode='a')  # mode (режим): запись в конец
                        # file_content = line
                        # file.write(file_content)
                    else:
                        # self.step = 1
                        self.pref_char = line[16]
                    # print(self.step)
                    # print('NOK найдена в строке', line)
    #                 self.pars(line=line)
                        print(f'{line[0:17]}] {self.step}')
                        self.step = 1
    #
    # def pars(self, line):
    #     for char in line:
    #         print([16])

            # if char[16] == self.pref_char:
            #     # step += 1
            #     file = open('result.txt', mode='a')  # mode (режим): запись в конец
            #     file_content = line
            #     file.write(file_content)
            # self.pref_char = char[16]
parser = Parser(file_name='events.txt')
parser.collect()
