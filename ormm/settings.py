import peewee

db = peewee.PostgresqlDatabase(
    'orm',
    user = 'aisen',
    password = '1',
    host = 'localhost',
    port = 5432
)
# print(db.connect())