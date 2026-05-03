from fastapi import Depends, FastAPI
from models import ProductSchema
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/") #decorators used with get because we are reading the data
def geet():
    return "Welcome to Aditya's server"  #we have to written it rather than printing


products = [
    ProductSchema(id=1, name="phone", description="budget phone", price=9900, quantity=23),
    ProductSchema(id=2, name="laptop", description="gaming laptop", price=75000, quantity=10),
    ProductSchema(id=3, name="headphones", description="wireless headphones", price=4500, quantity=50),
    ProductSchema(id=4 , name="smartwatch", description="fitness smartwatch", price=12999, quantity=30),
    ProductSchema(id=5, name="tablet", description="10-inch tablet", price=24999, quantity=18),
    ProductSchema(id=6, name="camera", description="digital SLR camera", price=55999, quantity=8),
    ProductSchema(id=7, name="speaker", description="Bluetooth speaker", price=3499, quantity=60),
    ProductSchema(id=8, name="router", description="Wi-Fi 6 router", price=8999, quantity=22),
    ProductSchema(id=9, name="monitor", description="27-inch LED monitor", price=18999, quantity=15),
    ProductSchema(id=10, name="keyboard", description="mechanical keyboard", price=4999, quantity=40),
    ProductSchema(id=11, name="mouse", description="wireless ergonomic mouse", price=2299, quantity=55),
    ProductSchema(id=12, name="charger", description="fast charging adapter", price=1199, quantity=100),
    ProductSchema(id=13, name="powerbank", description="20000mAh power bank", price=2599, quantity=35),
    ProductSchema(id=14, name="webcam", description="HD webcam", price=6999, quantity=25)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count

    if count ==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump())) #converting the pydentic model data in this alchemy
        db.commit()    

'''
product.model_dump() convers the pydatic objects into dictionary

example;   
Product(id=1, name="phone")  
↓  
{"id":1, "name":"phone"}
'''

'''
database_models.Product(**...)  → Converts dictionary → SQLAlchemy object
dict → DB model (table-compatible object)


db.add(...) → Tells SQLAlchemy:
Store this object in database (but not yet saved)
'''

init_db()

@app.get("/products")   #all functions are async by default
def get_all_products(db: Session = Depends(get_db)): #we injected dependencies here 
    
    db_products = db.query(database_models.Product).all()

    return db_products   #still this is not doing the data validation





#fetch one product
@app.get("/product/{id}") #we made it dynamic because here {id} is directly mapped with the product number 
def get_products_by_id(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
        
    return "Product not found"







#add data in the products
@app.post("/product")
def add_product(product : ProductSchema, db: Session = Depends(get_db)):  #Product = object (Pydantic model)
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product






#put
'''
Here you are performing multiple steps:
fetch the database --> check for the value --> put it there
'''
@app.put("/product")
def update_product(id:int, product:ProductSchema, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
    else:
        return "Error: Product can't get updated"





#delete
@app.delete("/product")
def delete_product(id:int, db: Session = Depends(get_db)):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i] 
            return "Product Deleted"
        
    return "Product not delected"