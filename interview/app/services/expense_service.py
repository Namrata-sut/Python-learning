from sqlalchemy.orm import Session

from app.Schema.expense_schema import ExpenseSchema, ExpenseUpdateSchema
from app.repositories.expense_repo import ExpenseRepository


class ExpenseService:
    @staticmethod
    def create_expense(db: Session, data: ExpenseSchema):
        return ExpenseRepository.create_expense(db, data)

    @staticmethod
    def get_expense(db: Session, id: int):
        return ExpenseRepository.get_expense(db, id)

    @staticmethod
    def update_expense(db: Session, id: int, data: ExpenseUpdateSchema):
        return ExpenseRepository.update_expense(db, id, data)
