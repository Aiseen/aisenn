# `def func() :
#     print('Umar loh')
#     print('Aisen krasava0')
#     print('U kinda fuckeless')
# func()
# print('Siiu')
# func()`

# def f(x):
#     print('Квадрат числа',x,'=',x**2)
# for i in range(1,11):
#     f(i)

# def multipplt(a,b):
#     print(a*b)
# multipplt(3,5)


# def siu(a):
#     if a%2== 0 :
#         print(a,'четное')
#     else :
#         print(a,'нечетное')
# for i in range(100,200):
#  siu(i)

# def factorial(n):
#     a = 1
#     for i in range(1,n+1):
#         a = a*i
#     print(a)
# factorial(10)

# def func(x,y):
#     res = x+y
#     return res
# print(func('hello','world'))





# def func(r,w,y = 3):
#     res = r+y
#     res *= w
#     return res
# print(func(2,4))


# def func(*args):
#     return args
# print(func(1,14,12,1412,134))

# def func(x,y):
#     print(max(x,y))
# func(14,3)
# def func(x,y):
#     return max(x,y)
# print(func(41,13))

# def func(a,b,c,d):
#     print(a,b,c,d**2)
# func(1,2,3,4)

# list_ = [4,50,61,71]
# list2_ = []
# list2_ = [i**2 for i in list_]
# print(list2_)`

# list_ = [10,11,12,15,16,47]
# list_ = [ i for i in list_ if i%2 == 0]
# print(list_)



# def func(dict) :
#      print(dict)


# # dict= {k:k for k,v in dict.items()}


# dict_ = {'siu':'maekrs','car':'audi'}
# dict_ = {k: k  for k in dict_.items()}
# print(dict_)


# def foo():
#     var = 'переменная foo'

#     def bar():
#         global x 
#         var = 'переменная bar'
#         print(var)

#     bar()
#     print("переменная в foo: ", var)

# var = 'переменная bar'
# foo()
# print("переменная в foo: ", var)



# def foo():
#     var = 'переменная foo'

#     def bar():
#         var = 'переменная bar'

#     bar()
#     print("переменная в foo: ", var)

# var = 'переменная bar'
# foo()
# print("переменная в foo: ", var)



# `x = 'Я глобальная переменная'
# def func():
#     global x
#     x = 'я могу измениться!'
# func()
# # print(x)
# print(globals()['x'])

# num = 3

# def mul(num):
#     # global num
#     print(num**2)
#     return num
# mul(num)
# print(num)


# num = 3
# def func():
#     global num
#     num = num**2
#     return num
# func()
# print(num)


# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
#     return balance
    
# get_salary(500)
# print(balance)
# def pay_bills(amount,log_name):
#     global balance
#     balance = balance - amount
#     log_name = 'Интернет'
#     log_name = (f'вы заплатили- {amount}, за - {log_name}')
#     return balance
# pay_bills(300,'интернет')
# print(balance)



# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
#     return balance
    
# get_salary(500)
# print(balance)

# def pay_bills(amount,log_name):
#     global balance  
#     balance = balance - amount   
#     log_name = (f'вы потратили - {amount} сом за  {log_name}') 
#     print(log_name)
# pay_bills(200,'электричество')

# def get_balance():
#     global balance
#     balance = (f'у вас на счету {balance} сом ')
#     print(balance)
# get_balance()


# result = 0

# def pow_first(x, y):
#     global result
#     result = x*y
#     return result
# pow_first(2,3) 

 
# def pow_second(z):
#     global result
#     result = result%z
#     return result
# pow_second(4)
# print(result)


# list1 = ['aisen','malika','roman'] 
# list2 = []

# def func():
    
# func()
# print(list1)


# list1= [12,14,2,4,1,43]

# for i in list1 :
#     if i <7 :
#         print(i)

# list1= []
# def func():
#     global list1
#     for i in range(0,11):
#         print(i)
#         list1.append(i)
        
# func()
# print(list1)      

# list_1 = [1,2,4,10]
# list_2 = []

# def factorial(a,b,c,d):
#     a = 1
#     for i in range(1,a+1):
#   
# 
#      a = a*i
#     print(a)
# factorial(1,2,4,10)

# list1_ = [1,5,6,15]
# for i in list1_:
#     print(max(list1_))
#     break





# list_ = [11,12,10,15]
# r1 = list(map(lambda x: x**2,list_))
# print(r1)

# list_ = [-1, 2, 3, 0, 5, -3, 7]
# r1 = list(map(lambda x: False if x<0 else True , list_ ))
# print(r1)

# list_ = [1,2,5,15,10,11,14]
# r1 = list(filter(lambda x: x%2 == 0,list_))
# print(r1)

# list_ = ['aisen','makers','aaaaaaa','telephone','siu']
# r1 = list(filter(lambda x: len(x)>7,list_))
# print(r1)

# list_ = [11,12,14,15,10,5]
# r1 = list(filter(lambda x:  x%2 == 0 , list_))
# r2 = list(filter(lambda x: x%2 != 0, list_))
# print(len(r1))
# print(len(r2))


# list_ = [1,2,3,15,16,8,14,0]
# r1 = list(filter(lambda x: x>3, list_))
# print(len(r1))

# list_ = [-1,0,-2,15,11]
# r1 = list(filter(lambda x: x>=0,list_))
# print(r1)
# print(len(r1))

# list_ = [1,2,3,15,16,8,14,0]
# # r1 = list(filter(lambda x: x>3, list_))
# print(all((i > 3 for i in list_)))

# list_ = [-1,0,-2,15,11]
# print(any(i>=0 for i in list_))

# arr_raf=[1,0,3]

# arr_nov=[2,2,1]

# count_raf=0

# count_nov=0

# for i in range(len(arr_raf)):

#    if arr_raf[i]>arr_nov[i]:

#        count_raf+=1

#    if arr_raf[i]==arr_nov[i]:

#        count_raf+=1

#        count_nov+=1

#    if arr_raf[i]<arr_nov[i]:

       

#        count_nov+=1

# if count_raf>count_nov:

#    print('Рафаель выигрывает со счётом'+' '+str(count_raf)+':'+str(count_nov))

# else:

#    print('Новак выигрывает со счётом'+' '+str(count_nov)+':'+str(count_raf))


# rafael = [1,0,3]
# novak = [2,2,1]
# set_rafael = 0
# set_novak = 0
# for i in range(len(rafael)):
#     if rafael[i]>novak[i]:
#         set_rafael +=1
# for i in range(len(novak)):
#     if rafael[i]<novak[i]:
#         set_novak +=1
# if set_rafael > set_novak :
#     print(f'Рафаэль выйгрывает  со счетом - {set_rafael} - {set_novak}')
# else:
#     print(f'Новак выйгрывает со счетом - {set_novak} - {set_rafael}')

 
#import math
# a = math.pi
# print(a)


# print(divmod(15,6))

# list_ = ['aisen','map','makers','aaaaaaba','homework']
# list2_ = list(filter(lambda x: len(x) > 7,list_))
# print(list2_)


# `list_ = [-1, 2, 3, 0, 5, -3,7,]
# list_ = list(map(lambda x: True if x> 0 else False,list_))
# print(list_)`

# a = 25
# b = 36
# c = 40

# if c>a and c> b :
#     print(c)

# a = 25
# b = 36
# c = 40

# if 1 > 0:
#    print(max(a,b,c))


# list_ = [11, 12,13,1521,13,19]
# list_2 = len(list(filter(lambda x: x % 2 == 0 ,list_)))
# list_3 = len(list(filter(lambda x: x % 2 != 0,list_)))
# print(list_2)
# print(list_3)


# def func():
#     a = input('Введите  слово')
#     if a [::-1]:
#         print('Это палиндром!')
#     else : 
#         print('Это не палирдрмо')
# func()


