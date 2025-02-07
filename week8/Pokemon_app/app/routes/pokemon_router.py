import json
from typing import List

import requests
from fastapi import APIRouter, Depends, HTTPException, Path, Form
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
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
        if data:
            return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.get("/get_all", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_all(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        pokemon_list = await PokemonService.get_all_pokemons(db)
        return templates.TemplateResponse("pokemon_list.html", {"request": request, "pokemons": pokemon_list})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


@router.get("/search_by_id")
async def search_pokemon(request: Request, pokemon_id: int):
    """Redirects to the correct path with the given Pokemon name."""
    return RedirectResponse(url=f"/pokemon_by_id/{pokemon_id}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/pokemon_by_id/{pokemon_id}", response_model=PokemonSchema, status_code=status.HTTP_200_OK)
async def get_by_id(request: Request,
                    pokemon_id: int = Path(title="Id of the pokemon", description="Id must be Integer."),
                    db: AsyncSession = Depends(get_db)):
    try:
        pokemon = await PokemonService.get_pokemon_by_id(pokemon_id, db)
        return templates.TemplateResponse("pokemon_list.html", {
            "request": request,
            "pokemons": [pokemon],
            "search_name": pokemon_id
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.get("/pokemon_by_name")
async def search_pokemon(request: Request, pokemon_name: str):
    """Redirects to the correct path with the given Pokemon name."""
    if not pokemon_name.isalpha():
        return templates.TemplateResponse("pokemon_list.html", {
            "request": request,
            "error": "Invalid Pokemon name. Please enter a valid string."
        })
    lower_pokemon_name = pokemon_name.lower()
    return RedirectResponse(url=f"/pokemon_by_name/{lower_pokemon_name}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/pokemon_by_name/{pokemon_name}", response_model=List[PokemonSchema], status_code=status.HTTP_200_OK)
async def get_by_name(request: Request,
                      pokemon_name: str = Path(title="Name of pokemon.", description="Pokemon name must be string."),
                      db: AsyncSession = Depends(get_db)):
    try:
        pokemons = await PokemonService.get_pokemons_by_name(pokemon_name, db)
        return templates.TemplateResponse("pokemon_list.html", {
            "request": request,
            "pokemons": pokemons,
            "search_name": pokemon_name
        })

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@router.get("/edit/{pokemon_id}", response_class=HTMLResponse, status_code=200)
async def edit_pokemon(request: Request, pokemon_id: int, db: AsyncSession = Depends(get_db)):
    # Fetch Pokemon from database
    pokemon = await PokemonService.get_pokemon_by_id(pokemon_id, db)
    if not pokemon:
        return HTMLResponse(content="Pokemon not found", status_code=404)

    return templates.TemplateResponse(
        "update_pokemon.html",
        {"request": request, "updated_pokemon": pokemon}
    )


@router.post("/update/{pokemon_id}", response_model=PokemonSchema, status_code=status.HTTP_200_OK)
async def update(
        request: Request,
        pokemon_id: int,
        db: AsyncSession = Depends(get_db),
        name: str = Form(...),
        height: int = Form(...),
        weight: int = Form(...),
        xp: int = Form(...),
        image_url: str = Form(...),
        pokemon_url: str = Form(...),
        abilities: str = Form(...),
        stats: str = Form(...),
        types: str = Form(...)

):
    abilities_list = json.loads(abilities)
    stats_list = json.loads(stats)
    types_list = json.loads(types)

    payload = PokemonUpdateSchema(
        name=name, height=height, weight=weight, xp=xp,
        image_url=image_url, pokemon_url=pokemon_url,
        abilities=abilities_list, stats=stats_list, types=types_list
    )
    updated_pokemon = await PokemonService.update_existing_pokemon(pokemon_id, payload, db)
    return RedirectResponse(url="/get_all", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/delete_pokemon/{pokemon_id}", status_code=status.HTTP_200_OK)
async def delete(request: Request, pokemon_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await PokemonService.delete_pokemon(pokemon_id, db)
        return RedirectResponse(url="/get_all", status_code=status.HTTP_303_SEE_OTHER)
        # return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")
