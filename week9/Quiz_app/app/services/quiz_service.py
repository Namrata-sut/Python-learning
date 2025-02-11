from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.quiz_model import Quiz


class QuizService:
    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Quiz))
        quizzes = result.scalars().all()
        return quizzes
        