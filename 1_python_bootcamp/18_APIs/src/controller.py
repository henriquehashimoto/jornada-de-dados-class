# FUNÇÕES PARA PEGAR AS INFOMAÇÕES DESEJADAS

import requests 
from db import sessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema

def fetch_pokemon_data(id:int) -> PokemonSchema:
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    # Getting result from the api
    response = requests.get(url)

    if response.status_code == 200:        
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

    else: 
        return "Error getting the pokemon select id"


#=======================
# Add a new pokemon to db
#=======================
# The function will receive a pydantic (validate data), and will input into an ORM (db)
def add_pokemon_to_db (pokemon_schame: PokemonSchema) -> Pokemon:
    with sessionLocal() as db:
        db_pokemon = Pokemon(name = pokemon_schame.name, type = pokemon_schame.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    
    return db_pokemon