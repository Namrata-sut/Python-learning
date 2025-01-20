# from pathlib import Path
# import dotenv
from abc import ABC, abstractmethod  # new
import psycopg2

# BASE_DIR = Path(__file__).resolve().parent.parent
# dotenv.load_dotenv(BASE_DIR / ".env")


class Database(ABC):
    """
    Database context manager
    """

    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractmethod
    def connect_to_database(self):
        raise NotImplementedError()

    def __enter__(self):
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exception_type, exc_val, traceback):
        self.cursor.close()
        self.connection.close()


class PgDatabase(Database):
    """PostgreSQL Database context manager"""

    def __init__(self) -> None:
        self.driver = psycopg2
        super().__init__(self.driver)

    def connect_to_database(self):
        return self.driver.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="gai3905",
            database="pokemon_db"
        )


pokemon_table = "pokemon_table"


def create_tables():
    with PgDatabase() as db:
        db.cursor.execute(f"""CREATE TABLE {pokemon_table} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            height INTEGER NOT NULL,
            weight INTEGER NOT NULL,
            xp INTEGER NOT NULL,
            image_url TEXT NOT NULL,
            pokemon_url TEXT NOT NULL,
            abilities JSONB NOT NULL,
            stats JSONB NOT NULL,
            types JSONB NOT NULL
            );
        """)
        db.connection.commit()
        print("Tables are created successfully...")


def drop_tables():
    with PgDatabase() as db:
        db.cursor.execute(f"DROP TABLE IF EXISTS {pokemon_table} CASCADE;")
        db.connection.commit()
        print("Tables are dropped...")
