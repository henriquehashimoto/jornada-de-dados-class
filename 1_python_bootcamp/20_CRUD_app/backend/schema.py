"""
Responsável por definir os schemas do Pydantic, que são as classes que definem os tipos de dados que serão utilizados na API. 
Esses schemas são utilizados para fazer a validação dos dados que são recebidos na API, e também para definir os tipos de dados que são retornados pela API.

Temos o schema ProductBase, que é o schema base para o cadastro de produtos. 
Esse schema é utilizado para fazer a validação dos dados que são recebidos na API, e também para definir os tipos de dados que são retornados pela API.

Temos o schema ProductCreate, que é o schema que é retornado pela API. 
Ele é uma classe que herda do schema ProductBase, e possui um campo a mais, que é o id. Esse campo é utilizado para identificar o produto no banco de dados.

Temos o schema ProductResponse, que é o schema que é retornado pela API. 
Ele é uma classe que herda do schema ProductBase, e possui dois campos a mais, que é o id e o created_at. Esses campos são gerados pelo nosso banco de dados.

Temos o schema ProductUpdate, que é o schema que é recebido pela API para update. 
Ele possui os campos opcionais, pois não é necessário enviar todos os campos para fazer o update.

"""


from pydantic import BaseModel, PositiveFloat, EmailStr, field_validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    @field_validator("categoria")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @field_validator("categoria", pre=True, always=True)
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")
