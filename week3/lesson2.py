# l = []
# for i in range(1,11) :
#     l.append(i)
# print(l)

# l = [i for i in range(1,11)] #comprehension - поведение списка,сета,диктионэри.
# print(l)
# print(a)


#list comprehension

# Есть 3 вида comprehensiom:
  # list comprehension
  # set comprehension
  # dictionary comprehension

# l = []
# for i in range(1,11) :
#     l.append(i)

# a  ='Yes' if True else 'No'
# print(a)

# list_ = [i for i in range(1,11)]
# print(list_)

# list_ = [i for i in range(0,11,2)]
# print(list_)  # четные

# list_ = [i for i in range(100)if i % 2 ==0]
# print(list_)

# list_ = ['Четное'  if i %2 == 0  else ' Нечетное'for i in range(100)]

# print(list_)

# import time 
# start_time = time.time() #10:20
# # print(start_time)

# l = []
# for i in range(500):
#     l.append(i)

# time1 = end_time = time.time() #10:30
# print(end_time - start_time)

# start_time2 = time.time()
# list_ = [i for i in range(500)]
# time2 = end_time2 = time.time()
# print(time1/time2)

# 0 1 2 3
# 0 1 4 27

# list_ = [ i**2 if i % 2 == 0 else i**3  for i in range(101)]
# print(list_)

# list_ = [ i **2 if i% 2 == 0 else  i**1  for i in range (101)]
# list2_ = [i**2 for i in range (100) if i%2 == 0]
# print(list_)
# print(list2_)



# matrix = [
# [0,0,0],
# [1,1,1],
# [2,2,2]

# ]
# # 0 0 0 1 1 1 2 2 2

# list_ = [j for i in matrix for j in i ]
# print(list_)

# some_str = 'hello world'
# list_ = [ i for i in some_str if i== 'e' or i == 'o']
# print(list_)
# list_ = [True  if i % 2 == 0 else False for i in range(10)]
# print(list_)
# print(any(list_))
# print(all(list_))

# print(any([False,True])) # True
# print(any([False,False])) # False
# print(any([True,True])) # True

# print(all([False,True])) # False
# print(all([False,False])) # False
# print(all([True,True])) # True


# print(all([1,0,1])) # False
# print(all([1,1,1]))  # True


# l = ['apple','banana','kiwi']
# list_ = [i for i in l if 'a' in i ]
# print(list_) # ['apple','banana']

# list_ = [[j for j in range(i)]  for i in range(10) ] 
# print(list_)
# list_ = max ([i**2 for i in range(5)])
# print(list_)

# list_ = sum([i**2 for i in range(5)])
# print(list_)

# list_ = min([i**2 for i in range(5)])
# print(list_)

#a ->
#1 ->
# list_ = [ord(str(i)) for i in range(10)]
# print(list_)

###### set comprehension
# list_=[1,1,1,0,0,0]
# set_ = {i for i in list_}
# print(set_)

####### dictionary comprehension

# 0 : 0**2
#1 : 1**2
#2 : 2**2

# dict_ = {i: i**2 for i in range (10)}
# print(dict_)

# dict_ = {i: i**2 if i%2 == 0 else i**3 for i in range(10)}
# print(dict_)

# dict_ = {i: 'Четное' if i%2 == 0 else 'Нечетное'  for i  in range (10)}
# print(dict_)



# dict_ = {'c':5,'b':3,'f':2}
# dict_ = {k:'Четное' if v%2 == 0 else 'Нечетное'  for k,v  in dict_.items() }
# print(dict_)

# dict_ = {'a': [10,20], 'b':[30], 'c':[100,1]}
# dict_ = {k: max(v) for k, v in dict_.items()}
# print(dict_)

# a = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# b =  a.split()
# b = [i for i in b if not i.isalpha()]
# print(b)


