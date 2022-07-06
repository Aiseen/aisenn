# Логические выражения и операторы Python.
# NoneType.Условные операторы(if)

#print(type(True))
#print(type(False))

#bool - неизменяемый тип данных,который содержит только два значения:
#True - истина (да) -> 1
# False - Ложь (нет) -> 0

num1 = 10
num2 = 5


#print(num1 > num2) #true
#print(num1<num2) #false
#print( 5 >= 5) # true
#print(4<= 4) #true
#print(num1 == num2) #false
#print(num1 != num2) # != (не равен)


#print('a' > 'hello') #по первым буквам
#print(ord('a'))
#print(ord('h'))

#print(len('az') > len('ahello')) #  по длине строк

#some_str = 'hello'
#print('w ' in some_str) # false
#print('helo'in some_str) # false
#print('l' in some_str) #true

#not and or

#print(not True) # False
#print(not False) #True





#print(True and True) #True
#print(age>18 and name == 'John')
#print(True and False) # False
#print(age>18 and name == 'Steve')
#print(False and True) # False
#print(age > 50 and name == 'John')
#print(False and False) # False
#print (age > 25 and name == 'Steve')

#age = 19
#name = 'John'

#print(age > 18 or name == 'John') #True

#print(age > 18 or name == 'Steve') #True

#print(age > 50 or name == 'John') #True

#print(age == 5 or name == 'Steve') #False

#print((True or False) and True) # True
#print((True or False)and False) # False
#print((False == False)and True) #  True (False == False = правда)

# 2+2 * 2  = 6
# (2+2) * 2 = 8

#a = 'hello'
#b = 'hello'
#print(a == b) #True, == -сравнивает значение
#print(a is b ) # True, is сравнивает по id

#print(id(a))
#print(id(b))

#list_ = [1,2]
#list_2 = [1,2]

#print(list_==list_2) #True
#print(list_ is list_2) # False

#print(id(list_))
#print(id(list_2))
 
#NoneType - пустота
#res = None
#print(type(res)) 


#AGE = 18
#NAME = 'john'

#age = int(input('Введите ваш возраст:'))
#name = input('Укажите свое имя:')

#if age>= AGE and name.lower() == NAME :
  # print(f'Привет {name.title()}, ты vip клиент!')

#else:
 #   print('Вы не подходите')

#print('пока!')


#num1 = int(input('Введите первое число:'))
#num2 = int(input('Введите второе число:'))
#operator = input('ВВедите оператор(+,-,*,**,/):')

#if operator == '+':
 #   print(num1+num2)

#elif operator == '-':
 #   print(num1 - num2)
#elif operator == '*' :
 #   print(num1*num2)
#elif operator == '/':
 #   print(num1/num2)

#else:
 #   print('Нет такого оператора у нас в программе!')


# if 1 :
#     print('hello')
# print(bool(1))
# print(bool(0))
# print(bool(1000))
# print(bool(-1))
# print(bool(None))
# print(bool(-2))

