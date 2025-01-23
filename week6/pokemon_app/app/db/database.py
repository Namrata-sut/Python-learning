from abc import ABC, abstractmethod
import psycopg2


class Database(ABC):
    """
        Abstract base class for database interactions.
        Provides a context manager for simplified database operations.
    """

    def __init__(self, driver) -> None:
        """ Initializes the database object.
        Args:
            driver: The database driver(e.g: postgresql)
        """
        self.driver = driver

    @abstractmethod
    def connect_to_database(self):
        """
            connects to the database using the specified driver.
            raises: Not Implemented Error: Subclass must implement this.
        """
        raise NotImplementedError()

    def __enter__(self):
        """ Enter the context manager.
            Establishes a connection to the database and creates a cursor.
        """
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exception_type, exc_val, traceback):
        """ Exits the context manager.
            Closes the cursor and the database connection.
        """
        self.cursor.close()
        self.connection.close()


class PgDatabase(Database):
    """PostgreSQL Database context manager."""

    def __init__(self) -> None:
        """ Initializes the PgDatabase object with the psycopg2 driver."""
        self.driver = psycopg2
        super().__init__(self.driver)

    def connect_to_database(self):
        """Connects to the PostgreSQL database using the specified configuration."""
        return self.driver.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="gai3905",
            database="pokemon_db"
        )


pokemon_table = "pokemon_table"


def create_tables():
    """creates the 'pokemon_table' in the PostgreSQL database."""
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
    """drops the 'pokemon_table' in the PostgreSQL database."""
    with PgDatabase() as db:
        db.cursor.execute(f"DROP TABLE IF EXISTS {pokemon_table} CASCADE;")
        db.connection.commit()
        print("Tables are dropped...")
