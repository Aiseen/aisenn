# Работа с файлами. JSON. import (from)

# Библиотека - это просто набор модулей и функций.
# модуль - это файл с расширением .py, который определяет некоторые функции 
# и переменные

# пакет - набор модулей которые упаковывают для удобства управления


# встроенные модули :
# math
# datetime
# random
# functools


# import math
# print(math.pi)
# print(dir(math))


# from math import pi as PI
# print(PI)`

# from math import *
# print(sin)

# from test import hello
# print(hello)

# from my_package.test2 import age
# print(age)
# from my_package.test2 import age
# print(age)


# from my_package.test2 import age


# print(my_packagename)


# pi = 1
# print(pi)
# from math import pi
# print(pi)



################# файлы

# open()

# file = open('my_fiels/test1.txt','r')
# print(file.tell())

# print(file.read())
# print(file.seek(0))
# print('**********')
# print(file.tell())
# print(file.read())
# file.close()

# file = open('my_fiels/test1.txt','r')
# print(file.read(6))
# print(file.tell())
# file.close()

# file = open('my_fiels/test1.txt','r')
# for i in file :
#     print(i)

# file = open('my_fiels/test1.txt','r')
# # print(file.readline(3))
# print(file.readlines(33))

# file = open('my_fiels/test1.txt','r')
# print(file.readline())
# print(file.readline())


# for i in file.readlines():
#     print(i)

# for i in range(5):
    # print(file.readline())

# str_ = file.read()
# str_ = str_.replace('/n','')
# print(str_)

############ Запись в файл


# file = open('my_fiels/test2.txt','w') # создали тхт 

# # file.write(str(2))


# for i in range(100):
#     # file.seek(4)
#     file.write(str(i)+'\n')
# file.write(str(['asd','None']))
# file.writelines(['age',' ','siu']) # без разделителя

# with open('my_fiels/test2.txt','w')   as file:
#     file.write('hello world')
# print(file.write('asdas')) #error


# with open('my_fiels/test3.txt','a') as file:
#     file.write('hello\n')




# with open('my_fiels/test2.txt','w+') as file:
#     file.write('hello\n')
#     print(file.seek(0))
#     print(file.read())  
  



# file = open('my_fiels/task1.txt','r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())



# file = open('my_fiels/task2.txt','r')
# file1 = file.read()
# print(file1)

# file = open('my_fiels/task3.txt','w')
# print(file.writelines('1 2 3 4 5 6 7 8 9 10')) 

# file = open('my_fiels/task3.txt','w')
# print(file.write('1 2 3 4 5 6 7 8 9 10'))


# file = open('my_fiels/task4.txt','w')
# str_ = ['1\n' ,'2\n', '3\n','4\n','5\n','6\n','7\n','8\n','9\n','10\n','11\n','12\n','13\n','14\n','15\n']
# file.writelines(str_)
# file = open('my_fiels/task4.txt','r')
# file1 = file.read()
# print(file1)
# print(len(str_))



# file = open('task4.txt','w')
# str_ = ['1\n' ,'2\n', '3\n','4\n','5\n','6\n','7\n','8\n','9\n','10\n','11\n','12\n','13\n','14\n','15\n']
# file.writelines(str_)
# file = open('task4.txt','r')
# file1 = file.read()
# print(file1)
# print(len(str_))




