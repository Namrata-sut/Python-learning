from typing import List

from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from app.db.db_connection import Base


class Question(Base):
    __tablename__ = "questions_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey('quiz_table.id'), nullable=False)
    question = Column(String, nullable=False)
    options = Column(JSON, nullable=False)
    answer = Column(String, nullable=False)


