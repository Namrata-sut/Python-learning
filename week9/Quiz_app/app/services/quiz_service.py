from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models.quiz_model import Quiz
from app.schemas.quiz_schema import QuizInputSchema, QuizUpdateSchema


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

    @staticmethod
    async def get_quiz_by_id(quiz_id: int, db: AsyncSession):
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz = result.scalars().first()
        if not quiz:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found.")
        return quiz

    @staticmethod
    async def add_quiz(payload: QuizInputSchema, db: AsyncSession):
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
    async def delete_quiz(quiz_id: int, db: AsyncSession):
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz_exist = result.scalars().first()
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not exist.")
        await db.delete(quiz_exist)
        await db.commit()
        return "Quiz deleted."

    @staticmethod
    async def update_quiz(quiz_id: int, payload: QuizInputSchema, db: AsyncSession):
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz_exist = result.scalars().first()
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not exist.")
        for key, value in payload.dict().items():
            setattr(quiz_exist, key, value)

        await db.commit()
        await db.refresh(quiz_exist)
        return quiz_exist

    @staticmethod
    async def partial_update_quiz(quiz_id: int, payload: QuizUpdateSchema, db: AsyncSession):
        result = await db.execute(select(Quiz).where(Quiz.id == quiz_id))
        quiz_exist = result.scalars().first()
        if not quiz_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not exist.")
        for key, value in payload.dict(exclude_unset=True).items():
            setattr(quiz_exist, key, value)

        await db.commit()
        await db.refresh(quiz_exist)
        return quiz_exist

