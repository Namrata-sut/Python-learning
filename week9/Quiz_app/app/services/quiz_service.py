from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.models.quiz_model import Quiz
from app.schemas.quiz_schema import QuizInputSchema, QuizUpdateSchema


class QuizService:
    """
        Service class for handling quiz-related operations.
    """

    @staticmethod
    async def get_all(db: AsyncSession):
        """
            retrieves all quizzes from the database.
            arg: db: Async database session.
            return: List of Quizzes.
        """
        result = await db.execute(select(Quiz))
        quizzes = result.scalars().all()
        return quizzes

    @staticmethod
    async def get_by_category(category: str, db: AsyncSession):
        """
            Retrieves quizzes filtered by category.

            Args:
             category: Category of the quiz.
             db: Async database session.
            return: List of Quizzes in the specified category.
        """
        result = await db.execute(select(Quiz).where(func.lower(Quiz.category) == category.lower()))
        quizzes = result.scalars().all()
        return quizzes

    @staticmethod
    async def get_quiz_by_id(quiz_id: int, db: AsyncSession):
        """
            Retrieves a quiz by its ID.
            Args:
             quiz_id: The unique ID of the quiz.
             db: Async database session.
            return: Quiz if found, otherwise raises HTTP 404 error.
        """
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz = result.scalars().first()
        if not quiz:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found.")
        return quiz

    @staticmethod
    async def add_quiz(payload: QuizInputSchema, db: AsyncSession):
        """
        Adds a new quiz to the database.
        Args:
         payload: QuizInputSchema containing quiz details.
         db: Async database session.
        return: The created Quiz object.
        """
        data = Quiz(
            name=payload.name,
            category=payload.category,
            level=payload.level
        )
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update_quiz(quiz_id: int, payload: QuizInputSchema, db: AsyncSession):
        """
        Fully updates a quiz with new data.
        Args:
            quiz_id: The unique ID of the quiz.
            payload: QuizInputSchema with updated quiz details.
            db: Async database session.
        return: Updated Quiz object.
        """
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz_exist = result.scalars().first()
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz does not exist.")

        for key, value in payload.dict().items():
            setattr(quiz_exist, key, value)

        await db.commit()
        await db.refresh(quiz_exist)
        return quiz_exist

    @staticmethod
    async def partial_update_quiz(quiz_id: int, payload: QuizUpdateSchema, db: AsyncSession):
        """
        Partially updates a quiz with new data.
        Args:
         quiz_id: The unique ID of the quiz.
         payload: QuizUpdateSchema containing partial quiz details.
         db: Async database session.
        return: Updated Quiz object.
        """
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz_exist = result.scalars().first()
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz does not exist.")

        for key, value in payload.dict(exclude_unset=True).items():
            setattr(quiz_exist, key, value)

        await db.commit()
        await db.refresh(quiz_exist)
        return quiz_exist

    @staticmethod
    async def delete_quiz(quiz_id: int, db: AsyncSession):
        """
        Deletes a quiz from the database.
        Args:
         quiz_id: The unique ID of the quiz to delete.
         db: Async database session.
        return: Success message if deletion is successful.
        """
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz_exist = result.scalars().first()
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz does not exist.")
        await db.delete(quiz_exist)
        await db.commit()
        return "Quiz deleted."
