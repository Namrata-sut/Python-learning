from typing import List, Optional
from pydantic import BaseModel


class QuestionInputSchema(BaseModel):
    question: str
    options: List[str]
    answer: str
    category: str
    level: str


class QuestionUpdateSchema(BaseModel):
    question: Optional[str] = None
    options: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
    level: Optional[str] = None