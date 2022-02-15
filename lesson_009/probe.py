# -*- coding: utf-8 -*-
import os
import time
import shutil


class Sorter:
    prev_char = 0

    def __init__(self, origin_folder, target_folder):
        self.origin_folder = origin_folder
        self.target_folder = target_folder

    def sorted(self):
        origin_folder_normalized = os.path.normpath(self.origin_folder)
        target_folder_normalized = os.path.normpath(self.target_folder)
        for dirpath, dirnames, filenames in os.walk(origin_folder_normalized):
            # print('*' * 27)
            # print(dirpath, dirnames, filenames)
            print(os.path.dirname(dirpath))
            for file in filenames:
                full_file_path1 = os.path.join(dirpath, file)
                full_file_path2 = os.path.join(target_folder_normalized, file)
                secs = os.path.getmtime(full_file_path1)
                file_time = time.gmtime(secs)
                if file_time[0] == self.prev_char:
                    shutil.copy2(full_file_path1, target_folder_normalized + '\\' + str(file_time[0]))
                    print(full_file_path1, secs, file_time)
                else:
                    self.prev_char = file_time[0]
                    os.makedirs(target_folder_normalized + '\\' + str(file_time[0]))


sort = Sorter(origin_folder='E:/icons', target_folder='E:/icons_by_year')
sort.sorted()
