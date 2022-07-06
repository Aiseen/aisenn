#  Основные принципы ООП :  Наследование


# class A:
#     a = 5
#     def get_a(self):
#         print(self.a)

# class B(A):
#     pass






# obj_a = A()
# print(obj_a.a)
# obj_b = B()
# print(obj_b.a)
# obj_b.get_a()


# class Person :
#     def __init__(self,name,last_name,age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def __str__(self):
#         return self.name

#     def display_name(self):
#         print(f'Name : {self.name}')


# class Employee(Person):
#     def __init__(self,name,last_name,pol,age):
#         Person().__init__(self,name,last_name,pol)
#         self.age = age

#     def work(self):
#         print('Я работаю')

# # person = Person('John')
# # print(person)
# employee = Employee('John2','Snow','M',6)
# print(employee)


#Super - вместо родительского (Person).Это тот класс,котоырй был передан первый
# Если мы обращаемся к Person вместо Super,то должны добавить self


# class A:
#     a = 5


#     def info(self):
#         print('Hello')


# class B(A):
#     # a = 3
#     # a = A().a +2


#     def info(self):
#         res = super().info()
#         print(res*2)
#         print('Hello2') 

# a = A()
# b = B()
# # print(a.a)
# # print(b.a)
# a.info()
# b.info()


# # print(B().)


# class A:
#     def info(self):
#         return 'hello'

# class B(A):
#     def info(self):
#         return  super().info() +'world'

# obj1 = A()
# obj2 = B()
# print(obj1.info())
# print(obj2.info())

# часто используем super чтобы не поломать логику

# class MyStr(str):
#     def upper(self):
#         return super().upper() + 'Нет такого метода!'

# some_str = MyStr('asadloh ') #some_str = 'asasssaas
# # print(dir(MyStr))
# print(some_str.upper())




# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass



# a = A()
# b = B()
# c = C()

# проверяет является ли экземпляром   isinstance
# print(isinstance(a,A)) #true
# print(isinstance(b,A)) #true
# print(isinstance(c,A)) #true
# print(isinstance(a,B)) #false
# print(isinstance(b,B)) #true
# print(isinstance('assasaas',str)) #True
# print(isinstance(2,str)) #False


# print(issubclass(A,B))
# print(issubclass(B,A))
# print(issubclass(str,A))
# print(issubclass(C,A))

# class Person :


#     def  __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return self.name
        
# class Employee (Person):   
#     def __init__(self,name,company):
#         super().__init__(name)
#         self.company = company

#     def __str__(self):
#         return super().__str__() + ' ' + self.company  
        



# obj1 = Person('John') 
# print(obj1)

# obj2 = Employee('Nick','Data0x')
# print(obj2)
