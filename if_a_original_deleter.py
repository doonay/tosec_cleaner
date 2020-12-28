#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import shutil

'''
[a] — это альтернативная версия оригинальной версии игры, которую выпустили позже официальной даты выпуска игры. Как правило эта версия несла в себе исправления багов, замеченные в оригинальной версии или даже отменяла коды Game Genie.
Если присутствует [a], то удаляем оригинал
'''


if __name__ == "__main__":
    path_name = 'H:/emulation/roms/c64/Games/[TAP]/'
    os.chdir(path_name)
    print("Выбрана папка {}".format(path_name))
    list_files = os.listdir(path=".")
    list_of_a = []
    list_of_delete = []

    for f in list_files:
    #если присутствует [a]-ром, удаляем оригинал
        if (f.rfind('[a]')!=-1):
            list_of_a.append(f)

    index = 0
    for i in list_of_a:
        index = i.rfind('[a]')
        #print(i[0:index] + i[index+3:len(i)])
        for j in list_files:
            if (i[0:index] + i[index+3:len(i)]) == j:
                #print(i, j)
                #print(i[0:index] + i[index+3:len(i)], j)
                list_of_delete.append(j)

    try:
        os.mkdir('original_files')
    except(FileExistsError):
        print('Всё нормально, просто такая папка уже есть. Копирую в неё')

    # рекурсивно перемещает файл или директорию (src) в другое место (dst), и возвращает место назначения.
    for file_of_delete in list_of_delete:
        shutil.move(file_of_delete, path_name + 'original_files/')
        print(file_of_delete, 'перемещен в папку original_files')