# Import the necessary libraries
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from db import Base

# Define the User model
class User(Base):
    # Define the fields for the User model
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Define the __repr__ method to return a string representation of the User object
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Define the Item model
class Item(Base):
    # Define the fields for the Item model
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    is_offer = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Define the __repr__ method to return a string representation of the Item object
    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', price={self.price}, is_offer={self.is_offer})"