import requests
from fastapi import HTTPException, Path
from starlette import status
from models.pokemon import PokemonSchema, PokemonUpdateSchema
from repositories.pokemon_repository import PokemonRepository
from fastapi import APIRouter

router = APIRouter()
URL = 'https://raw.githubusercontent.com/DetainedDeveloper/Pokedex/master/pokedex_raw/pokedex_raw_array.json'


@router.get('/')
async def load_pokemon_data():
    response = requests.get(URL)
    pokemon_data = response.json()

    def remove_id(data):
        if isinstance(data, dict):
            return {key: remove_id(value) for key, value in data.items() if key != 'id'}
        elif isinstance(data, list):
            return [remove_id(item) for item in data]
        else:
            return data

    cleaned_data = remove_id(pokemon_data)
    for pokemon in cleaned_data:
        new_pokemon_data = await PokemonRepository.add_pokemon(pokemon)
        if not new_pokemon_data:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data not added.")
    return {"Success": True, "message": "Data added successfully."}


@router.get("/pokemon/{pokemon_id}")
async def get_by_id(pokemon_id: int = Path(..., title="Pokemon ID",
                                           description="The unique ID of the Pokémon (must be an integer).")):
    pokemon = await PokemonRepository.get_pokemon_by_id(pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pokemon not found.")
    return pokemon


@router.get("/pokemon")
async def get_all():
    pokemons = await PokemonRepository.get_all_pokemon()
    if not pokemons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon data is empty..")
    return pokemons


@router.post("/pokemon")
async def add(payload: PokemonSchema):
    payload_dict = payload.dict(exclude_unset=True)
    pokemon = await PokemonRepository.add_pokemon(payload_dict)
    if not pokemon:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Pokemon not added.")
    return {"Success": True, "message": "Data added successfully."}


@router.delete("/pokemon/{pokemon_id}")
async def delete(pokemon_id: int):
    pokemon = await PokemonRepository.delete_pokemon(pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pokemon not Found.")
    return {"Success": True, "message": "Data deleted successfully."}


@router.put("/pokemon/{pokemon_id}")
async def update(pokemon_id: int, payload: PokemonUpdateSchema):
    update_fields = []
    values = []

    payload_dict = payload.dict(exclude_unset=True)
    if not payload_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update.")

    for key, value in payload_dict.items():
        update_fields.append(key)
        values.append(value)

    data = {key: values[i] for i, key in enumerate(update_fields)}
    pokemon_updated = await PokemonRepository.update_pokemon(pokemon_id, data)
    return {"success": True, "message": "Pokemon data updated successfully.", "data": pokemon_updated}

