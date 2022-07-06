# list_ = ['aisen','roman','talgat','alibek','misha']
# print(list_[0])
# print(list_[1])
# print(list_[2])
# print(list_[3])
# print(list_[4])





# a = [1,2,4,6,11,55]
# b = [11,44,11,44,55667]
# print(sum(a+b))

# a = 2000
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
#     print('Yes')
# else :
#     print('NO')

# dict_ = {'age': 13, 
# 'number' : 7,
# 'name' : 'xz'
# }

# print(dict_.pop('age' ))
# print(dict_.pop('number'))
# print(dict_.pop('name'))
# print(dict_)



# a = dict(aisen=495,fas=167,terrible='ios')
# print(a['aisen'])

# b = dict.fromkeys(['a','b','c','d'],100)
# print(b)

# dict_ = {'siu' : 'mine', 'age': 30,'name':'aisen'}
# for i in dict_ :
#     print(i)



# dict_ = {'siu' : 'mine', 'age': 30,'name':'aisen'}
# dict2_ = {}
# import copy



# dict_ ==  dict2_
# dict2_ = dict_.copy()
# dict_ = copy.deepcopy(dict2_)
# print(dict2_)
# print(dict_)



# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list2 = [i for i in int_list if i > 0]
# print(int_list2)

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# str_list = [i for i in range (1,11)]
# print(str_list)

# list_ = [i**2 if i%2 == 0 else i**1 for i in range(1,11)]
# print(list_)

# list_ = [True if i%2 == 0 else False for i in range(1,10)]
# print(list_)

# list_ = ['aisen','talgat','roman','alibek','akimbo','ayan','kim','tema','dariya','ayana']
# list_ =  ['Shorter' if len(i)<4 else 'longer' for i in list_]
# print(list_)

# a = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# b =  a.split()
# b = [i for i in b if not i.isalpha()]
# print(b)

# a = { 1 : 'first',
# 2 : 'second',
# 3 : 'third',
# 4 : 'fourth'

# }
# a = {k: len(v) if k%2 == 0 else len(v)**3 for k,v in a.items() }

# print(a)

# dict_ = {1:'',
# 2: '' ,
# 3: '',
# 4: '',
# 5: '',
# 6: '',
# 7: '',
# 8: '',
# 9: '',
# 10: ''


# }


# dict_ = {k: int(k)**2 for k,v in dict_.items()}
# print(dict_)


# a = {'a': 1, 
# 'b': 3,
#  'c': 2,
# 'd': 4}

# try:
#  b = 10
#  c = 11
#  print(a)
# except  Exception :
#     print('не указан a ')


# try :
#  a = int(input('Введите первое  число :'))
#  b = int(input('Введите второе   число:'))
#  print(b/a)
# except ValueError :
#     print('Это не число') 
# except ZeroDivisionError :
#     print('На ноль делить нельзя')

# try:
#  a = int(input('Введите число:'))
#  b = int(input('Введите второе число:'))
#  print(a+b)

# except  Exception:
#     print('Это не число')

# try:
#  dict_ = {'first': 1,
# 'second':2,
# 'third':3 ,
# 'fourth' : 4
# }
#  print(dict_['fifth'])
# except  KeyError:
#     print('Такого ключа нет')




# list_ = ['aisen','makers','funny',1]
# try:
#     print(list_[4])
# except Exception :
#     print('Такого элемента нет')


# try:

#  a = int(input('Введите сумму на вашем кошельке :'))
#  if a<0 :
#     raise Exception



# except Exception :
#     print('Сумма не может быть отрицательной')








# try:
#  age = int(input('Введите ваш возраст:'))
#  if age>=18 :
#      raise Exception 

#  else :
#   print('Доступ запрещен')   


# except  ValueError :
#     print('Введен некорректный возраст')


# except Exception :
#     print('спасибо!')

# finally :
#     print('До свидания!')



# try:
#     a = int(input('Введите первое число:'))
#     b = int(input('Введите второе число:'))
#     print(a/b)
# except  ValueError :
#     print('Вы ввели не число')
# except ZeroDivisionError :
#     print('На ноль делить нельзя')

    

# def siu(x,y):
#     return x+y
# print(siu(1,15))


# def siu(x,y):
#     print(type(x))
#     print(type(y))
# siu('makers',111)

# def siu(num1,num2):
#     print(num1/num2)
# siu(11,4)

# ``def siu(num1,num2,num3,num4,num5,num6):
#     print(num1*num2*num3*num4*num5*num6)
# siu(11,22,1,3,5,1)``







