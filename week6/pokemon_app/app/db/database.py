# import psycopg2
# from psycopg2.extras import RealDictCursor
# from contextlib import contextmanager
#
# DATABASE_URL = "postgresql://postgres:gai3905@localhost/Pokemon"
#
#
# class Database:
#     def __init__(self):
#         self.connection = None
#
#     def connect(self):
#         self.connection = psycopg2.connect(DATABASE_URL)
#
#     def disconnect(self):
#         if self.connection:
#             self.connection.close()
#
#     @contextmanager
#     def get_cursor(self):
#         with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
#             yield cursor
#         self.connection.commit()
#
#
#     # pokemon_table = "pokemon_table"
#
#
#     def create_tables(self):
#         with self.get_cursor() as cursor:
#             cursor.execute(f"""CREATE TABLE pokemon_table (
#                 id SERIAL PRIMARY KEY,
#                 name VARCHAR(50) NOT NULL,
#                 height INTEGER NOT NULL,
#                 weight INTEGER NOT NULL,
#                 xp INTEGER NOT NULL,
#                 image_url TEXT NOT NULL,
#                 pokemon_url TEXT NOT NULL,
#                 abilities JSONB NOT NULL,
#                 stats JSONB NOT NULL,
#                 types JSONB NOT NULL
#                 );
#             """)
#             db = Database()
#             db.connect()
#             db.create_tables()
#             db.connection.commit()
#             print("Tables are created successfully...")
#
#
# def drop_tables():
#     with Database() as db:
#         db.cursor.execute(f"DROP TABLE IF EXISTS {pokemon_table} CASCADE;")
#         db.connection.commit()
#         print("Tables are dropped...")


# from pathlib import Path
# import dotenv
from abc import ABC, abstractmethod  # new
import psycopg2


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
            image_url VARCHAR(100) NOT NULL,
            pokemon_url VARCHAR(100) NOT NULL,
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
