from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_connection import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserUpdateSchema, PartialUserUpdateSchema, UserResponse
from app.services.user_service import UserService
from app.utils import admin_only, get_current_user

user_router = APIRouter()


@user_router.get("/get_user_by_id/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(admin_only)):
    """
        retrieve user details by user ID.
        Args:
            user_id (int): The ID of the user to retrieve.
            db (AsyncSession): Database session dependency.
            current_user (User): The currently authenticated user.
        Returns:
            User: The user details retrieved from the database.
        """
    user = await UserService.get_user_by_id(user_id, db)
    return user


@user_router.put("/update_user/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, payload: UserUpdateSchema, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(admin_only)):
    """
        update an existing user with new data.
        Args:
            user_id (int): The ID of the user to update.
            payload (UserUpdateSchema): The updated user data.
            db (AsyncSession): Database session dependency.
            current_user (User): The currently authenticated admin user.
        Returns:
            User: The updated user details.
    """
    user_updated = await UserService.update_user(user_id, payload, db)
    return user_updated


@user_router.patch("/partial_update_user/{user_id}", response_model=UserResponse)
async def partial_update_user(user_id: int, payload: PartialUserUpdateSchema, db: AsyncSession = Depends(get_db),
                              current_user: User = Depends(admin_only)):
    """
        partially update an existing user's data.
        Args:
            user_id (int): The ID of the user to update.
            payload (PartialUserUpdateSchema): The partial user data update.
            db (AsyncSession): Database session dependency.
            current_user (User): The currently authenticated admin user.
        Returns:
            User: The updated user details.
    """
    user_updated = await UserService.partial_update_user(user_id, payload, db)
    return user_updated


@user_router.delete("/delete_user")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(admin_only)):
    """
        delete a user by ID.
        Args:
            user_id (int): The ID of the user to be deleted.
            db (AsyncSession): Database session dependency.
            current_user (User): The currently authenticated admin user.
        Returns:
            dict: Confirmation of user deletion.
    """
    user_deleted = await UserService.delete_user(user_id, db)
    return user_deleted
