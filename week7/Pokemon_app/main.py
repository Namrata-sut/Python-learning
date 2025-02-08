from fastapi import FastAPI

from routes import pokemon_router

app = FastAPI()

app.include_router(router=pokemon_router.router)

