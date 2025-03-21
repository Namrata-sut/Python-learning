from typing import Optional

from pydantic import BaseModel


class ExpenseSchema(BaseModel):
    name: str
    expense: Optional[float]


class ExpenseUpdateSchema(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
