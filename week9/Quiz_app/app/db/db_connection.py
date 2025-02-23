import time

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# DATABASE_URL = URL.create(
#         host="localhost",
#         drivername="postgresql+asyncpg",
#         username="postgres",
#         password="gai3905",
#         database="quiz_db",
#         port=5432,
# )
DATABASE_URL = "postgresql+asyncpg://postgres:gai3905@localhost:5432/quiz_db"

import logging
logging.basicConfig(level=logging.DEBUG)

engine = create_async_engine(url=DATABASE_URL)
session = async_sessionmaker(bind=engine)
Base = declarative_base()


async def get_db():
    while True:
        try:
            async with engine.begin() as con:
                await con.run_sync(Base.metadata.create_all)
            break
        except ConnectionRefusedError:
            print('database connection refused, retrying in 5 seconds...')
            time.sleep(5)
    db = session()
    try:
        yield db
    finally:
        await db.close()

