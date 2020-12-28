#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import shutil

'''
Сразу удаляем [b] — Плохой дамп. Почти всегда этот РОМ просто испорчен при закачке из интернета, но бывают случае, когда его задампили с ошибками. Но это не значит, что в эту игру нельзя играть, глюк может появиться в музыке или в графике, что не повлияет на саму игру.
'''


if __name__ == "__main__":
    path_name = 'H:/emulation/roms/c64/Games/[TAP]/'
    os.chdir(path_name)
    print("Выбрана папка {}".format(path_name))
    list_files = os.listdir(path=".")
    list_of_delete = []

    for f in list_files:
    #сразу удаляем [b]
        if (f.find('[b]')!=-1):
            list_of_delete.append(f)

    try:
        os.mkdir('b_files')
    except(FileExistsError):
        print('Всё нормально, просто такая папка уже есть. Копирую в неё')


    # рекурсивно перемещает файл или директорию (src) в другое место (dst), и возвращает место назначения.
    for file_of_delete in list_of_delete:
        shutil.move(file_of_delete, path_name + 'b_files/')
        print(file_of_delete, 'перемещен в папку b_files')