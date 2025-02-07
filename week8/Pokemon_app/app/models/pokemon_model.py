from sqlalchemy import Column, String, Integer, JSON
from app.db.database_connection import Base


class Pokemon(Base):
    __tablename__ = "pokemon_new_data_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    xp = Column(Integer, nullable=False)
    image_url = Column(String, nullable=False)
    pokemon_url = Column(String, nullable=False)
    abilities = Column(JSON, nullable=False)
    stats = Column(JSON, nullable=False)
    types = Column(JSON, nullable=True)