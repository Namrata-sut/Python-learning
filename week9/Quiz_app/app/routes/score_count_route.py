from fastapi import Request, Depends, APIRouter
from fastapi.templating import Jinja2Templates

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_connection import get_db
from app.models.user_model import User
from app.services.score_service import process_quiz_submission
from app.utils import get_current_user

score_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@score_router.post("/submit_quiz")
async def submit_quiz(request: Request, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    """
        handles the submission of a quiz attempt by a user.
        this endpoint processes a quiz submission, calculates the score,
        and returns the results in an HTML template.
        Args:
            request (Request): The incoming HTTP request containing quiz answers.
            db (AsyncSession): The database session dependency.
            current_user (User): The authenticated user making the request.
        Returns:
            TemplateResponse: A rendered HTML template displaying the quiz results.
    """
    try:
        result = await process_quiz_submission(request, current_user, db)

        return templates.TemplateResponse("score.html", {
            "request": request,
            "correct_count": result["correct_count"],
            "total_questions": result["total_questions"],
            "score_percentage": result["score"],
            "quiz_id": result["quiz_id"]
        })
    except Exception as e:
        return {"Error Occurred": e}
