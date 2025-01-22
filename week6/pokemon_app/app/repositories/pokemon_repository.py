import json
from fastapi import HTTPException
from starlette import status
from db.database import PgDatabase


class PokemonRepository:
    @staticmethod
    async def get_pokemon_by_id(pokemon_id: int):
        try:
            with PgDatabase() as db:
                db.cursor.execute(f"SELECT * FROM pokemon_table WHERE id = {pokemon_id}")
                return db.cursor.fetchone()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error {e}")

    @staticmethod
    async def get_all_pokemon():
        try:
            with PgDatabase() as db:
                query = "SELECT * FROM pokemon_table;"
                db.cursor.execute(query)
                return db.cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error {e}")

    @staticmethod
    async def add_pokemon(payload: dict):
        try:
            query = """INSERT INTO pokemon_table (
                                    name, height, weight, xp, image_url, pokemon_url, abilities, stats, types
                                )
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = [
                payload["name"],
                payload["height"],
                payload["weight"],
                payload["xp"],
                str(payload["image_url"]),
                str(payload["pokemon_url"]),
                json.dumps(payload["abilities"]),
                json.dumps(payload["stats"]),
                json.dumps(payload.get("types", []))
            ]
            with PgDatabase() as db:
                db.cursor.execute(query, data)
                db.connection.commit()
                return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")

    @staticmethod
    async def delete_pokemon(pokemon_id: int):
        query = f"DELETE FROM pokemon_table WHERE id = {pokemon_id}"
        try:
            with PgDatabase() as db:
                db.cursor.execute(query)
                db.connection.commit()
                res = db.cursor.statusmessage
            if res == "DELETE 1":
                return True
            return False
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error deleting Pokemon: {e}")

    @staticmethod
    async def update_pokemon(pokemon_id: int, payload: dict):
        try:
            processed_payload = {
                key: (json.dumps(value) if isinstance(value, (dict, list)) else value)
                for key, value in payload.items()
            }
            columns = ", ".join(f"{key} = %s" for key in processed_payload.keys())
            query = f"UPDATE pokemon_table SET {columns} WHERE id = %s"

            values = list(processed_payload.values()) + [pokemon_id]
            with PgDatabase() as db:
                record_exist = await PokemonRepository.get_pokemon_by_id(pokemon_id)
                if not record_exist:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon Not Found.")

                db.cursor.execute(query, values)
                db.connection.commit()
                result = await PokemonRepository.get_pokemon_by_id(pokemon_id)
                return result
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")
