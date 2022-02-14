# -*- coding: utf-8 -*-
import os
import zipfile


class Sorter:

    def __init__(self, file_name):
        self.file_name = file_name

    def unzip(self):
        z = zipfile.ZipFile(self.file_name)
        with z:
            z.extractall('E:')

    def sorted(self):
        pass


sort = Sorter('icons.zip')
sort.unzip()
