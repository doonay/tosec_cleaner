#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import shutil

'''
[a1] еще доработаннее, чем [a].
Если присутствует [a[n+1]], то удаляем [a[n]]
'''


if __name__ == "__main__":
    path_name = 'H:/emulation/roms/c64/Games/[TAP]/'
    os.chdir(path_name)
    print("Выбрана папка {}".format(path_name))
    list_files = os.listdir(path=".")
    a_bigest = 0
    list_of_delete = []

    index = 0
    for f in list_files:
    #если попался [an], где n больший, чем a_bigest, в a_bigest записываем новый номер и удаляем файл с предыдущим a
        if (f.find('[a')!=-1):
            index = f.rfind('[a]') + 3
            print(index)



