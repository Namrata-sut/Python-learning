from fastapi import APIRouter, Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.utils import get_current_user
from app.db.db_connection import get_db
from app.models.quiz_model import Quiz
from app.models.user_model import User
from app.services.question_service import QuestionService

question_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@question_router.get("/quiz/{quiz_id}/questions", name="get_questions_by_quiz")
async def get_questions_by_quiz(quiz_id: int, request: Request, db: AsyncSession = Depends(get_db),
                                current_user: User = Depends(get_current_user)):
    questions = await QuestionService.get_by_quiz_id(quiz_id, db)
    quiz_result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
    quiz = quiz_result.scalars().first()
    return templates.TemplateResponse("questions.html", {"request": request, "questions": questions, "quiz": quiz})
