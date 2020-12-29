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

    index1 = 0
    index2 = 0
    max = 0
    List_just_a = []
    list_max_a = []
    for f in list_files:
    #пока кладем в отдельную папку только файлы без обновления вообще
        if (f.find('[a')!=-1):
            index1 = f.find('[a')
            index2 = f.find('.tap')

            if f[index1 + 2].isdigit() and f[index1 + 3].isdigit():
                if max < int(f[index1 + 2] + f[index1 + 3]):
                    max = int(f[index1 + 2] + f[index1 + 3])

            elif f[index1 + 2].isdigit():
                if max < int(f[index1 + 2]):
                    max = int(f[index1 + 2])
            else:
                List_just_a.append(f)

                #print(f[0:index1] + '[a' + str(max) + ']' + f[index2:len(f)])
        else:
            list_of_delete.append(f)
    try:
        os.mkdir('dont_a_files')
    except(FileExistsError):
        print('Всё нормально, просто такая папка уже есть. Копирую в неё')

    # рекурсивно перемещает файл или директорию (src) в другое место (dst), и возвращает место назначения.
    for file_of_delete in list_of_delete:
        shutil.move(file_of_delete, path_name + 'dont_a_files/')
        print(file_of_delete, 'перемещен в папку dont_a_files')
