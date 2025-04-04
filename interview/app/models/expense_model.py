from sqlalchemy import Column, Integer, String, Float

from app.db_connection.db_connection import Base


class ExpenseModel(Base):
    __tablename__ = "expense_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    expense = Column(Float, nullable=True)
