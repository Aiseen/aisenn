# Циклы в  Python. Цикл While и цикл for. Кортеж(tuple)

#tuple - неизменяемый, упорядоченный и итерируемый тип данных

# tuple_ = (1,2,3,4, 'hello',True, ['a','b'])
# # print(type(tuple_))
# # print(dir(tuple_))\
# print(tuple_.count(1)) #2
# print(tuple_.index('hello')) # 4
# tuple_[-1].append('c')
# print(tuple_)

####### Циклы
# while True :
#    name = input('Введите ваше имя:')

#    if name == 'John' :
#       print('Hello John')
      #break - прервать

# age = 18
# age2 = int(input('Введите ваш возраст'))
# while age2 <=  18 :
#     age2 = int(input('Введите ваш возраст еще раз'))
# else:
#     print('Good')

# count_ = 0
# while True :
#     count_ += 1
#     print(count_)
# play = True
# while play:
#     num1 = int(input('num1: '))
#     num2 = int(input('num2:'))
#     operation = input('Введите ''+'' или ''-'' :')
#     if operation == '+':
#         print(num1+num2)
#     elif operation == '-' :
#         print(num1-num1)
#     else :
#         print('Такой операции нет!')

#     f = input('Хотите завершить работу?(Yes)')
#     if f == 'Yes':
#         play = False
#         print('See you!')

# list_= ['hello',True, 'Sam']
# i = 0
# while i < len(list_):
#     print(list_[i]) # 0 1 2
#     i += 1
# print(list_[0])
# print(list_[1])
# print(list_[2])

# list_= ['hello',True, 'Sam']
# for i in list_:
#     print(i) # вместо i можем любую строку


# text = 'hello world'
# for i in text:
#   print(i)

# for i in range(5):
#     print(i)

# for i in range(1,6) :
#     print(i)

# for i in range(0,100,3) :
#     print(i)

# list_ = list(range(100))
# print(list_)

# for i in range(5):
#     if i == 3:
#          continue
#     print(i)

# list_ = []
# list_2 = []
# for i in range(101):
#     if i % 2 == 0 :
#         list_.append(i)
# else:
#     list_2.append(i)
# print(list_)
# print(list_2)


# list_ = ['Alex', 'Sam', 'John', 'Tom', 'Snow']
# for i in list_ :
#     if i != 'Snow' :
#         print(f'Привет {i}')
#     else :
#         print(f'Пока {i}')

# list_ = [[1,2], [1,2,3], ['hello']]
#  for i in list_ :
#     # print(f'start {i}')
#    # for j in i :
#   #     print(j) 
#    # print(f'end {i}')   

### вверхнее повторить

# for i in str(2):
#     print(i)

# import random
# print(random.randint(0,10))


# import random

# list_ = []
# for i in range(100):
#     list_.append(random.randint(0,10))
# print(list(set(list_)))


# for i in range(21):
#     if i % 2 == 0 :
#         print(i**2)
# else :
#     print(i**5)
  
