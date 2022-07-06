
# import random
# random.choice('0123456789')


# def get_info():
#     name = input('Введите ваше имя')
#     surname = input('Введите вашу фамилию')
#     # return name and surname
#     global get_info
#     def genarate_password():
#         password = name + surname
#         print(''.join([random.choice('0123456789') for i in range(8)]))
#         print(genarate_password)



# def genarate_password(name,last_name):
#     code = [random.choice('012345678') for i in range(8)]
#     return name+ last_name + ''.join(code)

# def get_info():
#     name = input('enter your name:')
#     last_name = input('enter your lastname')
#     return genarate_password(name,last_name)

# print(get_info())

#Области видимости
# LEGB

# def func():
#     x = 5 #enclosed
#     def func2():
#         # x = 20
#         print(x)
#     func2()
# func()



# global_ = 0
# for i in range(10):
#     global_ += 1
# print(global_)



# var = 0
# def func():
#     global var
#     var += 1
#     return var

# print(var)
# print(func())
# print(func())
# print(func())




# def foo():
#     var = 'переменная foo' #enclosed
    
#     def bar():
#         global var
#         var = 'перемененная bar' #local
#     bar()
#     print('переменная в foo',var)

# foo()
# print('переменная в foo', var)


# L -  видит все (тело функции)
# E - Global,built in (внешняя функция)
# G - Built in (все на уровне исполняемого файла)
# B - - (мы не видим его)
 
 

# LEGB




# list_ = ['level','hello','down','wow','lmao','lol']
# r1 = list(map(lambda x: x if x == x [::-1] else None ,list_))
# print(r1)

# `list_ = ['123','12ds','54','das','142']
# # r1 = list(filter(lambda x: x.isdigit() ,list_))
# # r2 = list(map(lambda x: int(x),r1))
# # print(r2)

# lst = list(map(int,list(filter(lambda x: x.isdigit(),list_))))

# print(lst)

def is_prime(number):
    if number >=0 and number <=1000 and number!= 1:
        for i in range(2,number): # ты передал 6.
            if number%1 == 0: # рассмотри в цикле все числа до 6. 2,3,4,5
                return False
            return True
    else:
        return False



print(is_prime(7))