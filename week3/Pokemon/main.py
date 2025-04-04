import requests
from fastapi import FastAPI, HTTPException, status

URL = "https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json"

pokemon_data = {}

app = FastAPI()


class PokemonNotFound(HTTPException):
    def __init__(self, pokemon_id: int):
        self.pokemon_id = pokemon_id
        self.detail = f"Pokemon with ID {self.pokemon_id} not found."
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=self.detail)


class PokemonEmptyDataError(HTTPException):
    def __init__(self):
        self.detail = "Pokemon data is empty."
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=self.detail)


@app.get("/load_pokemon_data")
def load_data():
    global pokemon_data
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            pokemon_data = {pokemon["id"]: pokemon for pokemon in response.json()}
            return pokemon_data
    except Exception as e:
        return {f"Error: {e}"}


@app.get("/pokemon/id/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    if pokemon_id in pokemon_data:
        return pokemon_data[pokemon_id]
    raise PokemonNotFound(pokemon_id)


@app.get("/pokemon/name")
def get_pokemon_by_name(pokemon_name: str):
    pokemon_name_lower = pokemon_name.lower()
    for pokemon in pokemon_data.values():
        if pokemon.get("name") == pokemon_name_lower:
            return pokemon
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pokemon not found.")


@app.get("/pokemon")
def get_all_pokemon():
    if pokemon_data:
        return pokemon_data
    raise PokemonEmptyDataError()


@app.post("/pokemon")
def add_pokemon(new_pokemon: dict):
    try:
        max_id = max([int(key) for key in pokemon_data.keys()], default=0)
        pokemon_id = max_id + 1
        new_pokemon["id"] = pokemon_id
        pokemon_data[pokemon_id] = new_pokemon
        return new_pokemon
    except Exception as e:
        return {f"Error: {e}"}


@app.put("/pokemon/id/{pokemon_id}")
def update_pokemon(pokemon_id: int, update_pokemon: dict):
    if not pokemon_data:
        raise PokemonEmptyDataError
    if pokemon_id in pokemon_data:
        pokemon_data[pokemon_id].update(update_pokemon)
        return {"message": "pokemon updated successfully", "pokemon": pokemon_data[pokemon_id]}
    raise PokemonNotFound(pokemon_id)


@app.delete("/pokemon/id/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    if not pokemon_data:
        raise PokemonEmptyDataError
    if pokemon_id in pokemon_data:
        pokemon_data.pop(pokemon_id)
        return {"message": "Pokemon deleted successfully"}
    raise PokemonNotFound(pokemon_id)
