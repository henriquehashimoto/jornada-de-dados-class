# CONFIGURAÇÃO DO BANCO DE DADOS

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

sqlalchemy_db_url = "sqlite:///./pokemon.db"
engine = create_engine(sqlalchemy_db_url)
Base = declarative_base()
     

sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

