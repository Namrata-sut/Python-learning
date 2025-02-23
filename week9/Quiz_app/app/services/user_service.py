from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models.user_model import UserRole, User
from app.schemas.user_schema import CreateUserRequest
from app.utils import verify_password, create_access_token


class UserService:
    @staticmethod
    async def add_user(payload: CreateUserRequest, db: AsyncSession):
        new_user = User(username=payload.username,
                        email=payload.email,
                        password=payload.password,
                        role=UserRole.user)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    @staticmethod
    async def get_user(user_details: OAuth2PasswordRequestForm, db: AsyncSession):
        result = await db.execute(select(User).where(User.username == user_details.username))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The User does not exist")

        if not verify_password(user_details.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The Passwords do not match")

        access_token = create_access_token(data={"user_id": user.id})
        return access_token

    @staticmethod
    async def delete_user(user_id: int, db: AsyncSession):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The User does not exist")

        await db.delete(user)
        await db.commit()
        return "user deleted"

