import requests
from fastapi import FastAPI, HTTPException, status

URL = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"

pokemon_data = []

# pokemon= [
#   {
#     "id": 1,
#     "name": "bulbasaur",
#     "height": 70,
#     "weight": 69,
#     "xp": 64,
#     "image_url": "https://pokeres.bastionbot.org/images/pokemon/1.png",
#     "pokemon_url": "https://www.pokemon.com/us/pokedex/bulbasaur",
#     "abilities": [
#       {
#         "name": "overgrow",
#         "is_hidden": False
#       },
#       {
#         "name": "chlorophyll",
#         "is_hidden": True
#       }
#     ],
#     "stats": [
#       {
#         "name": "hp",
#         "base_stat": 45
#       },
#       {
#         "name": "attack",
#         "base_stat": 49
#       },
#       {
#         "name": "defense",
#         "base_stat": 49
#       },
#       {
#         "name": "special-attack",
#         "base_stat": 65
#       },
#       {
#         "name": "special-defense",
#         "base_stat": 65
#       },
#       {
#         "name": "speed",
#         "base_stat": 45
#       }
#     ],
#     "types": [
#       {
#         "name": "grass"
#       },
#       {
#         "name": "poison"
#       }
#     ]
#   },
#  ]


app = FastAPI()


@app.get("/load_pokemon_data")
def load_data():
    global pokemon_data
    response = requests.get(URL)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        raise Exception("Failed to fetch pokemon data")


@app.get("/pokemon/id/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    for pokemon in pokemon_data:
        if pokemon.get("id") == pokemon_id:
            return pokemon
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")


@app.get("/pokemon/name/{pokemon_name}")
def get_pokemon_by_name(pokemon_name: str):
    for pokemon in pokemon_data:
        if pokemon.get("name") == pokemon_name:
            return pokemon
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pokemon not found.")


@app.get("/pokemon")
def get_all_pokemon():
    if pokemon_data:
        return pokemon_data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon data is empty.")


@app.post("/pokemon")
def add_pokemon(new_pokemon: dict):
    max_id = max([_pokemon.get("id") for _pokemon in pokemon_data], default=0)
    pokemon_id = max_id + 1
    new_pokemon["id"] = pokemon_id
    pokemon_data.append(new_pokemon)
    return new_pokemon


@app.put("/pokemon/id/{pokemon_id}")
def update_pokemon(pokemon_id: int, update_pokemon: dict):
    for i, pokemon in enumerate(pokemon_data):
        if pokemon.get("id") == pokemon_id:
            update_pokemon["id"] = pokemon_id
            pokemon_data[i] = update_pokemon
            return {"message": "pokemon updated successfully", "pokemon": pokemon_data[i]}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")


@app.delete("/pokemon/id/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    for pokemon in pokemon_data:
        if pokemon.get("id") == pokemon_id:
            pokemon_data.remove(pokemon)
            return {"message": "Pokemon deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Pokemon not found")
