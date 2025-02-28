# Import necessary libraries
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import database
from typing import List, Union
from schema import Item, ItemBase, ItemCreate

# Create a new FastAPI application
app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)


#============================
# Define a route to create a new item
#============================
@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(database.get_db)):
    # Create a new item in the database
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


#============================
# Define a route to read all items
#============================
@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    # Get all items from the database, skipping the first 'skip' items and limiting to 'limit' items
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items


#============================
# Define a route to read a single item by ID
#============================
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    # Get the item from the database by ID
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    # If the item is not found, raise a 404 error
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


#============================
# Define a route to update an existing item
#============================
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(database.get_db)):
    # Get the item from the database by ID
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    # If the item is not found, raise a 404 error
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    # Update the item in the database
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


#============================
# Define a route to delete an item
#============================
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    # Get the item from the database by ID
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    # If the item is not found, raise a 404 error
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    # Delete the item from the database
    db.delete(db_item)
    db.commit()
    return db_item