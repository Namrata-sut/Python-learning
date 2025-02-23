from typing import Optional

from pydantic import BaseModel


class QuizInputSchema(BaseModel):
    name: str
    category: str
    level: str


class QuizUpdateSchema(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    level: Optional[str] = None
