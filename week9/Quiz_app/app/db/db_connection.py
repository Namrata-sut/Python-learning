from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = URL.create(
        drivername="postgresql+asyncpg",
        username="postgres",
        password="gai3905",
        database="quiz_db",
        port=5432,
)

engine = create_async_engine(url=DATABASE_URL)
session = async_sessionmaker(bind=engine)
Base = declarative_base()


async def get_db():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)
    db = session()
    try:
        yield db
    finally:
        await db.close()

