# Dict
# Comprehensions
# Try - except
#Functions

# Словарь - изменяемый, неупорядоченый тип данных, в котором хранятся пары в виде клбч и значение. Ключ - любой неизменяемый тип данных. Значение - любой тип данных.


# Comprehensions - Генераторы последовательности.
# # Cинтаксис:
# [действие for элемент in последовательности  [if условие]]
# [   i   for  i in range(1,11) if i%2 == 0  ]

# comprehension с фильтрами  
# list_ = [i for i in range(1,11) if i%2 != 0]
# l = []

# for i in range(1,11):
#     if i%2 != 0:
#      l.append(i)
# print(list_)
# print(l)


# comprehension с тернарными условиями
# res = [True if i%2 ==0 else False for i in range(1,11)]
# print(res)
# l = []
# for i in range(1,11) :
#     if i % 2 == 0:
#         l.append(True)
#     else:
#         l.append(False)
# print(l)


# dict_ = {i: i**2 for i in range(1,11)}
# print(dict_)


# a = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# a = {
#  k:inner_key for k,v in a.items() 
#  for  inner_key, inner_value in v.items()
#   if inner_value == max(v.values())


# }
# print(a)


# Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Нужно использовать comprehension.
# Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}

# my_dict = {'first': {'a': 1}, 
# 'second': {'b': 2}

# }

# my_dict_ = {k: i_v  for k,v in my_dict.items() for i_k, i_v in v.items()}
# print(my_dict)


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# # a = {k:[i for i in range(1,v+1)]for k,v in a.items()}
# print(a)

# res = {}
# for k,v in a.items() :
#     lst = [i for i in range(1,v+1)]
#     res.update({k:lst})
# print(res)
    
# import random

# set1 = {random.randint(0,10) for i in range(10)}
# set2 = {random.randint(0,10) for i in range(10)}
# res = (set1.union(set2))
# if len(res) < 20 :
#     print(f'В этом сете было {20 - len(res)} повторений, его длина составляет {len(res)}')`


####### try - except - конструкция, для обработки исключений и ошибок.
#Синтаксические ошибки мы не можем обработать

# Синтаксис : 

# try:

# код, который может вызвать ошибку

# except :

# код, который сработает если ошибка возникла

# else :

# Код, который сработает если ошибка не возникла

# finally :
# код, который сработает в любом случае(даже когда сломался)




# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е. нтаксис : 

#соединение, строк. В остальных случаях введенные числа суммируются.


# try :
#     a = input('Enter:')
#     b = input('Enter:')
#     int(a)
#     int(b)
# except ValueError :
#     print('Вы ввели не число!')
#     print(a+b)
# else :
#     print(int(a)+int(b))`



# Запросите у пользователя несколько слов и чисел введенных через пробел, затем поместите эти слова в список,
#  переберите этот список циклом и перевидете все строки в тип данных число, все числа поместите в отдельный список,
#   а на возникающие ошибки выводите исключение: 'Данный элемент не является числом!'


# inp =input('Enter values :')
# list_ = inp.split()
# list2_ = []
# for i in list_ :
#     try:
#         list2_.append(int(i))
#     except ValueError:
#         print('Данный элемент не является числом')
# print(list2_)



# Functions
'''
Функция - именованный блок кода, выполняющий какие либо действия и возвращающий какой либо результат.
Мы Можем вызывать функцию, обращаясь к ней по имени и используя круглые скобочки. 
Код который прописан внутри функции будет работать только когда вы ее вызовите.

'''



# def func(a,b) : # параметры мы задаем
#     print(a+b)
#     print('hello') # тело функции

# func(a=4,b=5) аргументы передаем

# Types of arguments
'''
Позиционные
Именованные
Необязательные( *args)
Ключевые (*kwargs)

'''

#Очередь принятия параметров
#       a,b       c = 6

# def func(позиционные, с дефолтом,  *args,*kwargs):
#     args - tuple
#     kwargs - dictionary


#  Очередь передачи аргументов 
# func(позиционные,необязательные,ключ = значение)

# def func(a,b,c=6):
#     return a+b+c
# print(func(1,2,3))



# def func(c):
#     return [ i for i in range(1,c+1)]
# print(func(8))



# accounts = [[1,5],[7,3],[3,5]]
# list_=  []
# for i in accounts :
#     list_.append(sum(i))
# print(max(list_))


# account = [[1,5],[7,3],[3,5]]
# list_ = [sum(i) for i in account]
# print(max(list_))

# accounts = [[1,5],[7,3],[3,5]]
# def func(l):
#     return max([sum(i) for i in l])

# print(func(accounts))
def f() :
 a = {'key': 13131,
    'cod': 12312313,
    'password': 223311
    }
 a = {k: k for k,v in a.items()}
f()