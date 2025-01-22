from typing import Optional, List
from pydantic import BaseModel


class PokemonSchema(BaseModel):
    name: str
    height: int
    weight: int
    xp: int
    image_url: str
    pokemon_url: str
    abilities: List[dict]
    stats: List[dict]
    types: Optional[List[dict]] = None


class PokemonUpdateSchema(BaseModel):
    name: Optional[str] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    xp: Optional[int] = None
    image_url: Optional[str] = None
    pokemon_url: Optional[str] = None
    abilities: Optional[List[dict]] = None
    stats: Optional[List[dict]] = None
    types: Optional[List[dict]] = None

