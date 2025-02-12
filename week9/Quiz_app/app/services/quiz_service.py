from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.quiz_model import Quiz


class QuizService:
    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Quiz))
        quizzes = result.scalars().all()
        return quizzes

    @staticmethod
    async def get_by_category(category: str, db: AsyncSession):
        result = await db.execute(select(Quiz).where(func.lower(Quiz.category) == category.lower()))
        quizzes = result.scalars().all()
        return quizzes
