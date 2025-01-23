import json
from fastapi import HTTPException
from starlette import status
from db.database import PgDatabase


class PokemonRepository:
    """A repository class for interacting with the pokemon_table in the database."""
    @staticmethod
    async def get_pokemon_by_id(pokemon_id: int):
        """Retrieves a single pokemon record from the database by its ID.
            Args:
                pokemon_id(int): The ID of the pokemon to retrieve.
            Returns: A pokemon record or None if no pokemon with the given ID is found.
        """
        try:
            with PgDatabase() as db:
                db.cursor.execute(f"SELECT * FROM pokemon_table WHERE id = {pokemon_id}")
                return db.cursor.fetchone()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error {e}")

    @staticmethod
    async def get_all_pokemon():
        """Retrieves all pokemon records present in database.
            Returns: A list of pokemon records.
        """
        try:
            with PgDatabase() as db:
                query = "SELECT * FROM pokemon_table;"
                db.cursor.execute(query)
                return db.cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error {e}")

    @staticmethod
    async def add_pokemon(payload: dict):
        """Adds a new pokemon record to the database.
            Args:
                payload(dict): A dictionary containing the pokemon data to be added.
                The dictionary must have followed keys:
                - name(str)
                - height(int)
                - weight(int)
                - xp(int)
                - image_url(str)
                - pokemon_url(str)
                - abilities(List[dict])
                - stats(List[dict])
                - types(List[dict], optional)
            Returns: True if the pokemon was added successfully.
        """
        try:
            query = """INSERT INTO pokemon_table (
                    name, height, weight, xp, image_url, pokemon_url, abilities, stats, types
                    )VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
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
        """ Deletes a pokemon record from the database by its ID.
            Args: pokemon_id(int): The ID of the pokemon to delete.
            Returns: True if the pokemon was deleted successfully, False otherwise.
        """
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
        """ Updates the existing pokemon records in the database.
            Args:
                pokemon_id(int): The ID of the pokemon to update.
                payload(dict): The dictionary containing the updated pokemon data.
            Returns: The updated pokemon record or None if the pokemon was not found.
            Raises: HTTPException: If the pokemon with the given ID is not found(404 NOT FOUND) or
                    if an error occurs during the update (400 BAD REQUEST)
        """
        try:
            processed_payload = {
                key: (json.dumps(value) if isinstance(value, (dict, list)) else value) for key, value in payload.items()
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
