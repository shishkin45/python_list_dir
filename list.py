import os
import time

#Переходим в корневой каталог c:\
os.chdir("c:\\")

#Получаем список файлов и папок в текущем каталоге
list_dir_all = os.listdir()

#Делим содержимое каталога на два массива: 1)папки, 2)файлы.
list_dir = []
list_file = []

for i in list_dir_all:
    if os.path.isdir(i):
        list_dir.append(i)
    elif os.path.isfile(i):
        list_file.append(i)

list_dir.sort()
list_file.sort()

#Выводим на экран папки
for i in list_dir:
#выравнивание длины
    len_path = len(i)
    len_add = 50 - len(i)
    fill = " " * len_add
    print (i,fill,"DIR")
    time.sleep(.3)

#выводим файлы
for i in list_file:
#выравнивание длины
    len_path = len(i)
    len_add = 50 - len(i)
    fill = "." * len_add
    print (i, fill)
    time.sleep(.3)