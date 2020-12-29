#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

'''
Убераем окончания у видеопревьюшек
(USA)
(Europe)
(France)

Слишком много движений. Вынести цикл в функцию!
'''


if __name__ == "__main__":
    path_name = 'H:/emulation/roms/c64/snaps'
    os.chdir(path_name)
    print("Выбрана папка {}".format(path_name))
    list_files = os.listdir(path=".")
    new_list_files = []

#Elvira II (Europe) (Disk 1 Side A)
    for f in list_files:
        #переименовываем файл
        if (f.find('(Disk 1 Side A)')!=-1):
            x = f.find('(Disk 1 Side A)')
            #new_list_files.append(f[0:x-1] + f[x+15:len(f)])
            newfile = f[0:x-1] + f[x+15:len(f)]
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #переименовываем файл
        if (f.find('(Disk 1)')!=-1):
            x = f.find('(Disk 1)')
            #new_list_files.append(f[0:x-1] + f[x+15:len(f)])
            newfile = f[0:x-1] + f[x+8:len(f)]
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #Fourth Protocol, The (Europe) (Side B).mp4
        if (f.find('(Side B)')!=-1):
            x = f.find('(Side B)')
            newfile = f[0:x-1] + f[x+8:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            os.rename(f, newfile)

    for f in list_files:
        if (f.find('(Europe)')!=-1):
            x = f.find('(Europe)')
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            newfile = f[0:x-1] + f[x+8:len(f)]
            os.rename(f, newfile)

    for f in list_files:
        if (f.find('(USA)')!=-1):
            x = f.find('(USA)')
            #new_list_files.append(f[0:x-1] + f[x+5:len(f)])
            newfile = f[0:x-1] + f[x+5:len(f)]
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #Fourth Protocol, The (Europe) (Side A).mp4
        if (f.find('(Side A)')!=-1):
            x = f.find('(Side A)')
            newfile = f[0:x-1] + f[x+8:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #Fourth Protocol, The (Europe) (Side A).mp4
        if (f.find('(Sweden)')!=-1):
            x = f.find('(Sweden)')
            newfile = f[0:x-1] + f[x+8:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #Fourth Protocol, The (Europe) (Side A).mp4
        if (f.find('(Germany)')!=-1):
            x = f.find('(Germany)')
            newfile = f[0:x-1] + f[x+9:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #Fourth Protocol, The (Europe) (Side A).mp4
        if (f.find('(France)')!=-1):
            x = f.find('(France)')
            newfile = f[0:x-1] + f[x+8:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for f in list_files:
        #Fourth Protocol, The (Europe) (Side A).mp4
        if (f.find('(Spain)')!=-1):
            x = f.find('(Spain)')
            newfile = f[0:x-1] + f[x+7:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)
    for f in list_files:
        #Fourth Protocol, The (Europe) (Side A).mp4
        if (f.find('(Unl)')!=-1):
            x = f.find('(Unl)')
            newfile = f[0:x-1] + f[x+5:len(f)]
            #new_list_files.append(f[0:x-1] + f[x+8:len(f)])
            try:
                os.rename(f, newfile)
            except(FileExistsError):
                os.rename(f, '_delete_this_' + newfile)

    for name in list_files:
        if name.find('(') != -1:
            print(name)

                                                                                                                                                                                                                                                                                                                                                                                         