# name - input("тебе сколько лет?")






# +, -, *, /, //, %, **
"""
num1= 5
num2 = 5
print(num1+num2) # 10
print(num1-num2) #0
print(num1*num2) #25
print(num1/num2) #1.0
print(num1//num2) #1.0
print(num1%num2)  # 0 остаток от деления
print(num1**num2) #3125 степень
print(-num1) #-5
print(25%7) # 4 осталось от деления
"""







from re import A


x = 1
y = 2
z = 3
# x,y,z = 1,2,3 #множественное присваивание
# print(x)
x,y,z = z,x,y

print(pow(3,2)) # 3  в квадрате , так как там 2
print(pow(3,2,3)) #  (3**2) % 3 , то есть пыталось найти остаток от деления

print(abs(-5)) #5 - модуль числа (неотрицательное число)
print(abs(5))

# Найти число pi в модуле math
# изучить что такое divmod()
# Что делает функция id?


import math
print(math.pi)

print(divmod(4,2))  # 4 делится на два, а дальше 4 % на два
print(divmod(10,5))

name = 'John'
age = 30
print(id(name))
print(id('John'))
print(id(age))

print('hello'*5)

