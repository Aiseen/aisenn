#Введение в ООП

#  ООП - Обьектно - ориентированное программирование - парадигма (набор правил написания) программирования
# в котором все основывается на 2 ключевых понятиях: класс и обьект

# Класс - Дает общую характеристику которую будут использовать их обьекты
# Обьект - экземпляр класса

# class GetInfo:  #класс       #можем  GetInfo()
#     name = 'John' #Атрибут класса
    
#     def get_name(self,age): #метод 
#         print(f'Привет,тебя зовут - {self.name},тебе  {age} лет')



# obj1 = GetInfo()
# obj1.name = 'Nick'
# obj2 = GetInfo()
# print(obj1)
# print(obj1.name)
# print(obj2.name)

# print(dir(obj1))



# obj1.get_name(18)
# obj2.get_name(30)


# len('adadadadad')  #  функция (обычно без точки)
# list.append() # метод (обычно с точкой)



# class Animal():
#     def __init__(self,name,animal_type):
#         self.name = name #Атрибут экземпляра класса
#         self.animal_type = animal_type


    # def get_info(self):
    #     return f'Имя обеьекта- {self.name} и тип -
    #      {self.animal_type}'
# # выяснить, почему там ошибка (сверху)



        

# cat = Animal('Barsik','cat')
# print(cat.name)
# print(cat.animal_type)
# dog  = Animal('Reks','dog')
# print(dog.name)





# print(cat.get_info())
# print(dog.get_info())


# class person():

#     isalive = True
    

#     def __init__ (self,name,lastname,age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age

#     def get_info(self):
#         return f'{self.name},{self.lastname},{self.isalive}'

#     def birthday(self):
#         past_age = self.age
#         self.age += 1
#         print('c днем рождения')
#         print(f'Тебе было {past_age} и стало {self.age}')
    
# siu = person('John','Smith',30)
# print(siu.get_info())
# siu.birthday()
# siu.birthday()

# class Bank:
#     total = 0

#     def get_summ(self):
#         print(self.total)

#     def add_sum(self,dob):
#         self.total += dob
#         self.get_summ()

#     def min_sum(self,minimum):
#         # if self.total - minimum < 0:
#         #     raise Exception ('Недостаточно средств!')
#         self.total -= minimum
#         self.get_summ()



# client1 = Bank()
# client1.get_summ()
# client1.add_sum(100)
# # client1.get_summ()
# client1.min_sum(1000)
# # client1.get_summ()


# class song():
#     def __init__(self,show_author,show_year,show_tittle):
#         self.show_author = show_author
#         self.show_year = show_year
#         self.show_tittle = show_tittle


#     def get_info(self):
#         return f'Эта песня вышла в - {self.show_year}, авторами были {self.show_author},а название - {self.show_tittle}'

# siu = song('Imagine Dragons',2018,'Believer')
# print(siu.get_info())


# class song():
#     def __init__(self,show_author,show_year,show_tittle):
#         self.show_author = show_author
#         self.show_year = show_year
#         self.show_tittle = show_tittle


#     def year(self):
#         return f'Эта песня вышла в - {self.show_year}'

#     def author(self):
#         return f'Авторы этой песни группа - {self.show_author}'

#     def tittle(self):
#         return f'Название этой песни - {self.show_tittle}'

# siu = song('Imagine Dragons',2018,'Believer')
# print(siu.year())
# print(siu.author())
# print(siu.tittle())






# from math import pi

# class Circle():

#     color = 'blue'
#     math = pi
    
#     def __init__(self,r):
#         self.r = r
#         r = 4
        
    
     
# class BankAccount():
#     balance = 0

#     def add(self):
#         print(self.balance)

#     def withdraw(self,amount):
#         self.balance -= amount
#         self.add()

#     def deposit(self,amount):
#         self.balance += amount
#         self.add()
    
# a = BankAccount()
# a.add()
# a.withdraw(100)
# a.add()
# a.deposit(100)
# a.add()



# class PhoneBook():
#     def __init__(self,name,lastname,number):
#         self.name = name
#         self.lastname = lastname
#         self.number = number
    
#     def get_info(self):
#         return f'КОнтакт:  {self.name} {self.lastname}, телефон - {self.number}'

# a = PhoneBook('aisen','sagynbaev','9994123123')
# print(a.get_info())


# class Taxi():
#   company_name = 'Yandex'
#   posadka = 30
#   kilom = 10
#   def method(self):
#       if self.posadka > 20 and self.kilom > 5 :
#           print(150)
      
        


# a = Taxi()
# print(a.method())



# class Taxi():
#   company_name = 'Namba'
#   posadka = 30
#   kilom = 10
#   def method(self):
#       if self.posadka > 20 and self.kilom > 5 :
#           print(100)
      
        


# a = Taxi()
# print(a.method())
    


# class Taxi():
#   company_name = 'Jorgo'
#   posadka = 40
#   kilom = 25
#   def method(self):
#       if self.posadka > 20 and self.kilom > 5 :
#           print(200)
      
        


# a = Taxi()
# print(a.method1())
    


class Password():
    def __init__(self,password):
        self.passwod = password

    def  __str__(self):
        return (len(self.passwod) * '*')  

    def validate(self):
        list_ = ['@', '#','$']
        if  not len(self.passwod)>= 8 and not len(self.passwod)<= 15:
            raise Exception('Пароль неправильной длины')
        elif self.passwod.isalpha():
            raise Exception('Добавьте цифры')

        elif self.passwod.isdigit():
            raise Exception('Добавьте буквы')

        elif not any([i in list_ for i in self.passwod]):
            raise Exception('You must added some symbol')

        else:
            return 'Все хорошо!' 




    
password1 = Password('aisen#')
print(password1)
print(password1.validate())

    