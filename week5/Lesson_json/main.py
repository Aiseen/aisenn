from views import *


print("Привет, тебе доступны следующие функции:\n\tPOST\n\tGET\n\tDELETE\n\tPUT\n\tDETAIL")

while True:
    operation = input('Введите действие:')
    if operation == 'GET':
        print(get_data())
    elif operation == 'DETAIL':
        print(get_one_data())
    elif operation == 'POST':
        print(post_data())
    elif operation == 'PUT':
        print(update_data())
    elif operation == 'DELETE':
        print(delete_data())
    else:
        print('НЕТ ТАКОГО ДЕЙСТВИЯ!!!!!')