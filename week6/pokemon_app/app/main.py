from fastapi import FastAPI, HTTPException, Path
from routers import pokemon_router

app = FastAPI()

app.include_router(pokemon_router.router)