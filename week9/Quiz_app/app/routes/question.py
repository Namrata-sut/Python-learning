from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.db.db_connection import get_db
from app.services.question_service import QuestionService

question_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@question_router.get("/quiz/{quiz_id}/questions", name="get_questions_by_quiz")
async def get_questions_by_quiz(quiz_id: int, request: Request, db: AsyncSession = Depends(get_db)):
    questions = await QuestionService.get_by_quiz_id(quiz_id, db)
    return templates.TemplateResponse("questions.html", {"request": request, "questions": questions, "quiz_id": quiz_id})