# Словари(dictionary) + Методы словарей
# Изменяемый, итерируемый (циклом пройтись можно),упорядоченный тип данных
# # литералы - {}

# синтаксиc - {key:value,key2:value2}

# dict_ = {}
# print(type(dict_))

# dict_ = {'name':'John', 
#  'age': 30,
#  'id' : 1}

# # Ключи должны быть уникальными и неизменяемыми
# print(dict_['age'])
# print(dict_['name'])

# dict_ = dict(name = 'John', age = 20, id = 20)
# print(dict_)

# print(dir({}))

# dict_ = {
#     'name': 'John'
     
# }
# import copy
# # dict_2 = dict_
# # dict_2 = dict_.copy()
# dict2 = copy.deepcopy(dict_)
# print(dict_)

# list_ = ['John','SAm','Steve']
# dict_ = {}
# dict_2 = {}
# dict_ = dict_.fromkeys(list_,True)
# dict_2 = dict_2.fromkeys('hello')
# print(dict_)
# print(dict_2)

# dict_ = {
#     'name':'John',
#      'hobby': ['finish','football']}
# print(dict_['id']) # Error
# print(dict_.get('id', 'Нет такого ключа'))
# print(dict_['name'])

# dict_.pop('name')
# print(dict_)

# dict_['age'] = 30
# removed = dict_.pop('age')
# print(dict_)
# print(removed)
# # dict_.pop('name') #Keyerror
# removed = dict_.pop('name', 'Нет такого ключа')
# print(removed)

# dict_ = {
#     'name':'John',
#      'hobby': ['finish','football']
#      }

# r = dict_.popitem()
# print(r)
# print(dict_)

# dict_ = {
# 'name' : 'John'

# }
# dict_.setdefault('age','30') # создает значение по умолчанию пустое
# print(dict_)

dict_ = {
'name' : 'JOhn',
'age' : 30,
'status' : True,
'hobby': 'fishing'

}
# print(dict_)
# print(dict_.values())
# print(dict_.keys())
# print(dict_.items())

# for i in dict_.keys(): # keys() по умолчанию
#     print(i)

# for i in dict_.values() :
#     print(i)

# for i in dict_.items() :
#      print(i)
#      print(i[1])
#      break

# for i, j in dict_.items():
#     print(f'key - {i}, value - {j}')


# d1 = {
# 'name': 'John',
# 'age' : 30

# }
# d2 = {
# 'name' : 'Sam',
# 'id' : 1

# }
# d1.update(d2)
# print(d1)


# admin = {
#  'id' : 1,
#  'name' : 'John',
#  'password' : 'admin123'

# }
# name = None
# password = None
# count_ = 3
# while admin['name'] != name :
#     name = input('Введите ваше имя!')
# print(f'Привет {admin["name"]}. Скажи кодовый пароль, у тебя 3 попытки!')

# while admin ['password'] != password :
#     if count_ == 0:
#         break
#     password = input(f'У тебя  осталось {count_} попыток')
#     count_ -= 1

