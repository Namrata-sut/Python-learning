from fastapi import FastAPI, HTTPException
from starlette import status
from app.db.database import drop_tables, create_tables

from app.db.database import PgDatabase

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Welcome to news app!'}


@app.post('/initdb')
async def initdb():
    try:
        # drop_tables()
        create_tables()
        return {"message": "Tables dropped and created!"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error {e}"
        )


@app.get("/pokemon_by_id")
async def get_pokemon_by_id(id: int):
    try:
        with PgDatabase() as db:
            db.cursor.execute(f"SELECT * FROM pokemon_table WHERE id = {id}")
            db.connection.commit()
            print("Data fetched successfully.")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error {e}")


# @app.post("/add_pokemon")
# async def add_pokemon():
#     try:
#         with PgDatabase() as db:
#             db.cursor.execute(f"""INSERT INTO pokemon_table (
#     name,
#     height,
#     weight,
#     xp,
#     image_url,
#     pokemon_url,
#     abilities,
#     stats,
#     types
# )
# VALUES (
#     'bulbasaur',
#     70,
#     69,
#     64,
#     'https://pokeres.bastionbot.org/images/pokemon/1.png',
#     'https://www.pokemon.com/us/pokedex/bulbasaur',
#     '[{"name": "overgrow", "is_hidden": false}, {"name": "chlorophyll", "is_hidden": true}]'::jsonb,
#     '[{"name": "hp", "base_stat": 45}, {"name": "attack", "base_stat": 49}, {"name": "defense", "base_stat": 49}, {"name": "special-attack", "base_stat": 65}, {"name": "special-defense", "base_stat": 65}, {"name": "speed", "base_stat": 45}]'::jsonb,
#     '[{"name": "grass"}, {"name": "poison"}]'::jsonb
# );
# """)
#             db.connection.commit()
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error {e}")
