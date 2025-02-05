from typing import List
import requests

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.db.database_connection import get_db
from app.schemas.pokemon_schema import PokemonSchema, PokemonUpdateSchema
from app.services.pokemon_service import PokemonService

router = APIRouter()
templates = Jinja2Templates(directory='app/templates')


@router.get("/load_data")
async def load_data(URL: str, db: AsyncSession = Depends(get_db)):
    try:
        response = requests.get(URL)
        pokemon_data = response.json()

        def remove_id(_data):
            if isinstance(_data, list):
                return [remove_id(item) for item in _data]
            elif isinstance(_data, dict):
                return {key: remove_id(value) for key, value in _data.items() if key != 'id'}
            else:
                return _data

        cleaned_data = remove_id(pokemon_data)
        for data in cleaned_data:
            pokemon = PokemonSchema(**data)
            await PokemonService.add_new_pokemon(pokemon, db)
        return {"status": True, "message": "data added successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.get("/create/", response_class=HTMLResponse)
def create_form(request: Request):
    return templates.TemplateResponse("create_pokemon.html", {"request": request})


@router.post("/create/", response_model=PokemonSchema, status_code=status.HTTP_201_CREATED)
async def create(payload: PokemonSchema, db: AsyncSession = Depends(get_db)):
    try:
        data = await PokemonService.add_new_pokemon(payload, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.get("/read_data", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_all(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        pokemon_list = await PokemonService.get_all_pokemons(db)
        print(pokemon_list)
        return templates.TemplateResponse("pokemon_list.html", {"request": request, "pokemons": pokemon_list})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


@router.get("/pokemon/{pokemon_id}", response_model=PokemonSchema, status_code=status.HTTP_200_OK)
async def get_by_id(pokemon_id: int = Path(title="Id of the pokemon", description="Id must be Integer."),
                    db: AsyncSession = Depends(get_db)):
    try:
        pokemon = await PokemonService.get_pokemon_by_id(pokemon_id, db)
        return pokemon
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.put("/pokemon", response_model=PokemonSchema, status_code=status.HTTP_200_OK)
async def update(pokemon_id: int, payload: PokemonUpdateSchema, db: AsyncSession = Depends(get_db)):
    try:
        updated_pokemon = await PokemonService.update_existing_pokemon(pokemon_id, payload, db)
        return updated_pokemon
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.delete("/pokemon/{pokemon_id}", status_code=status.HTTP_200_OK)
async def delete(pokemon_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await PokemonService.delete_pokemon(pokemon_id, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.get("/pokemon_by_name/{pokemon_name}", response_model=List[PokemonSchema], status_code=status.HTTP_200_OK)
async def get_by_name(pokemon_name: str = Path(title="Name of pokemon.", description="Pokemon name must be string."),
                      db: AsyncSession = Depends(get_db)):
    try:
        if not pokemon_name.isalpha():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pokemon name must be a valid string.")
        pokemons = await PokemonService.get_pokemons_by_name(pokemon_name, db)
        return pokemons

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")
