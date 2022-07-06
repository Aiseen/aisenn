# a = 'hello'
# # for i in a :
# #     print(i)


# i = 0
# while i < len(a): # 0<5, 1<5 ..... 5<5
#    print(a[i])
#    i+= 1

# Области видимости и пространства имен

# LEGB
   # L - Local
   # E - Enclosed
   # G - Global
   # B - Built-in

# import this

# x = 'Это глобальная переменная'



# def some_func():
#     x = 'Это замкнутая переменная'
#     def some_func2():
#         x = 'Это локальная переменная'
#     return some_func2
# some_func()
# print(x)




# x = 'Это глобальная переменная'



# def some_func():
#     x = 'Это замкнутая переменная'
#     def some_func2():
#         x = 'Это локальная переменная'
#         print(x)
#     return some_func2()
# some_func()


# x = 10
# def func():
#     print(x)
#     x = 5

# func()
# print(x)



# x = 10 
# y = 15
# def func():
#     x = 5
#     print(locals())
# func()
# print(x)
# # print(globals)

# x = 0
# def counter():
#     global x 
    
#     x += 1
#     print(x)

# counter()
# counter()
# counter()
# counter()
# counter()
# counter()




# x = 0
# def counter():
#     global x 
    
#     x += 1
#     print(x is globals())
#     # print(globals()[x])

# counter()

# x = 0 
# print(x)
# def counter():
#      global x
#      x += 1
#      print(x)
#      def func():
#          global x
#          x+=1
#          print(x)
#      func()

# counter()
# print(x)        



# def f():
#     x = 20
#     def f2():
#         nonlocal x 
#         x = 40
#     f2() 
#     print(x)
#     x += 5
#     print(x)

# f()   


# for i in range(10):
#     pass 
# print(i)

# while 1:
#     i = 10
#     break 
# print(i)

# from math import pi
# print(dir(__builtins__))



# def outer_func():
#     global a
#     a = 20

#     def inner_func():
#         # nonlocal a
#         a = 30
#         print(a)
#     inner_func()
#     print(a)
# a = 10 
# outer_func()
# print(a)

# a = 5
# pass
# def f():
#     a = 10
# f()
# pass
# print(a+10)

