from sqlalchemy import Column, Integer, ForeignKey, Float, Interval
from app.db.db_connection import Base


class Score(Base):
    """Represents a user's score for a quiz along with a timestamp."""
    __tablename__ = "score_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_table.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz_table.id'), nullable=False)
    score = Column(Float, nullable=False)
    timestamp = Column(Interval, nullable=False)

