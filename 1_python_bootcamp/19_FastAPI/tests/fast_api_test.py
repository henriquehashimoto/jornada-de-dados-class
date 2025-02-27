from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

# Declaring my API
app = FastAPI()


#================================
# Building data validation with pydantic
#================================
class Item_check(BaseModel):
    name: str
    price: float
    is_offer: bool


#================================
# Building my APIs parameters
#================================
# Initial page 
@app.get("/") 
def read_root():
    return{"Hello":"World"}


# Getting page items of a certain declared in URL item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id": item_id, "q": q}


# Putting info into the api
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item_check):
    return {"item_name": item.name, "item_id": item_id}


