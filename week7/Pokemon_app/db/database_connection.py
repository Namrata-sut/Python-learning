from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# URL = "postgresql+psycopg2-binary://postgres:gai3905@localhost:5432/pokemon_db"

url = URL.create(
    drivername="postgresql+asyncpg",
    username="postgres",
    password="gai3905",
    host="localhost",
    database="pokemon_db",
    port=5432
)

engine = create_async_engine(url)
SessionLocal = async_sessionmaker(bind=engine)
Base = declarative_base()


async def get_db():
    # async with engine.begin() as con:
    #     await con.run_sync(Base.metadata.create_all)
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
