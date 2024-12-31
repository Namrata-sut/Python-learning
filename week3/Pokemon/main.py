import requests
from fastapi import FastAPI, HTTPException, status

URL = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"

pokemon_data = []

app = FastAPI()


@app.get("/load_pokemon")
def load_data():
    global pokemon_data
    response = requests.get(URL)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        raise Exception("Failed to fetch pokemon data")


@app.get("/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    for pokemon in pokemon_data:
        if pokemon.get("id") == pokemon_id:
            return pokemon
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")


@app.get("/pokemon_by_name/{pokemon_name}")
def get_pokemon_by_name(pokemon_name: str):
    for pokemon in pokemon_data:
        if pokemon.get("name") == pokemon_name:
            return pokemon
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pokemon not found.")


@app.get("/")
def get_all_pokemon():
    if pokemon_data:
        return pokemon_data
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Pokemon data is empty")


@app.delete("/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    for pokemon in pokemon_data:
        if pokemon.get("id") == pokemon_id:
            pokemon_data.remove(pokemon)
            return {"message": "Pokemon deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pokemon not found"
    )




