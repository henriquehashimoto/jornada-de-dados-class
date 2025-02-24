import requests 
from pydantic import BaseModel

#=======================
# Criando contrato / schema / view da api
#=======================
class PokemonSchema(BaseModel): # Pydantic roda uma verificação de tipos, setado abaixo
    name: str
    type: str 

    class Config:
        orm_mode = True


def get_pokemon(id:int) -> PokemonSchema:
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'

    # Getting result from the api
    response = requests.get(url)
    poke_data = response.json()

    # Getting only the types information
    poke_types = poke_data["types"]

    # Creating a list with all types
    types_list = []
    for type in poke_types:
        types_list.append(type['type']['name'])

    # Splitting by , 
    types = ' ,'.join(types_list)
    
    return PokemonSchema(name = poke_data["name"], type = types)



#=======================
#=======================

if __name__ == "__main__":
    print(get_pokemon(15))
    print(get_pokemon(25))

