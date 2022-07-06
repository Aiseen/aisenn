# Тип данныъ: String(строки)

# СТрока - это последовательный набор символо, который может состоять  букв,цифр, знаков, разделителей и тд.
# Строка это неозменяемый, упорядоченный и идексируемый тип данных

#Pep - 8




# name = 'John' 
# last_name = 'Snow'
# full_info = name + " " +  last_name #Конкатенация - сложение строк ('h'+ 'l')
# age = 30
# print(full_info+" " + str(age)) # '30'


#text = "aisensuperduperlohemesaytloh"
# print(len(text))
# print(text*5)


#Индексация начинается с нуля
# hello = 'hello world' #01234

# print(hello[0]) # -> h
# print(hello[2]) # -> l
# print(hello[-1]) # -> d


# срезы(slice)

# test_text = 'hello world'
#  от и до
# print(test_text[0:5]) #hello
# print(test_text[0:1]) # e
# print(test_text[6:11]) #world
# print (test_text[0:5:2]) # [от:до:шаг] -> hlo
# print(test_text[0:5:3]) #hl
# print(test_text[:5])
# print(test_text[0:-2])
# print(test_text[-1:5])
# print(test_text[::-1])
# print(test_text[0:5:])

#экронированные последовательности - это последовательности, которые начинаются с символа '/' за которым следует один или более символов 
# print('Hello\n  World') # Перенос на следующую строку

# print('Heloo\r a') # Возврат каретки
# print('Hello\t world') #табуляция (4 пробела)
# info = '\t это табуляция'
# info2 = r'\t это табуляция' #(из за r нет пробелов)
# info3 = '\\t это табуляция'
# info4 = r' \\t это табуляция' # (Из за  r меняется только одна \)
# print(dir(list))
# print(info4)

# Методы строк
# text = 'SOme text'
# print(dir(text))
# print(dir(str))

# import math
# print(dir(math))

# str_='hello'
# print(str_.isalpha()) #Проверяет состоит ли строка только из букв
# print(str_.isdigit()) #Проверяет состоит ли строка только из цифр
# print(str_.islower()) # Проверяет состоик ли строка только в нижнем регистре (маленькая буква)
# some_text = input('Введите любую строку:')
# print(some_text.islower())

# hello = 'hello world'
# print hello.replace('l','#', 1) # replace (Шаблон,замену[,maxcount])
# print(hello)

# s = input('введите строку:')
# s = s.replace('a','').replace('A','').replace(" ", '')
# print(s)

# str_ = 'hello,world,name,ff'
# str_ = str_.split(',')
# print(str_)
# some_text = 'Hello World my name is Aisen SAgynbaev'
# print(some_text.split('  '))


# hello = 'hello'
# hello = hello.upper()
# print(hello)

# hello = 'hello'
# aidol = hello.lower()
# print(aidol)

# hello = hello.lower()
# print(hello)
# hello = hello.title()
# print(hello)
# s = 'hELLo'
# print(s.tittle()) 

#БЯЗАТЕЛЬНО ПЕРЕУЧИТЬ ВВЕРХНЕЕ



# str_ = 'HEllo i am aisen'
# print(str_.count('a')) #2
# print (str_.count('l')) #2

# s = 'heh'
# print(s.count('h',1))# Начать с первого символа
# print(s.count('h',1,1)) # 0  начни от сюда и закончи там (str,[start],[end])

# some_text = '   h    a s  s s d s f a qr g gq q s s s s  ss s s    '
# print(some_text.strip()) # Удаляет данные в начале и конце
# print(some_text.rstrip())
# print(some_text.lstrip())

# email = 'admin@admin.com'
# print(email.endswith('.com'))
# print(email.startswith('a'))

# str_ = 'hello is hello is s i'
# print(str_.count('is'))

# list_ = str_.split()
# print(type(list_)) # -> list
# print(list_)
# hello = ' '.join(list_)
# print(hello)

# name = input('введите ваше имя:')
# age = int(input ('введите ваш возраст:'))
# email = input('ввдите ваш email:')
# print(f'Здравствуйте, вас зовут -{name}. Вам {age} лет. Вы зашли на {email} почту')

# name = input('введите ваше имя:')
# age = int(input ('введите ваш возраст:'))
# email = input('ввдите ваш email:')


# if email.endswith('.com'):
#  print(f'Здравствуйте, вас зовут -{name}. Вам {age} лет. Вы зашли на {email} почту')
    
# print('hey')

# str_ = 'key world hello'
# str_ = str_.split()
# print(str_)
# str_ = ' '.join(str_)
# print(str_)


# print(ord('a')) # 97 = Уникальное значение
# print(ord('а')) # 1072 = уникальное значение 
# print(ord('1')) # 49 = уникальное значение
# print(chr(49)) #1 
# print(chr(98)) #b

name = 'John'
password = '1'

password2 = int(input('Введите пароль:' ))
if not  password2 == int(password): # == всегда сравнение
    print(name)

    