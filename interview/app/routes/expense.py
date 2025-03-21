from fastapi import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.Schema.expense_schema import ExpenseSchema
from app.db_connection.db_connection import get_db
from app.services.expense_service import ExpenseService

from app.Schema.expense_schema import ExpenseUpdateSchema

router = APIRouter()


@router.post("/expense/", response_model=ExpenseSchema)
async def create_expense(expense: ExpenseSchema):
    return expense


@router.get("/expense/{id}")
def get_expense(id: int, db: Session = Depends(get_db)):
    expense = ExpenseService.get_expense(db, id)
    return expense


@router.put("/expense/{id}")
def update_expense(data: ExpenseUpdateSchema, id: int, db: Session = Depends(get_db)):
    updated_expense = ExpenseService.update_expense(db, id, data)
    return updated_expense
