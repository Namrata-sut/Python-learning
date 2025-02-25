import os
from dotenv import load_dotenv
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

# Load environment variables from the .env file
load_dotenv()

# Construct the database URL using environment variables
DATABASE_URL = URL.create(
        host=os.getenv("DB_HOST", "localhost"),
        drivername=os.getenv("DB_DRIVER", "postgresql+asyncpg"),
        username=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "gai3905"),
        database=os.getenv("DB_NAME", "quiz_db"),
        port=os.getenv("DB_PORT", 5432),
)

# Create an asynchronous database engine
engine = create_async_engine(url=DATABASE_URL)

# Create a session factory for handling database transactions
session = async_sessionmaker(bind=engine)

# Define the base class for ORM models
Base = declarative_base()


async def get_db():
    """
       Asynchronous generator function to provide a database session.

       This function creates a new database session and yields it for use in
       asynchronous operations. After the operation is complete, it ensures that
       the session is properly closed.

       Yields:
           AsyncSession: An asynchronous database session instance.
    """
    db = session()
    try:
        yield db
    finally:
        await db.close()

