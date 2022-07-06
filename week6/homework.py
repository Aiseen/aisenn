
# class Class1:
#     def __init__(self,name,last_name,age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#     def aw(self):
#         return f'вау,тебя зовут - {self.name}'

# class Class2(Class1):
#     def siu(self):
#         return f'и у тебя еще фамилия  {self.last_name}'
#     def jok(self):
#         return f'тебе еще и {self.age} лет'    


# a = Class2('Aisen','Sagynbaev',30)
# print(a.aw())
# print(a.siu())
# print(a.jok())


# class A:
#     def method1(self):
#         return 'Основной функционал'

# class B(A):
#     def method1(self):
#         return super().method1()+ ' '+ 'Дополнительный функционал'

# a = B()
# print(a.method1())


# class Polygon:
#     sides = 'many'
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs= kwargs
#         print(self.args)
#         print(self.kwargs)

#     def get_perimetr(self):
#         if self.args:
#          return sum(self.args)
#         elif self.kwargs:
#          return sum(self.kwargs.values())


# class Rectangle(Polygon):
#     sides = 4

#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def get_perimetr(self):
#        return (self.a + self.b)*2











# class Triangle(Polygon):
#     sides = 3

#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def get_perimetr(self):
#         return (self.a + self.b + self.c)

# triangle = Triangle(a=1,b=3,c=5)
# print(triangle.get_perimetr())
# print(triangle.sides)

    
# rectangle = Rectangle(11,22)
# print(rectangle.get_perimetr())
# print(rectangle.sides)


# a = Polygon(a=1,b=22,c=23)
# print(a.get_perimetr())
# print(a.sides)





# class MyDict(dict):
#     def get(self,key,value='siu'):
#         print('Are you kidding me?')
#         return dict.get(self,key,value)

# siu2 = MyDict(a=2,b=3,c=4)
# siu2.get('d')

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         return f'вас зовут - {self.name} ваш возраст - {self.age}'

# class Student(Person):
#     def __init__(self,name,age,facultet):
#         super().__init__(name,age)
#         self.facultet = facultet

#     def display_student(self):
#         return f'вас зовут - {self.name} ваш возраст - {self.age} и вы учитесь в {self.facultet}'


# a = Person('aisen',30)
# print(a.display())
# b = Student('aisen',30,'художка')
# print(b.display_student())



# class aisen:
#     name = 'aisen'
#     _hobby = 'siu'
#     __school = 13

# a = aisen
# print(a.name)
# print(a._hobby)
# print(a._aisen__school)

# class A:
#     def method1():
#         return 'Hello World'

# class B(A):
#     pass
# a = B
# print(a.method1())


# class Car:
#     __speed = 0



#     def   set_speed(self,value):
#         self.__speed = value
    
#     def show_speed(self):
#         return self.__speed

# car = Car() 
# car.set_speed(value=25)
# print(car.show_speed())

# class Car:
#     __speed = 0


#     @property
#     def show_speed(self):
#         return self.__speed



#     @show_speed.setter
#     def set_speed(self,value):
#         self.__speed = value


# car = Car()
# car.speed = 120
# print(car.speed)

# class PriveteProject:
#     github_link = 'some_url'
#     _developers = ['Aiseen','Janaai','Siuuu']
#     def __init__(self,username):
#         self.username = username

#     def check_username(self):
#         if self.username == self._developers:
#             return self.github_link
#         else:
#             return 'Forbidden'    
    

# a = PriveteProject('sasha')
# print(a.check_username())



# class Song:
#     def __init__(self,author,title,year):
#         self.author = author
#         self.title = title
#         self.year = year
    
#     def show_author(self):
#         return f'автор этой песни - {self.author}'
    
#     def show_title(self):
#         return f'название этой песни - {self.title}'

#     def show_year(self):
#         return f'год этой песни - {self.year}'
      
    
# song = Song('Imagine Dragons','Believer',1900)
# print(song.show_author())
# print(song.show_title())
# print(song.show_year())




# class Taxi:
#     def __init__(self,name,posadka,killometr):
#         self.name = name
#         self.pos = posadka
#         self.k = killometr
    
#     def value(self):
#         if self.pos > 20 and self.k > 2:
#             print(200)
#         elif self.pos < 20 and self.k > 4:
#             print(300)
#         else:
#             print('как выйдет')

# taxi = Taxi('yandex',22,3)
# taxi2 = Taxi('Namba',20,2)
# taxi3 = Taxi('Jorgo',15,5)
# taxi.value()
# taxi2.value()
# taxi3.value()

class Car:
    __speed = 0



    @property
    def show_speed(self):
        return self.__speed



    @show_speed.setter
    def set_speed(self,value):
        self.__speed = value


car = Car()
car.speed = 120
print(car.speed)




# class MyDict(dict):
    # def __init__(self,siu,va)


