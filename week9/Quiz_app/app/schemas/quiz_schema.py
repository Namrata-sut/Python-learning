from typing import Optional
from pydantic import BaseModel


class QuizInputSchema(BaseModel):
    """
    Schema for creating a new quiz.
    Attributes:
        name (str): The name of the quiz.
        category (str): The category to which the quiz belongs.
        level (str): The difficulty level of the quiz.
    """
    name: str
    category: str
    level: str


class QuizUpdateSchema(BaseModel):
    """
    Schema for updating an existing quiz. Fields are optional.
    Attributes:
        name (Optional[str]): The updated name of the quiz.
        category (Optional[str]): The updated category of the quiz.
        level (Optional[str]): The updated difficulty level of the quiz.
    """
    name: Optional[str] = None
    category: Optional[str] = None
    level: Optional[str] = None
