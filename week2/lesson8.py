#list_ - список
#arrays -  массив

#   динамическая типизация  

# name = 'John'
# name = 12
# print(name)
# str name #динамическая типизация   = 'John'
# name = 12

# some_list = [1,2,3,'hello','world']
# print(some_list)
# int some_list = [1,2,3,4,5,6,] #только целые числа

# print(dir([]))

# # изменяемый, mutable

# str_ = '{} world'
# print(str_.format('Hello'))

# str_ = 'hello'
# str_[0] = 't'


#12 - неизменяемый
from doctest import OutputChecker
from pickletools import long1


# int
# float
# str
# complex
# tuple
# frozenset
# long
# bool


# list
# dict
# set


# {
#     'key':'value'
# }


# print(dir([]))

# ls = ['audi']
# print('Before:', ls)
# ls.append('toyota')
# print('after: ',ls)

#FIFO - first in First Out
#LIFO - Last in FIrst Out


# ls = ['audi','toyota','Mercedes','Bmw']
# print('Before:', ls)
# removed = ls.pop(0)
# print(removed)
# print('after: ',ls)

# password,password_comfirmation
# # ==

# ls = ['audi','bmw','mercedes','honda','audi']
# ls.remove('audi',)
# print(ls)


# phone_numbers = [999,777,888,666,333,222,999,666,777]
# unique_phone_numbers = []
# for i in phone_numbers :
#     if i not in unique_phone_numbers :
#         unique_phone_numbers.append(i)
#     else:
#         continue

# print('original:', phone_numbers)
# print('unique:', unique_phone_numbers)

# phone_numbers = [999,777,888,666,333,222,999,666,777]
# phone_numbers.insert(0,110)
# print(phone_numbers)

# new = [1,2,3]
# new.extend([4,5,6])
# print(new)

# strings = ['hello','world','for','if','case','switch']
# strings.sort(key=len)

# print(strings)

# сортировка по длине строк (сверху)

# ls_original = ['john','raychel','peter','jessica']
# cp_ls = ls_original.copy()
# cp_ls[0] = 'Arnold'
# print(cp_ls)
# print(ls_original)


# ls_original = ['john','raychel','peter','jessica',['test','test2']]
# cp_ls = ls_original.copy()
# cp_ls[4][0] = 'Arnold'
# print(cp_ls)
# print(ls_original)

# import string
# import random

# password = ''
# for i in range(2):
#     password += random.choice(string.ascii_uppercase)

# password += random.choice(string.digits)
# password += random.choice(string.punctuation)
# ls = list(password)
# print(ls)
# print(string.ascii_uppercase)
# повторить join