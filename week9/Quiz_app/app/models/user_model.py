from enum import Enum
from sqlalchemy import Column, Integer, String
from app.db.db_connection import Base
from sqlalchemy import Enum as SQLAlchemyEnum


class UserRole(str, Enum):  # Enum for roles
    """Enum representing user roles."""
    admin = "admin"
    user = "user"


class User(Base):
    """Represents a user with a username, email, password, and role."""
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), default=UserRole.user)
