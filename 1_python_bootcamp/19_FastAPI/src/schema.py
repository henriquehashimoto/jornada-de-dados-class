# Import the necessary libraries
from pydantic import BaseModel
from typing import Union

# Define a base class for our models; for automatic data validations and support of Pydantic advanced data type
class ItemBase(BaseModel):
    # Define the fields for the Item model
    name: str
    price: float
    is_offer: Union[bool, None] = None


# Define a class for creating new items
class ItemCreate(ItemBase):
    # This class inherits from ItemBase and adds no new fields
    pass


# Define a class for representing items in the database
class Item(ItemBase):
    # This class inherits from ItemBase and adds an 'id' field
    id: int