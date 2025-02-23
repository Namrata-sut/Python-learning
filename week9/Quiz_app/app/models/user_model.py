from enum import Enum

from sqlalchemy import Column, Integer, String
from app.db.db_connection import Base

from sqlalchemy import Enum as SQLAlchemyEnum  # Import correctly


class UserRole(str, Enum):  # Enum for roles
    admin = "admin"
    user = "user"


class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), default=UserRole.user)
