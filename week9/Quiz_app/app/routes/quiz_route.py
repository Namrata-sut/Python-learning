from fastapi import APIRouter, Depends, Request, Path, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from app.db.db_connection import get_db
from app.models.user_model import User
from app.schemas.quiz_schema import QuizInputSchema, QuizUpdateSchema
from app.services.quiz_service import QuizService
from app.utils import get_current_user, admin_only

quiz_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@quiz_router.get("/get_all_quizzes")
async def get_all_quizzes(request: Request, db: AsyncSession = Depends(get_db),
                          current_user: User = Depends(get_current_user)):
    """
        retrieve all quizzes available in the database.
        Args:
            request (Request): The HTTP request object.
            db (AsyncSession): The database session.
            current_user (User): The authenticated user.
        Returns:
            TemplateResponse: A rendered template displaying the list of quizzes.
        """
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized. Please log in.")
    quizzes = await QuizService.get_all(db)
    return templates.TemplateResponse("quizzes.html", {"request": request, "quizzes": quizzes})


@quiz_router.get("/get_quizzes_by_category")
async def search_category(request: Request, category_name: str, current_user: User = Depends(get_current_user)):
    """
        search for quizzes based on a category.
        Args:
            request (Request): The HTTP request object.
            category_name (str): The category to search for.
            current_user (User): The authenticated user.
        Returns:
            RedirectResponse: Redirects to the endpoint that fetches quizzes by category.
    """
    if not category_name.isalpha():
        return templates.TemplateResponse("quizzes.html", {
            "request": request,
            "error": "Invalid Category. Please enter a valid string."
        })
    lower_category = category_name.lower()
    return RedirectResponse(url=f"/get_all_quizzes/{lower_category}", status_code=status.HTTP_303_SEE_OTHER)


@quiz_router.get("/get_all_quizzes/{category_name}")
async def get_quiz_by_category(request: Request, category_name: str = Path(title="category."),
                               db: AsyncSession = Depends(get_db),
                               current_user: User = Depends(get_current_user)):
    """
        retrieve all quizzes that belong to a specific category.
        Args:
            request (Request): The HTTP request object.
            category_name (str): The category name to filter quizzes.
            db (AsyncSession): The database session.
            current_user (User): The authenticated user.
        Returns:
            TemplateResponse: A rendered template displaying quizzes under the specified category.
        """
    quizzes = await QuizService.get_by_category(category_name, db)
    return templates.TemplateResponse("quizzes.html", {
        "request": request,
        "quizzes": quizzes,
        "search_name": category_name
    })


@quiz_router.get("/get_quiz_by_id/{quiz_id}")
async def get_quiz_by_id(quiz_id: int, db: AsyncSession = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    """
        Retrieve a quiz by its unique ID.
        Args:
            quiz_id (int): The unique identifier of the quiz.
            db (AsyncSession): The database session.
            current_user (User): The authenticated user.
        Returns:
            Quiz: The requested quiz object.
    """
    quiz = await QuizService.get_quiz_by_id(quiz_id, db)
    return quiz


@quiz_router.post("/add_quiz")
async def add_quiz(payload: QuizInputSchema, db: AsyncSession = Depends(get_db),
                   current_user: User = Depends(admin_only)):
    """
        add a new quiz to the database.
         (admin only)
        Args:
            payload (QuizInputSchema): The quiz details including title, category, difficulty.
            db (AsyncSession): The database session.
            current_user (User): The authenticated admin user.
        Returns:
            Quiz: The newly created quiz.
        """
    added_quiz = await QuizService.add_quiz(payload, db)
    return added_quiz


@quiz_router.put("/update_quiz/{quiz_id}")
async def update_quiz(quiz_id: int, payload: QuizInputSchema, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(admin_only)):
    """
        fully update an existing quiz.
         (admin only)
        Args:
            quiz_id (int): The unique identifier of the quiz to be updated.
            payload (QuizInputSchema): The updated quiz details.
            db (AsyncSession): The database session.
            current_user (User): The authenticated admin user.
        Returns:
            Quiz: The updated quiz object.
    """
    updated_quiz = await QuizService.update_quiz(quiz_id, payload, db)
    return updated_quiz


@quiz_router.patch("/partial_update_quiz/{quiz_id}")
async def partial_update_quiz(quiz_id: int, payload: QuizUpdateSchema, db: AsyncSession = Depends(get_db),
                              current_user: User = Depends(admin_only)):
    """
        partially update a quiz.
         (admin only)
        Args:
            quiz_id (int): The unique identifier of the quiz to be updated.
            payload (QuizUpdateSchema): The fields to update (optional fields).
            db (AsyncSession): The database session.
            current_user (User): The authenticated admin user.
        Returns:
            Quiz: The updated quiz object.
    """
    updated_quiz = await QuizService.partial_update_quiz(quiz_id, payload, db)
    return updated_quiz


@quiz_router.delete("/delete_quiz")
async def delete_quiz(quiz_id: int, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(admin_only)):
    """
        delete a quiz from the database.
         (admin only)
        Args:
            quiz_id (int): The unique identifier of the quiz to be deleted.
            db (AsyncSession): The database session.
            current_user (User): The authenticated admin user.
        Returns:
            dict: A success message confirming deletion.
    """
    quiz_deleted = await QuizService.delete_quiz(quiz_id, db)
    return quiz_deleted
