# import random


# class Character:

#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

#     def __init__(self,name):
#         self.name = name

    
#     def give_weapon(self):
#         weapon_list = ['1','2','3','4','5']
#         return random.choice(weapon_list)

#     def give_role(self):
#         role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         return random.choice(role_list)

#     def get_powers(self,key,value):
#         self.power_list[key]= value
        

# class Elf(Character):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age

#     def get_age(self):
#         return self.age


    
# obj1 = Character('obj1')
# print(obj1.give_weapon())
