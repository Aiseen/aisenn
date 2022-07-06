#  Обработка исключений. Оператор  try - except
# 1) Ошибки
#      # SynraxError
  # #  2f = 2
  # if True


   #IdenrationalError -  неправильный отступ 

 #name = 'John'

 # TabError - смешивание пробелов и табов
# if True :
#     print('Hello')
#     print('Hello')

# 2) Исключения 
# ZeroDivisionError
#2/0

#TypeError
# 'hello' + 2

# ValueError

# age = int(input())
#int('str)

#IndexError
# l = [1,2,3]
#l[5]


#KeyError

# dict_ = {'a' : 'hello'}
# dict_['b']

#ModuleNotFoundError
#import math2




# import math
# from math import pi
# print(math.pi)




# #ImportError
# from math import pi22


#AttributeError
# age = 30
# age.lower()


#KeyboardInterrupt
# while True :
#     print('Hello')

# print('f')
# try:
#     2 / 0
# except ZeroDivisionError :
#     print('ОБработали исключение')
# print('f1')


# l = [1,2,3]
# try:
#     print(l[0])
# except:
#     print('Обработали')

# try:
#  num1 = int(input('num1:'))
#  num2 = int(input('num2: '))
#  print(num1/num2)
# except ValueError:
#     print('Вы ввели не число!')
# except ZeroDivisionError :
#     print('На ноль делить нельзя')



# try:
#  num1 = int(input('num1:'))
#  num2 = int(input('num2: '))
#  print(num1/num2)
# except (ValueError, ZeroDivisionError) :
#     print('Вы ввели не число!')
#     print('На ноль делить нельзя')
# try :
#  while True :
#     print('hello world')
# except KeyboardInterrupt :
#     print('Вы нажали  ctrl + c')
# print(2+2)

# try:
#  2name
# except:
#      print('f')

# list_ = [1,2,3,4,5,6]
# try:
#  for i in  range (len(list_)+1) : # range(7)
#     list_.pop()
# except IndexError :
#     print('Такого индекса нет!')      
# print(list_)

# try:
#     age = int(input('Введите ваш возраст'))
# except:
#     age = None
#     print('Вы ввели не число!')
# else: # когда в блоке try  не возникло исключения
#     print('Все хорошо, вы правильно ввели возраст')
# finally :  # сработает в любом случае
#     print('Я закончил обрабатывать исключение')
# print(age)


# age = int(input('Введите ващ возраст :'))
# if age < 18 :
#     #  raise Exception ('Вы малы!')
#     raise ZeroDivisionError ('Вы малы!')


# try:
#  age = int(input('Введите ващ возраст :'))
#  if age < 18 :
#     raise ValueError ('Вы малы!')
# except Exception:
#     print('Все хорошо мы справились с исключением!')

# print(2+2)




# try:
#     num1 = 2
#     num2 = 'adsasds'
#     print(num1/num2)
# except Exception as e :
#     print(type(e))



# try: 
#     2/0
# except Exception :
#     print('Exception')
# except ZeroDivisionError:
#     print('Zero')

