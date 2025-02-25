from typing import List, Optional
from pydantic import BaseModel


class QuestionInputSchema(BaseModel):
    """
        Schema for creating a new question.
        Attributes:
            question (str): The text of the question.
            options (List[str]): A list of possible answers.
            answer (str): The correct answer from the options.
            quiz_id (int): The ID of the associated quiz.
    """
    question: str
    options: List[str]
    answer: str
    quiz_id: int


class QuestionUpdateSchema(BaseModel):
    """
        Schema for updating an existing question. Fields are optional.
        Attributes:
            question (Optional[str]): The updated question text.
            options (Optional[List[str]]): Updated list of answer choices.
            answer (Optional[str]): Updated correct answer.
            quiz_id (Optional[int]): Updated quiz association.
    """
    question: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    quiz_id: Optional[int] = None
