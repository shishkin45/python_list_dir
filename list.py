import os
import time

#Переходим в корневой каталог c:\
os.chdir("c:\\")

#Получаем список файлов и папок в текущем каталоге
list_dir_all = os.listdir()

#Делим содержимое каталога на два массива: 1)папки, 2)файлы.

print (list_dir_all)
#сортируем массив по алфавиту
list_dir_all.sort()
print (list_dir_all)

path = os.getcwd()
list_dir = os.listdir()
print (path)
print("Кол-во элементов:", len(list_dir_all))
#перебор элементов списка
for i in list_dir_all:
    if os.path.isdir(i):
        type = "dir"
    elif os.path.isfile(i):
        type = "file"
#выравнивание длины
    len_path = len(i)
    len_add = 50 - len(i)
    fill = "." * len_add
    print (i, fill, type)
    time.sleep(.3)
