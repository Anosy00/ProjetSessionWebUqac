from peewee import Model, SqliteDatabase, IntegerField, BooleanField, TextField, FloatField

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Product(BaseModel):
    id = IntegerField(primary_key=True)
    name = TextField()
    description = TextField()
    price = FloatField()
    weight = IntegerField()
    in_stock = BooleanField()
    image = TextField()

class Order(BaseModel):
    id = IntegerField(primary_key=True)
    product_id = IntegerField()
    quantity = IntegerField()
    total_price = FloatField()
    total_price_tax = FloatField()
    shipping_price = FloatField()
    email = TextField(null=True)
    shipping_information = TextField(null=True)
    paid = BooleanField(default=False)

def init_db():
    db.connect()
    db.create_tables([Product, Order], safe=True)
    db.close()