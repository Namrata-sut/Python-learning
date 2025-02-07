from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.models.pokemon_model import Pokemon
from app.schemas.pokemon_schema import PokemonSchema, PokemonUpdateSchema


class PokemonNotFound(HTTPException):
    def __init__(self, pokemon_id: int):
        self.pokemon_id = pokemon_id
        self.detail = f"Pokemon with ID {self.pokemon_id} not found."
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=self.detail)


class PokemonService:

    @staticmethod
    async def add_new_pokemon(payload: PokemonSchema, db: AsyncSession):
        data = Pokemon(
            name=payload.name,
            height=payload.height,
            weight=payload.weight,
            xp=payload.xp,
            image_url=payload.image_url,
            pokemon_url=payload.pokemon_url,
            abilities=payload.abilities,
            stats=payload.stats,
            types=payload.types
        )
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return PokemonSchema.model_validate(data.__dict__)

    @staticmethod
    async def get_all_pokemons(db: AsyncSession):
        result = await db.execute(select(Pokemon))
        pokemons = result.scalars().all()
        if not pokemons:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon data is empty.")
        return pokemons

    @staticmethod
    async def get_pokemon_by_id(pokemon_id: int, db: AsyncSession):
        query = select(Pokemon).where(Pokemon.id == pokemon_id)
        result = await db.execute(query)
        pokemon = result.scalars().first()
        if not pokemon:
            raise PokemonNotFound(pokemon_id)
        return pokemon

    @staticmethod
    async def get_pokemons_by_name(pokemon_name: str, db: AsyncSession):
        statement = select(Pokemon).where(func.lower(Pokemon.name) == pokemon_name.lower())
        result = await db.execute(statement)
        pokemons = result.scalars().all()
        if not pokemons:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon Not Found.")
        return pokemons

    @staticmethod
    async def update_existing_pokemon(pokemon_id: int, payload: PokemonUpdateSchema, db: AsyncSession):
        statement = select(Pokemon).where(Pokemon.id == pokemon_id)
        result = await db.execute(statement)
        existing_pokemon = result.scalars().first()
        if not existing_pokemon:
            raise PokemonNotFound(pokemon_id)

        for field, value in payload.dict(exclude_unset=True).items():
            setattr(existing_pokemon, field, value)
        await db.commit()
        await db.refresh(existing_pokemon)
        return existing_pokemon

    @staticmethod
    async def delete_pokemon(pokemon_id: int, db: AsyncSession):
        query = select(Pokemon).where(Pokemon.id == pokemon_id)
        result = await db.execute(query)
        pokemon = result.scalars().first()

        if not pokemon:
            raise PokemonNotFound(pokemon_id)

        await db.delete(pokemon)
        await db.commit()
        return {"message": "Pokemon deleted successfully"}

