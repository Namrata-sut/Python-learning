from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.question_model import Question
from app.schemas.question import QuestionInputSchema, QuestionUpdateSchema


class QuestionService:
    @staticmethod
    async def get_by_quiz_id(quiz_id: int, db: AsyncSession):
        result = await db.execute(select(Question).filter(Question.quiz_id == quiz_id))
        return result.scalars().all()
