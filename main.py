from fastapi import FastAPI
from models import Product


app = FastAPI()

@app.get("/") #decorators used with get because we are reading the data
def geet():
    return "Welcome to Aditya's server"  #we have to written it rather than printing


products = [
    Product(id=1, name="phone", description="budget phone", price=9900, quantity=23),
    Product(id=2, name="laptop", description="gaming laptop", price=75000, quantity=10),
    Product(id=3, name="headphones", description="wireless headphones", price=4500, quantity=50),
    Product(id=4, name="smartwatch", description="fitness smartwatch", price=12999, quantity=30),
    Product(id=5, name="tablet", description="10-inch tablet", price=24999, quantity=18),
    Product(id=6, name="camera", description="digital SLR camera", price=55999, quantity=8),
    Product(id=7, name="speaker", description="Bluetooth speaker", price=3499, quantity=60),
    Product(id=8, name="router", description="Wi-Fi 6 router", price=8999, quantity=22),
    Product(id=9, name="monitor", description="27-inch LED monitor", price=18999, quantity=15),
    Product(id=10, name="keyboard", description="mechanical keyboard", price=4999, quantity=40),
    Product(id=11, name="mouse", description="wireless ergonomic mouse", price=2299, quantity=55),
    Product(id=12, name="charger", description="fast charging adapter", price=1199, quantity=100),
    Product(id=13, name="powerbank", description="20000mAh power bank", price=2599, quantity=35),
    Product(id=14, name="webcam", description="HD webcam", price=6999, quantity=25)
]

@app.get("/products")   #all functions are async by default
def get_all_products():
    return products   #still this is not doing the data validation


#fetch one product
@app.get("/product/{id}") #we made it dynamic because here {id} is directly mapped with the product number 
def get_products_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
        
    return "Product not found"



#add data in the products
@app.post("/product")
def add_product(product : Product):  #Product = object (Pydantic model)
    products.append(product)
    return product

#put
@app.put("/product")
def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added successfully"
    
    return "Error: Product can't get updated"
#delete
@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
        
    return "Product not delected"