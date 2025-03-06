"""
Responsável por definir os modelos do SQLAlchemy, que são as classes que definem as tabelas do banco de dados. 
Esses modelos são utilizados para fazer a comunicação com o banco de dados.

É aqui que definimos o nome da tabela, os campos e os tipos de dados. 
Conseguimos incluir campos gerados aleatoriamente, como o id e o created_at. 
Para o id, ao incluir o campo Integer, com o parâmetro primary_key=True, o SQLAlchemy já entende que esse campo é o id da tabela.
Para o created_at, ao incluir o campo DateTime, com o parâmetro default=datetime, o SQLAlchemy já entende que esse campo é a data de criação da tabela.

Lembrar:
- O models é agnóstico ao banco, ele não sabe qual é o banco que é criado! Ele vai importar o base do database!
- Declarar sua Tabela
"""


from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ProductModel(Base):
    __tablename__ = "products"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    categoria = Column(String, index=True)
    email_fornecedor = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)

