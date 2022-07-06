from models import Product,Category

def add_category(name):
    try:
        row = Category(name = name)
        row.save()
        print('Saved!!!!')
    except:
        print('Такая категория уже существует!!')


def add_product(name,price,category):
    category_id = Category.select().where(Category.name == category)


    row = Product(name = name,price = price, category = category_id)
    row.save()


# add_category('Game')
# add_product(name = 'Мяч', price = 10200,category ='Game')



def get_categories():
    categoris = Category.select()
    for i in categoris:
        # print(dir(i))
        print(i.id, end = ' ')
        print(i.name)
# get_categories()


def get_products():
    products = Product.select()
    for i in products:
        print(i.id,end = ' ')
        print(i.name,end = '')
        print(i.price, end = ' ')
        print(i.category.name)

# get_products()

def delete_product(id):
    product = Product.select().where(Product.id == id)
    product[0].delete_instance()

# delete_product(1)


def update_product(id,name):
    product = Product.get(Product.id ==id)
    product.name = name
    product.save()
    print(product)

# update_product(2,'Старое платье22')