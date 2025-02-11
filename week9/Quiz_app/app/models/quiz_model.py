from sqlalchemy import Column, Integer, ForeignKey, Float, Interval, String
from app.db.db_connection import Base


class Quiz(Base):
    __tablename__ = "quiz_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    level = Column(String, nullable=False)


