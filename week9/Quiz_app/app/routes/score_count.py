from fastapi import Request, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates

from app.utils import get_current_user
from app.db.db_connection import get_db
from app.models.user_model import User
from app.services.score_service import process_quiz_submission

score_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@score_router.post("/submit_quiz")
async def submit_quiz(request: Request, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    result = await process_quiz_submission(request, db)

    if "error" in result:
        return {"error": result["error"]}

    return templates.TemplateResponse("score.html", {
        "request": request,
        "correct_count": result["correct_count"],
        "total_questions": result["total_questions"],
        "score_percentage": result["score"],
        "quiz_id": result["quiz_id"]
    })
