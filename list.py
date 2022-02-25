import os
import time

list_dir = os.listdir()
#сортировка
list_dir.sort()
print (list_dir)
#меняем текущий каталог
print("Переходим в корневой каталог. ")
print ("Список файлов:")
os.chdir("c:\\")
path = os.getcwd()
list_dir = os.listdir()
print (path)
print("Кол-во элементов:", len(list_dir))
#перебор элементов списка
for i in list_dir:
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


#2 commit_2
