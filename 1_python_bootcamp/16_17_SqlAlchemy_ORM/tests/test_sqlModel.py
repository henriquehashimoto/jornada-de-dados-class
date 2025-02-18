from typing import Optional

from sqlmodel import Field, SQLModel, Session, create_engine


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# An engine that will create a sql lite db
engine = create_engine("sqlite:///tests/database.db",echo=True)
SQLModel.metadata.create_all(engine)


# Creating objects of the class Hero (db name of the example), that will be added to the db
hero_1 = Hero(name="deadpool", secret_name="Dive wilson")
hero_2 = Hero(name="spider man", secret_name="Peter Park")
hero_3 = Hero(name="iron man", secret_name="Tony Stark", age=46)


# Loop to add all objects in the created database
with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
