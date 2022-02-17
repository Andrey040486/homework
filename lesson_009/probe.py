# -*- coding: utf-8 -*-
import os
import time
import shutil


class Sorter:
    prev_char_Y = 0
    prev_char_M = 0
    prev_char_D = 0

    def __init__(self, origin_folder, target_folder):
        self.origin_folder = origin_folder
        self.target_folder = target_folder

    def sorted(self):
        origin_folder_normalized = os.path.normpath(self.origin_folder)
        target_folder_normalized = os.path.normpath(self.target_folder)
        for dirpath, dirnames, filenames in os.walk(origin_folder_normalized):
            print(os.path.dirname(dirpath))
            for file in filenames:
                full_file_path1 = os.path.join(dirpath, file)
                full_file_path2 = os.path.join(target_folder_normalized, file)
                secs = os.path.getmtime(full_file_path1)
                file_time = time.gmtime(secs)
                if file_time[0] == self.prev_char_Y:
                    if file_time[1] == self.prev_char_M:
                        if file_time[2] == self.prev_char_D:
                            shutil.copy2(full_file_path1,
                                         target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(
                                             file_time[1]) + '\\' + str(file_time[2]))
                        else:
                            self.prev_char_D = file_time[2]
                            os.makedirs(target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(
                                file_time[1]) + '\\' + str(file_time[2]), exist_ok=True)
                            shutil.copy2(full_file_path1,
                                         target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(
                                             file_time[1]) + '\\' + str(file_time[2]))
                    else:
                        self.prev_char_M = file_time[1]
                        os.makedirs(
                            target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(file_time[1]) + '\\' + str(
                                file_time[2]), exist_ok=True)
                        shutil.copy2(full_file_path1, target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(
                            file_time[1]) + '\\' + str(file_time[2]))
                else:
                    self.prev_char_Y = file_time[0]
                    os.makedirs(target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(file_time[1]) + '\\' + str(file_time[2]), exist_ok=True)
                    shutil.copy2(full_file_path1, target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(
                        file_time[1]) + '\\' + str(file_time[2]))


sort = Sorter(origin_folder='C:\\Users\\aik30\\Downloads', target_folder='E:/icons_by_year')
sort.sorted()
