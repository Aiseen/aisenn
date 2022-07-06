# def func(*,a=5,b=10):
#     print(a,b)

# func(7,a=2,b=3)


# is ==
# l1 = [1,2,3]
# # l2 = [1,2,3]
# # l2 = l1.copy()
# l2 = l1
# print(id(l1))
# print(id(l2))
# print(l1==l2) # сравниваем значение
# print(l1 is l2)

# l1 = [1,2,3,[5,6]]
# l2 = l1
# print(l1)
# print(l2)
# l1.pop()
# print(l1)
# print(l2)

# l1 = [1,2,3,[5,6]]
# l2 = l1.copy
# l1.remove(1)
# print(l1)
# print(l2)



# l1 = [1,2,3,[5,6]]
# l2 = l1.copy()
# l1[0] = 'hello'
# l1[-1][0]= 'world'
# print(id(l1[-1]))
# print(id(l2[-1]))

# import this cтишок пайтонистов
'''

1) Обьявление
   а) Глагол
   б) snake case
   в) () - обязательно
   г) параметры не обязательно




2) Тело функции
    а) 4 пробела
    б)return -  необязательно, но желательно (если не напишем, то будет - none)
    в) Внутри тела функции можете писать что угодно
3) Single Responsibility - принцип единой отвественности (функция доллжна отвечать только за одну логику)
4) Аргументы :
    Есть 2: позиционныые и именнованные
5) Есть понятие по дефолту
6) *args, **kwargs
7) def func(a,b): # параметры
     pass
    func(a,b) #аргументы
8) Аннотация

'''
 #def some_name():
#    

# def dunc(a=5,b=3):
#     print(a,b)
# dunc()
# dunc(2,2)
# dunc(a=5,b=5)
# dunc(5,b=55)
# dunc(1)

# def func(*args):
#     print(max(args))

# func(4,3)

# def func(*args):
#     return max(args)

# print(func(3,4))


# def func(*args):
#     res = args[0] if args[0] > args[1] else args[1]
#     return res


# print(func(4,3))


# def func1():
#     a = 4
#     def inner():
#         a+= 2
#     inner()
#     return a
# print(func1())

# def func2():
#     a = 4
#     def inner(var):
#         var += 1
#         return var
#     a = inner(a)
#     return a
# print(func2())

'''

lambda = анонимная функция 
'''


# def func1(x,y):
#     return x + y 

# func1_1 = lambda x,y : x + y
# print(func1_1(1,5))

# func1 = lambda x,y : x if x > y else y
# print(func1(53,7))



# def palindrom(words:list) -> list:
#     '''Эта функция которая проверяет является ли данное слово полиндромом'''
#     polindrom1 = []
#     for i in words :
#         if str(i) == str(i)[::-1]:
#             polindrom1.append('Да')
#         else:
#             polindrom1.append('Нет')
#     return polindrom1

# print(palindrom(['hello','aa',5,'aba',41]))


# def validate_email(email:str):
#     '''functions for validate email'''
#     domains = ['gmail.com','mail.ru']
#     index = email.find('@')
#     print(index)
#     print(email[index+1 :])
#     if '@' not in email:
#         raise Exception('Invalid Email')
#     elif email[index + 1:] not in domains :
#         raise Exception(f'Invalid email domains {domains}')
#     elif not email[0:index]:
#         raise Exception('Incorrect email')


#     return True


# email = input('Введите email:')
# print(validate_email(email))
