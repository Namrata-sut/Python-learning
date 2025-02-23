from typing import List, Optional
from pydantic import BaseModel


class QuestionInputSchema(BaseModel):
    question: str
    options: List[str]
    answer: str
    quiz_id: int


class QuestionUpdateSchema(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    quiz_id: Optional[int] = None
