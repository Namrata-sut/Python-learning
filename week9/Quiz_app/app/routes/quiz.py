from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.db.db_connection import get_db
from app.services.quiz_service import QuizService

quiz_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@quiz_router.get("/get_all_quizzes")
async def get_all_quizzes(request: Request, db: AsyncSession = Depends(get_db)):
    quizzes = await QuizService.get_all(db)
    return templates.TemplateResponse("quizzes.html", {"request": request, "quizzes": quizzes})
