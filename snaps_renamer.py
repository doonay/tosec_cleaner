#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

'''
Убераем окончания у видеопревьюшек
(USA)
(Europe)
(France)
'''


if __name__ == "__main__":
    path_name = 'H:/emulation/roms/c64/snaps'
    os.chdir(path_name)
    print("Выбрана папка {}".format(path_name))
    list_files = os.listdir(path=".")
    new_list_files = []

    for f in list_files:
        #переименовываем файл
        if (f.find('(USA)')!=-1):
            x = f.find('(USA)')
            new_list_files.append(f[0:x] + f[x+4:len(f)])
    
    for filename in new_list_files:
        print(filename)
        #os.rename(f, new_filename)

                                                                                                                                                                                                                                                                                                                                                                                         