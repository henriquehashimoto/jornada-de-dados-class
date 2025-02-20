import requests 


url = 'https://pokeapi.co/api/v2/pokemon/15'

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
print(types)

