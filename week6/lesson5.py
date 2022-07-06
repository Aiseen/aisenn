
# class Employee:
#     count_employee = 0 
#     salary = 500
#     def __init__(self,name,surname,pay):
#         self.name = name #John
#         self.surname = surname #Snow
#         self.pay = pay 
#         self.email = (name + surname + '@gmail.com').lower()
#         Employee.count_employee += 1 

#     def fullname(self):
#         print(self.name + self.surname)
#         return 'ffffffff'
    
# obj1 = Employee('John','Snow',500)
# obj2 = Employee('John2','Snow2',300)
# obj1.fullname()
# # print(obj1.fullname()) выводит return
# print(obj1.email)
# print(obj1.count_employee)


'''
Создайте класс User. В этом классе есть защищенный метод _create_user, который принимает email и password.
 Этот метод вызывается в публичных методах create_user и create_superuser. Оба метода отличаются друг от друга тем,
что в методе create_user атрибут is_superuser имеет значение False, а в методе create_superuser - True.
Также в классе есть метод admin_login, который принимает password.
Создайте два объекта от класса User. К первому объекту примените метод create_superuser, а ко второму - create_user.
Далее у обоих объектов вызовите метод admin_login, передав правильные пароли.
У первого объекта должно выдаваться сообщение Successfully logged in, а у второго - Forbidden, так как поле is_superuser у второго объекта имеет значение False. 
Также если даже is_superuser у первого объекта True, ему не удасться залогиниться, если он передал неправильный пароль password в метод admin_login и ему выдается сообщение: Invalid password.
'''


# class User:
#     def _create_user(self,email,password):
#         self.email = email
#         self.password = password

#     def create_user(self,email,password):
#         self.is_superuser = False
#         self._create_user(email,password)

#     def create_superuser(self,email,password):
#         self.is_superuser = True
#         self._create_user(email,password)
    
#     def admin_login(self,password):
#         if self.is_superuser and self.password == password:
#             print('Succesfully logged in')
#         elif self.is_superuser == False:
#             print('Forbidden')
#         else:
#             print('Invalid password')    


# user1 = User()
# user2 = User()

# user1.create_superuser('user1@gmail.com','user1')
# user2.create_user('user2@gmail.com','user12')

# user1.admin_login('user1')
# user2.admin_login('user2')






'''
Пользователи Создайте класс с именем User. Создайте два атрибута first_name и last_ name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя. 
Напишите метод describe_user(), который выводит сводку с информацией о пользователе. Создайте еще один метод greet_user() для вывода 
персонального приветствия для пользователя. Напишите класс с именем Admin, наследующий от класса User из. Добавьте атрибут privileges дл
я хранения списка строк вида «разрешено добавлять сообщения», «разрешено удалять пользователей», «разрешено банить пользователей» и т. д . 
Напишите метод show_privileges() для вывода набора привилегий администратора. Создайте экземпляр Admin и вызовите все методы.
'''
# class User:
#     def __init__(self,first_name,last_name,age):
#         self.name = first_name 
#         self.surname = last_name
#         self.age = age

#     def describe_user(self):
#         print(f'{self.name} {self.surname} {self.age}')

#     def greet_user(self):
#         print(f'Your welcome, {self.name}')

# class Admin(User):
#     priveliges = ['разрешено добавлять сообщения», «разрешено удалять пользователей», «разрешено банить пользователей'] #

#     def show_priveliges(self):
#         print(self.priveliges)


# admin = Admin('John','Snow',20)
# admin.describe_user()
# admin.show_priveliges()
# admin.greet_user()



# ИЗУЧИТЬ
# Что такое Ассоциация: композиция и агрегация 

# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         result = 0
#         for i in operations:
#             if i == '--X' or i == 'X--':
#                 result -= 1
#             else:
#                 result += 1
#         return result




'''
Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count,
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта
'''

# class A:
#     vowels = list('eyuioa') # Так быстрее
    
    
#     def __init__(self,word):
#         self.word = word


#     def count(self):
#         counter = 0


#         for a in self.word: 
#             if a in self.vowels:
#                 counter += 1

#         return counter           




# class B(A):
        
#     def count(self):
#         counter = 0


#         for a in self.word: 
#             if not a  in self.vowels:
#                 counter += 1

#         return counter 

# a = A('maekrs')
# b = B('maekrs')
# print(a.count())
# print(b.count())



class BaseLift:

    __floor = 1


    def __init__(self,max_floor,min_floor = 1):
        self.max_floor = max_floor
        self.min_floor = min_floor


    @property
    def _floor(self):
        return self.__floor

    @_floor.setter
    def _floor(self,to_floor):
        self.__floor = to_floor


class Lift(BaseLift):
    def show_floor(self):
        print(f'You are on the floor {self._floor}')

    def up(self):
        if self._floor == self.max_floor:
            print('You can\'t go up, you are on the highest floor')
        else:
            self._floor += 1
            self.show_floor
    
    def down(self):
        if self._floor == self.max_floor:
            print('u cant gp down,you are on the lowest floor')
        
        else:
            self._floor -= 1
            self.show_floor

    def go_to(self,to_floor):
        pass #докончить

lift = Lift(15)


lift.up()
lift.up()
lift.down()
lift.down()
lift.show_floor()




