# Множество (set()) - изменяемый, неупорядоченный и итерируемый тип данных

# {} -  литералы
# set_ = {1,2}
# dict_ = {'a':'hello', 1:2}
# set2 = set()
# print(type(set_))


# set_ = {1,2,3, 'h', 'h', 3,2,1}
# print(set_)
# print(dir(set_))

# set_ = {(1,2,3),(2)} #не может хранить изменяемый тип данныХ,только неизменяемые

# res =[1,1,1,1,1,1,1,1,1,1,1,1,1]

# print(set(res)) 


# Найти факториал введенного числа
# 3! = 1*2*3 = 6

# l = [2,3,10,5]
# res = []
# for i in l : #2
#     f = 1
#     for j in range (1,i+1):
#         f*= j #1 * 1 = 1 * 2 = 2
#     res.append(f)
#     print(f)
# print(res)


# for i in range(5) :
#     if i ==2 :
#         break
#     print(i)
# else : # не сработает если сработал break
#     print('Все')

# for i in range(11) :
#     if i % 2 : # 0 % 2 = 0 , 1 % 2 = 1 --> True
#         print('Четное')
#     else :
#         print('Нечетное')

# for i in range(11) :

#  print('Четное ') if i%2 == 0 else print ('Нечетное') 
    

# text_ = 'aisenvelikiychelovekizvsehvremeninarodovamdkasjdpqpdmlalxqsaakdijfsmjcdkkmc'
# while True :
#      char = input('Введите символ:')
#      print(text_.count(char))
    
# Сложить цифры целого числа 
# 3 = 2
# 22 = 2 + 2  = 4
# 45 = 4 + 5 = 9

# num = 55 #10
# res = 0
# for i in str(num) :
#     print(i)
#     res += int(i)
#     # res = res + int(i) # 2 вариант
# print(res)

# list_ = [55,56,'hello', 'aba', 'c', 'lol']
# for i in list_ :
#     if str(i)  == str(i)[::-1] :
#      print('DA')
# else :
#     print('NET')      # <--- nepravil'no


#  Угадай число


# import random

# num = random.randint(0,10)
# a  = 3
# while True :
#     num2 = int(input('Угадайте число :'))
#     if num2 == num :
#         print(f'Поздравляю, вы угадали {num}!')
#         break
#     else :
#         a = a -1
#         print(f'Попробуй еще раз,{a-1}')
#     if a == 0 :
#         print('Вы проиграли.')
#         break


# import random

# l = []
# for i in range(101):
#     l.append(random.randint(-10,10))
# print(len(set(l)))
# print(len(l)- len(set(l)))

# import os
# os.system('touch test.py')

# for i in range(10) :
#     if i == 9 :
#      continue
#     print(i) 

a = int(input('Введите число'))
for i in range(11) :
   print(i*a)

    
    
