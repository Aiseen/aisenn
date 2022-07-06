# Введение в функции. Позиционные и именованные, *agrs* и **kwargs, аргументы по default

 # функция это именованный блок кода ....




# def func1(x,y):
#     print('hello')
#     return x + y
    
 
# print(func1(2,1))


# def func1(x):
#     print('hello world')
#     return x

# print(func1('hello world'))


# def func2(str_,num) : # параметры
#     res = str_ * num
#     return f'новая строка -{res}'


# n = 5

# print(func2('hello',n)) # аргументы

# Аннотация функций - подсказки к аргументам функции и возвращемому значению
# def func3(num1: int,num2: int) -> int :
#     return num1 + num2 

# print(func3(1,2))


# def func3(num1,num2):
#     return num1 + num2 

# print(func3('f','1'))




# def func4(num1,num2) :
#     return num1 * num2

# print(func4(2,2))



# def func4(num1,num2=1) :
#     return num1 * num2

# print(func4(2))


# def func5(num1,num2,num3):
#     return num1+num2+ num3

# print(func5(1,2,3))



# def func5(num1,*args) :
#     print(num1)
#     print(args)

#     res = 0
#     for i in args :
#         res += i
#         return res
# print(func5(1,2,3,4,5))

# подучить

# def func6(num1,num2,num3) :
#     return num1//num2 + num3


# print(func6(5,2,3)) # позиционные аргументы
# print(func6(num2 =5,num1=2,num3=3)) #именнованые
# print(func6(1,num3 = 1, num2 = 2))
# print(func6(num1 = 1 ,2,3)) #Error


# def func7(name,age,*args,**kwargs):
#     print(name)
#     print(age)
#     print(args)
#     print(kwargs)

# func7('John',30,'kg','bishkek',hobby='fishing',age2 = 32)



# def fun1(num1,num2):
#     return num1 + num2

# def fun2(num1,num2):
#     return num1 - num2


# def fun3():

#  num1 = int(input('num1:'))
#  num2 = int(input('num2:'))
#  operator = input('+ or - :')
#  if operator == '+':
#     return(fun1(num1, num2))

#  elif operator == '-':
#     return(fun2(num1, num2))

# while True :
#     answer = input('хотите продолжить?')
#     if answer == 'Да':
#      print(fun3())
#     else:
#          break


# def func10(tuple_,*args) :
#     print(tuple_)
#     print(args)
# print(func10((1,2,3)))
# print(func10((1,2,3,4),1,2,3,4)) #10,10



# t = (1,2,3,4)
# arg = (1,2,3,4)
# for i in t :
#     print(sum(t))
#     break

# for i in arg :
#     print(sum(arg))
#     break


# def my_range(end_=0,start_=0,step_=1):
#     return list(range(start_,end_,step_))

# print(my_range(5,0,1))
# print(my_range(5))



# def is_even(x:int) -> bool :
#     if x %2==0:
#         return True
#     else:
#         return False
# num1 = int(input('Введите число:'))
# print(is_even(num1))
