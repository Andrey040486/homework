# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

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
                            shutil.copy2(full_file_path1, target_folder_normalized + '\\' + str(file_time[0]) + '\\' + str(file_time[1]) + '\\' + str(file_time[2]))
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

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
