from fastapi import APIRouter, Depends, Request, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.utils import get_current_user
from app.db.db_connection import get_db
from app.models.user_model import User
from app.services.quiz_service import QuizService

quiz_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@quiz_router.get("/get_all_quizzes")
async def get_all_quizzes(request: Request, db: AsyncSession = Depends(get_db),
                          current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized. Please log in.")
    quizzes = await QuizService.get_all(db)
    return templates.TemplateResponse("quizzes.html", {"request": request, "quizzes": quizzes})


@quiz_router.get("/get_quizzes_by_category")
async def search_category(request: Request, category_name: str, current_user: User = Depends(get_current_user)):
    if not category_name.isalpha():
        return templates.TemplateResponse("quizzes.html", {
            "request": request,
            "error": "Invalid Category. Please enter a valid string."
        })
    lower_category = category_name.lower()
    return RedirectResponse(url=f"/get_all_quizzes/{lower_category}", status_code=status.HTTP_303_SEE_OTHER)


@quiz_router.get("/get_all_quizzes/{category_name}")
async def get_quiz_by_category_level(requst: Request, category_name: str = Path(title="category."),
                                     db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    quizzes = await QuizService.get_by_category(category_name, db)
    return templates.TemplateResponse("quizzes.html", {
        "request": requst,
        "quizzes": quizzes,
        "search_name": category_name
    })
