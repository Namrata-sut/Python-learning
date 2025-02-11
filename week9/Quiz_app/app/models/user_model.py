from sqlalchemy import Column, Integer, String
from app.db.db_connection import Base


class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

