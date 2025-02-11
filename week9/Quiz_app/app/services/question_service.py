from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.question_model import Question
from app.schemas.question import QuestionInputSchema, QuestionUpdateSchema


class QuestionService:
    @staticmethod
    async def get_by_quiz_id(quiz_id: int, db: AsyncSession):
        result = await db.execute(select(Question).filter(Question.quiz_id == quiz_id))
        return result.scalars().all()
    #
    # @staticmethod
    # async def get_all(db: AsyncSession):
    #     result = await db.execute(select(Question))
    #     questions = result.scalars().all()
    #     return questions
    #
    # @staticmethod
    # async def get_by_id(question_id: int, db: AsyncSession):
    #     query = select(Question).where(Question.id == question_id)
    #     result = await db.execute(query)
    #     question = result.scalars().first()
    #     return question
    #
    # @staticmethod
    # async def add(payload: QuestionInputSchema, db: AsyncSession):
    #     data = Question(
    #         question=payload.question,
    #         options=payload.options,
    #         answer=payload.answer,
    #         category=payload.category,
    #         level=payload.level
    #     )
    #     db.add(data)
    #     await db.commit()
    #     await db.refresh(data)
    #     return data
    #
    # @staticmethod
    # async def update(question_id: int, payload: QuestionUpdateSchema, db: AsyncSession):
    #     existing_question = await db.execute(select(Question).where(Question.id == question_id))
    #
    #     for key, value in payload.dict(exclude_unset=True).items():
    #         setattr(existing_question, key, value)
    #     await db.commit()
    #     await db.refresh(existing_question)
    #     return existing_question
    #
    # @staticmethod
    # async def delete(question_id: int, db: AsyncSession):
    #     existing_question = await db.execute(select(Question).where(Question.id == question_id))
    #     await db.delete(existing_question)
    #     await db.commit()
    #     return "Data deleted."
