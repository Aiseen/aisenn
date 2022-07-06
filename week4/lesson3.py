# Встроенные функции.Map,filter,lambda

# Функция высшего порядка - это функция, которая может принимать в качестве агрумента другую функцию и/или возвращать
#функцию как результат работы

# print(len('asdasdas'))
# print(len([1,2,3,4,5]))

# list_ = list(range(10))
# # print(list_)

# print(all(i>100 for i in list_))
# print(all(i>=0 for i in list_))
# print(all(1 for i in list_))


# def func(x,y):
#     print(x,y)
# func(4,5)
# print(func(4,5)) # None

# lambda - анонимная функция, которая имеет более короткую запись и чаще всего вызывается один раз

 # lambda arguments: expression - синтаксис


# f = lambda x,y :print(x,y)
# f(4,5)

# f = lambda x,y: x+y
# print(f(4,5))

# f = lambda x,y : x if x > y else y
# print(f(5,4))

# def func(x,y):
#     if x > y :
#         return x
#     else :
#         return y
# print(func(5,4))



######### map - встроенная функция которая нужна для того,чтобы применить какую - либо функцию к каждому элементу в итерируемом обьекте


# map(functions,iter_type) - синтаксис

# list_ =` [1,2,3,4,5] # ['1','2',....]
# def func(x):
#     return str(x)
# result = list(map(func,list_))
# result2 = list(map(lambda x:str(x),list_))
# result3 = list(map(str,list_))
# print(result)
# print(result2)
# print(result3)


# list_ = range(0,10) #[10,11,12,13,14....]
# def func(x):
#     return x + 10
# result1 = list(map(func,list_))
# result2 = list(map(lambda x: x+10,list_))
# print(result1)
# print(result2)



# list_ = [1,2,3,4,5,6] # Нечетное, Четное,


# res1 = list(map(lambda x: 'Четное' if x%2 == 0 else 'Нечетное',list_))
# print(res1)

# def func(x):
#     if x%2 == 0:
#         return 'Четное'
#     else :
#         return 'Нечетное'
# res2 = list(map(func,list_)) 
# print(res2)


# list_ = ['1','2','3','4']

# res1 = list(map(lambda x: list(x),list_))
# print(res1)

# def func(x):
#     return list(x)
# res1 = list(map(list,list_))
# print(res1)

# res3 = list(map(list,list_))
# print(res3)



# filter - функция для фильтрации 

# list_ = [1,2,3,4,5,6,7,8]
# # res1 = list(filter(lambda x: x>3,list_))
# # res2 = list(map(lambda x: x>3,list_))
# # print(res1)
# # print(res2)

# def func(x):
#     return x>3
# res3 = list(filter(f,list_))
# print(res3) # ПОВТОРИТЬ

# list_ = range(0,100)
# # r1  = list(filter(lambda x: x % 2 == 0,list_))
# # print(r1)
# r2 = list(filter(lambda x: x != 0 , list_))
# print(r2)


# str_ = 'hello'

# res1 = list(map(lambda x: 'hello '+ x ,str_))
# print(res1)


# str_ = 'aaaaaaaaaabbbbbbbcccccceeeeee'
# r1 = list(filter(lambda x: x != 'a' and x!= 'e',str_))
# print(r1)


# str_ = 'aaaaaaaaaabbbbbbbcccccceeeeee'
# r1 = set(filter(lambda x: x != 'a' and x!= 'e',str_))
# print(r1)


# list_ = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c']
# s = ''.join(list_)
# print(s)
# # s = s.split()
# print(list(s))


