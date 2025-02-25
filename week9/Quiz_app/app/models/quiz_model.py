from sqlalchemy import Column, Integer, String
from app.db.db_connection import Base


class Quiz(Base):
    """Represents a quiz with a name, category, and difficulty level."""
    __tablename__ = "quiz_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    level = Column(String, nullable=False)


