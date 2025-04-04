from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status

from app.Schema.expense_schema import ExpenseSchema, ExpenseUpdateSchema
from app.models.expense_model import ExpenseModel


class ExpenseRepository:
    @staticmethod
    def create_expense(db: Session, data: ExpenseSchema):
        payload = ExpenseModel(
            name=data.name,
            expense=data.expense
        )

        db.add(payload)
        db.commit()
        return payload

    @staticmethod
    def get_expense(db: Session, id: int):
        expense_stmt = db.execute(select(ExpenseModel.id == id))
        result = expense_stmt.scalars().first()
        return result

    @staticmethod
    def update_expense(db: Session, id: int, data: ExpenseUpdateSchema):
        check_expense_exist = ExpenseRepository.get_expense(db, id)
        if not check_expense_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found.")

        for key, value in data.__dict__:
            setattr(check_expense_exist, key, value)

        db.commit()
        db.refresh(check_expense_exist)
