from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_connection import get_db
from app.models.user_model import User
from app.services.user_service import UserService
from app.utils import admin_only

user_router = APIRouter()


@user_router.delete("/delete_user")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(admin_only)):
    user_deleted = await UserService.delete_user(user_id, db)
    return user_deleted


