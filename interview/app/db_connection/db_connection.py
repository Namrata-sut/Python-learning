from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = URL.create(
    host="localhost",
    drivername="postgresql",
    username="postgres",
    password="gai3905",
    database="Expense_db",
    port=5432
)

engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

