# Import the necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create an engine to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a base class for our models
Base = declarative_base()

# Create a session maker to create sessions to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a function to get a database session
def get_db():
    # Create a new session
    db = SessionLocal()
    try:
        yield db
    finally:        
        db.close()