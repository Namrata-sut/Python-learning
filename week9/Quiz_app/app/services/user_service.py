from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models.user_model import UserRole, User
from app.schemas.user_schema import CreateUserRequest, PartialUserUpdateSchema, UserUpdateSchema
from app.utils import verify_password, create_access_token


class UserService:
    """
        Service class for handling user-related operations in the system.
    """
    @staticmethod
    async def add_user(payload: CreateUserRequest, db: AsyncSession):
        """
        add a new user to the database.
        Args:
            payload (CreateUserRequest): The user data containing username, email, and password.
            db (AsyncSession): The asynchronous database session.
        Returns:
            User: The newly created user object after being committed to the database.
        """
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
        """
            authenticates a user based on username and password.
            Args:
                user_details: Form containing the username and password.
                db: Async database session.
            return: A generated access token for the authenticated user.
            raises HTTPException: If the user does not exist or password is incorrect.
        """
        result = await db.execute(select(User).where(User.username == user_details.username))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The User does not exist")

        if not verify_password(user_details.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The Passwords do not match")

        access_token = create_access_token(data={"user_id": user.id})
        return access_token

    @staticmethod
    async def get_user_by_id(user_id: int, db: AsyncSession):
        """
            retrieves a user by their ID.
            Args:
                user_id: The ID of the user.
                db: Async database session.
            return: The user object if found.
            raises HTTPException: If the user does not exist.
        """
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The User does not exist")
        return user

    @staticmethod
    async def update_user(user_id: int, payload: UserUpdateSchema, db: AsyncSession):
        """
            fully updates a user's information.
            Args:
                user_id (int): The ID of the user to update.
                payload (payload): The updated user data.
                db (AsyncSession): Async database session.
            return: The updated user object.
            raises HTTPException: If the user does not exist.
        """
        result = await db.execute(select(User).where(User.id == user_id))
        user_exist = result.scalars().first()
        if not user_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist.")
        for key, value in payload.dict().items():
            setattr(user_exist, key, value)
        await db.commit()
        await db.refresh(user_exist)
        return user_exist

    @staticmethod
    async def partial_update_user(user_id: int, payload: PartialUserUpdateSchema, db: AsyncSession):
        """
            partially updates a user's information, modifying only provided fields.
            Args:
                user_id: The ID of the user to update.
                payload: Partial data to update.
                db: Async database session.
            return: The updated user object.
            raises HTTPException: If the user does not exist.
        """
        result = await db.execute(select(User).where(User.id == user_id))
        user_exist = result.scalars().first()
        if not user_exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist.")
        for key, value in payload.dict(exclude_unset=True).items():
            setattr(user_exist, key, value)
        await db.commit()
        await db.refresh(user_exist)
        return user_exist

    @staticmethod
    async def delete_user(user_id: int, db: AsyncSession):
        """
          deletes a user from the database.
          args
                user_id: The ID of the user to delete.
                db: Async database session.
          return: Confirmation message upon successful deletion.
          raises HTTPException: If the user does not exist.
        """
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The User does not exist")

        await db.delete(user)
        await db.commit()
        return "user deleted"
