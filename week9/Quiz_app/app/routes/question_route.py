from fastapi import APIRouter, Depends, Request

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.db.db_connection import get_db
from app.models.user_model import User
from app.schemas.question_schema import QuestionInputSchema, QuestionUpdateSchema
from app.services.question_service import QuestionService
from app.services.quiz_service import QuizService
from app.utils import admin_only, get_current_user

question_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@question_router.get("/quiz/{quiz_id}/questions", name="get_questions_by_quiz")
async def get_questions_by_quiz(quiz_id: int, request: Request, db: AsyncSession = Depends(get_db),
                                current_user: User = Depends(get_current_user)):
    """
        retrieve all questions for a specific quiz.
        Args:
            quiz_id (int): The ID of the quiz whose questions need to be fetched.
            request (Request): The HTTP request object.
            db (AsyncSession): The database session.
            current_user (User): The authenticated user.
        Returns:
            HTMLResponse: A rendered template displaying the quiz questions.
    """
    questions = await QuestionService.get_by_quiz_id(quiz_id, db)
    quiz_result = await QuizService.get_quiz_by_id(quiz_id, db)
    return templates.TemplateResponse("questions.html",
                                      {"request": request, "questions": questions, "quiz": quiz_result})


@question_router.get("/get_all_questions")
async def get_all_questions(db: AsyncSession = Depends(get_db),
                            current_user: User = Depends(admin_only)):
    """
        fetch all questions in the database.
        (admin only)
        Args:
            db (AsyncSession): The database session.
            current_user (User): The authenticated admin user.
        Returns:
            List[Question]: A list of all questions.
    """
    questions = await QuestionService.get_all(db)
    return questions


@question_router.post("/add_question")
async def add_question(payload: QuestionInputSchema, db: AsyncSession = Depends(get_db),
                       current_user: User = Depends(admin_only)):
    """
       add a new question to the database.
        (admin only)
       Args:
           payload (QuestionInputSchema):
            The question details including quiz ID, question text, options, and answer.
           db (AsyncSession): The database session.
           current_user (User): The authenticated admin user.
       Returns:
           Question: The newly created question.
       """
    question_added = await QuestionService.add(payload, db)
    return question_added


@question_router.patch("/update_question/{question_id}")
async def partial_update_question(question_id: int, payload: QuestionUpdateSchema,
                                  db: AsyncSession = Depends(get_db), current_user: User = Depends(admin_only)):
    """  partially update an existing question.
     (admin only)

    Args:
        question_id (int): The ID of the question to be updated.
        payload (QuestionUpdateSchema): The fields to update (optional fields).
        db (AsyncSession): The database session.
        current_user (User): The authenticated admin user.

    Returns:
        Question: The updated question object.
    """
    updated_question = await QuestionService.update(payload, question_id, db)
    return updated_question


@question_router.put("/update_question/{question_id}")
async def update_question(question_id: int, payload: QuestionInputSchema,
                          db: AsyncSession = Depends(get_db), current_user: User = Depends(admin_only)):
    """
     fully update an existing question.
      (admin only)
    Args:
        question_id (int): The ID of the question to be updated.
        payload (QuestionInputSchema): The complete updated question details.
        db (AsyncSession): The database session.
        current_user (User): The authenticated admin user.

    Returns:
        Question: The updated question object.
    """
    updated_question = await QuestionService.full_update(payload, question_id, db)
    return updated_question


@question_router.delete("/delete_question/{question_id}")
async def delete_question(question_id: int, db: AsyncSession = Depends(get_db),
                          current_user: User = Depends(admin_only)):
    """
       delete a question from the database.
        (admin only)
       Args:
           question_id (int): The ID of the question to delete.
           db (AsyncSession): The database session.
           current_user (User): The authenticated admin user.
       Returns:
           dict: A success message confirming deletion.
    """
    question_deleted = await QuestionService.delete(question_id, db)
    return question_deleted
