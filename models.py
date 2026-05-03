from pydantic import BaseModel


class ProductSchema(BaseModel):  #inheritance
    id: int
    name: str
    description: str
    price: int
    quantity: int

#since pydantic is installed we dont need to create a base model by ourself pydentic does it for us
'''
    def __init__(self, id:int, name: str, description:str, price:int, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
'''
