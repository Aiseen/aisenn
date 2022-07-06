# CRUD интернет магазина на функциях. Работа с JSON
    #C - create
    #R - read 
    #U - update
    #D - delete

# JSON(JaavaScript Object Notation) - простой формат
#обмена данными.



# import json


# data = {'name':'John',
# 'age': 30,
# 'last_name': None,
# 'is_admin': False
# }

# json_obj = json.dumps(data) #Сериализация (переводим данные в json)
# print(json_obj)

# python_obj = json.loads(json_obj) # Десериализация (переводим с json в python)
# print(python_obj)



########
# 
#PYTHON           JSON 
#tuple            array
#str               String
#int                number
#dict                object
#list                array
#float              number
#True , False     true/false
#None              null



# import json

# with open('test.json') as file:
#     # print(file.read())
#     print(file)
#     print(json.dumps(file.read()))

# import json

# data = {'is_admin': True}
# print(json.dumps(data))

# with open('test.json') as file: 
#  print(json.load(file))


#разница между load и loads, а также между dump и dumps в том,что load/dump - 
# принимают сам файл,  dumps/loads -  принимают строку



