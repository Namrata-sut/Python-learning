from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models.question_model import Question
from app.schemas.question_schema import QuestionInputSchema, QuestionUpdateSchema
from app.services.quiz_service import QuizService


class QuestionService:
    @staticmethod
    async def get_by_quiz_id(quiz_id: int, db: AsyncSession):
        result = await db.execute(select(Question).filter(Question.quiz_id == quiz_id))
        return result.scalars().all()

    @staticmethod
    async def get_all(db: AsyncSession):
        query = select(Question)
        result = await db.execute(query)
        question = result.scalars().all()
        return question

    @staticmethod
    async def add(payload: QuestionInputSchema, db: AsyncSession):
        quiz_exist = await QuizService.get_quiz_by_id(quiz_id=payload.quiz_id, db=db)
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not exist.")
        data = Question(
            question=payload.question,
            options=payload.options,
            answer=payload.answer,
            quiz_id=payload.quiz_id
        )
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return QuestionInputSchema.model_validate(data.__dict__)

    @staticmethod
    async def delete(question_id: int, db: AsyncSession):
        result = await db.execute(select(Question).where(Question.id == question_id))
        question_exist = result.scalars().first()
        if not question_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question Not Found.")

        await db.delete(question_exist)
        await db.commit()
        return "Question deleted."

    @staticmethod
    async def update(payload: QuestionUpdateSchema, question_id: int, db: AsyncSession):
        result = await db.execute(select(Question).where(Question.id == question_id))
        question_exist = result.scalars().first()
        if not question_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question Not found.")

        for key, value in payload.dict(exclude_unset=True).items():
            setattr(question_exist, key, value)

        await db.commit()
        await db.refresh(question_exist)
        return question_exist

    @staticmethod
    async def full_update(payload: QuestionInputSchema, question_id: int, db: AsyncSession):
        result = await db.execute(select(Question).where(Question.id == question_id))
        question_exist = result.scalars().first()
        if not question_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question Not found.")

        for key, value in payload.dict().items():
            setattr(question_exist, key, value)
        await db.commit()
        await db.refresh(question_exist)
        return question_exist

