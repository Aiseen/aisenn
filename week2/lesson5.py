# Тип данных - list(списки) + Методы списков

# list - изменяемый, упорядоченный и итерируемый тип данных

# list_ = ['Alex', 'John', 'Sam']
# print(list_[1])

# list_2 = []
# list_3 = list()

# list_4 = [1, True, 'John', [1,2,3, ['Sam']]]
# print(list_4 [1]) #True
# print(list_4[3]) # [1,2,3, ['Sam]]
# print(list_4[3][1]) #2
# print(list_4 [3][3][0]) #Sam
# print (list_4[-1]) # [1,2,3, ['Sam]]
# print (list_4[1:]) # все,начиная с 1
# print(len(list_4))
# print(len(list_))


# list_ = []
# print(dir(list_))
# #list_.append() # как использовать метод 
# list_.append([1,2])
# print(list_)
# list_.append((1,2))
# print(list_)
# list_.append(list([1,2])) 
# print(list_)


# list_1 = [True,1]
# list_2 = [False,0]
# list_1.extend(list_2) # расширяет список
# print(list_1)
# print(list_2)

# list_ = [3,4,5]
# list_.insert(0,2)
# print(list_)
# list_.insert(3, 'hello')
# print(list_)
# print(list_[0]+list_ [1])


# list_ = [1,2,3]
# # list_.remove (2) # удаляет по значению
# # list_.remove(5) #Error
# list_.remove(1)
# print(list_)

# list_ = [True,2,3, 'Hello']
# list_.pop() 
# list_.pop(0) # удаляет по индексу
# list_.pop(6) # Error
# print(list_)

# removed = list_.remove(True)
# print(list_)
# removed2 = list_.pop(2)
# print(removed2)

# list_ = [True,False, 1,2,3, True]
# print(list_.index(True)) # 0
# list_2 = ['hello','john','s','w','s']
# print(list_2.index('s')) #2
# print(list_2.index('s',3)) #4

# list_=[1,2,3,4]
# list_.reverse()
# print(list_)

# list_ = [1,3,4,10,2]
# list_.sort()
# print(list_)

# list_2 = [1,2,'3']
# list_2.sort()
# print(list_2)    # ошибка,тк там str и  int

# list_ = ['a','b','aa','ab']
# list_.sort()
#list_.sort(reverse=True) # по убыванию 
# print(list_)
# list_ = ['a','b','a','hello']
# print(list_.count('a')) #2
# print(list_.count('hello')) #1
# print(list_.count('h')) #0

# list_ = [1,2,3,4]
# print(sum(list_)) #10
# print(max(list_)) #4
# print(min(list_)) #1

# list_ = ['a','b','aa','ab']
# print(max(list_)) #b
# print(min(list_)) #a  по порядковому номеру

# l1 = [1,2,3,4]
# # print(id(l1))
# # l2=l1
# # print(l1)
# # print(l2)
# # l2.pop()
# # print(l1)
# # print(l2)

# l1 = [1,2,3,4, ['hello','hello2']]
# l2 = l1.copy() # поверхностное копирование
# l2[4][0] = 'John'
# print(id(l2[4]))
# print(id(l1[4]))
# print(l1)
# print(l2)

# import copy
# l1 = [1,2,3,4, ['hello','hello2']]
# l2 = copy.deepcopy(l1) #глубокое копирование
#l2.clear()

# l = ['a','b','c']
# s = ''.join(l)
# print(s)

# names = (input('Вводи данные через пробел:')).split()
# print(names)
# print(type(names))
# if 'John' in names :
#     print('Welcome John')

# a = 2
# a += 2 # a = a + 2
# x,y,z = 1,2,3

# num1 = 5
# num2 = 6
# res = 'Больше ' if num1>num2 else 'Меньше'
# print(res)