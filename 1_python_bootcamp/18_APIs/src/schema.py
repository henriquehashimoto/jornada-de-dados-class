from pydantic import BaseModel


class PokemonSchema(BaseModel): # Pydantic roda uma verificação de tipos, setado abaixo
    name: str
    type: str 

    class Config:
        orm_mode = True