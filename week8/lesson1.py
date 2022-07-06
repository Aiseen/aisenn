#Введение в PoSTgreSQL
# БД - организованная структура предназначенная для хранения, изменения и обработки вз
# аимосвязанной информации.(преимузественно больших обьемов)  (Храним даннын)

'''
СУБД - система управления базами данных  - комплекс программно-языковых средств, позволяющих
создавать БД и управлять данными
(в кратче,вытаскиваем и делаем что нибудь с данными)

СУБД - MySQL, MSSQL

PostgreSQL, (Postgress) - CУБД, которая представляет собой реализацию языка запросов SQL.

SQL - structure query language - язык запросов который используется в качестве способа
сохранения данных,поиска из частей, осуществляь CRUD записей в БД.

Реляционная БД -набор данных с предопределенными связями между ними

'''

#postgres - учетная запись по умолчанию

# sudo -i -u postgres #переход к учетной записи по умолчанию (psql postgres  на mac)

#psql - доступ к командной строке Postgres в Linux

# \q - выход из postgres


#КОМАНДА - последовательность компоненто заканчивающиеся на ;

# СREATE ROLE user_name WITH PASSWORD '1' - команда для создания юзера с паролем

#  ALTER ROLE username with superuser createrole createdb ; - Даем права юзеру

# GRANT ALL PRIVILEGES ON DATABASE test_user to test_user ; - теперь БД будут создаваться от этого юзера

# ALTER ROLE test_user with password 'new_password' ; - если забыл пароль(если надо изменять)

# \du (database users) - лист пользователей БД

# \l - list(лист БД)

# CREATE DATABASE db_name; - команда для создания БД
# \c db_name - подклбчение к БД
# CREATE TABLE Animal(); - создание пустой таблицы
# \d animal(table_name) - просмотреть информацию об этой таблице
# \dt (database tables) - таблицы внутри БД
# drop table animal (table_name); - удаление таблицы

# Типы данных в Postgres:

#1. Числа
# целые
# smallint -32768 до +32768 -2 байта (если введете больше,то будет ошибка)
# int    -2147483648 до + 2147483648 -4 байта
# bigint  -9223372036854775808 до 9223372036854775808 -8 байт

# serial #целые числа с автоинкрементом

#smallserial - 1 до 32768 - (2 байта)
#serial - 1 до 2147483648 (4 байта)
# bigserial - 1 до 9223372036854775808 (8 байт)

# дробные

# real  точность до 6 знаков(4 байта)
# double precision  точность до 15 знаков - (8 байт)

#NUMERIC -  хранит числа с фиксированной точностью, которые могут иметь до 131072 знаков в целой части 
# и до 16383 знаков после запятой.

#DECIMAL -  хранит числа с фиксированной точностью, которые могут иметь до 131072 знаков в целой части 
# и до 16383 знаков после запятой.

#MONEY - денежный тип -  хранит числа с фиксированной точностью, которые могут иметь до 131072 знаков в целой части 
# и до 16383 знаков после запятой, то же самое что и numeric 

# 2.Текстовые
# CHAR(n) - cтрока с постоянной длиной - CHAR(10) -> 
# test -> ошибка

#VARCHAR(n) - строка с максимальной длинной - VARCHAR(10) -> test
# -> 'test'(будет занимать меньше памяти)

# TEXT - строка неограниченной длины 

# 3. Дата и время
# DATE - дата - представляет дату от 4713 г. до н.э до 5874897 г н.э (4 байта)
# TIME -  время - хранит время точностью до 1 микросекунды.(Принимает значение от 00:00:00 до 24:00:00) - занимает 8 байт
# TIMESSTAMP - дата и время


# 4. Boolean -> true/false ; '1'/'0', 't'/'f', 'yes'/'no', 'on'/'off',TRUE/FALSE

# =======================================================
# Cоздать таблицу с полями name,last_name, age 

#CREATE TABLE table_name(
# name varchar(50), last_name varchar(100),age int);

#Добавили записи в таблицу
# INSERT INTO table_name (name,last_name,age) VALUES ('John','Snow',35);

#===========================================
#(constraint) -  ограничения 

# UNIQUE - все значенияв столбце должны быть уникальными(не должны повторяться)
# DEFAULT - у столбца будет значение по умолчанию
# NULL | NOT NULL - определяет будет ли столбец обязательным для заполнения
#CHECK - проверяет значение столбца на определенное условие
#PRIMARY KEY - определяет,будет ли столбец идентификатором записи. (Первичный ключ гарантирует,что нет двух записей с 
# одинаковым значенем ключа)
# FOREIGN KEY - задается ссылка на другую таблицу.

#Создание таблицы с ограничениями 

# CREATE TABLE person(
# id salary primary key # при каждой новой записи id += 1
# name varchar(50) not null #обязательно к заполнению
#  last_name text null, #необязательно к заполнению
# age int check (age > 2), #проверка значения возраста 
# salary money default 15000 #необязательное поле, если не заполнено ставится дефолтное значение, если заполена, то перезаписывается
#         )

